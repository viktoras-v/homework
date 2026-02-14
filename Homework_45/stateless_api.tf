terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}


# DynamoDB
resource "aws_dynamodb_table" "Cars_2" {
  name           = "Cars_2"
  billing_mode   = "PAY_PER_REQUEST"
  #read_capacity  = 20
  #write_capacity = 20
  hash_key       = "CarsId"
  
   attribute {
    name = "CarsId"
    type = "S"
  }
}


# Policy
resource "aws_iam_policy" "cars_2" {
  name = "Dynamo_cars_2"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "dynamodb:PutItem"
        Resource = aws_dynamodb_table.Cars_2.arn
      }
    ]
  })
}


# Role
resource "aws_iam_role" "lambda_cars_2" {
  name = "role_cars_2"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_cars_2_attach" {
  role       = aws_iam_role.lambda_cars_2.name
  policy_arn = aws_iam_policy.cars_2.arn
}



# Lambda
resource "aws_lambda_function" "lambda_cars_2" {
  function_name = "cars-2-function"

  runtime = "python3.12"   
  handler = "lambda_function.lambda_handler"

  role = aws_iam_role.lambda_cars_2.arn

  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")

  timeout     = 10
  memory_size = 128
}



# API GW
resource "aws_api_gateway_rest_api" "api_cars_2" {
  name        = "Cars_2"
  description = "API for Cars Lambda integration"
#  lifecycle {
#    prevent_destroy = true
#  }
}

resource "aws_api_gateway_resource" "root" {
  rest_api_id = aws_api_gateway_rest_api.api_cars_2.id
  parent_id   = aws_api_gateway_rest_api.api_cars_2.root_resource_id
  path_part   = "cars_2"
}

resource "aws_api_gateway_method" "post_cars_2" {
  rest_api_id   = aws_api_gateway_rest_api.api_cars_2.id
  resource_id   = aws_api_gateway_resource.root.id
  http_method   = "POST"
  authorization = "NONE"
  api_key_required = true
}

resource "aws_api_gateway_integration" "lambda_cars_2" {
  rest_api_id = aws_api_gateway_rest_api.api_cars_2.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.post_cars_2.http_method
  type        = "AWS_PROXY"
  integration_http_method = "POST"
  uri         = aws_lambda_function.lambda_cars_2.invoke_arn
}

resource "aws_lambda_permission" "apigw_invoke" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_cars_2.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api_cars_2.execution_arn}/*/*"
}

resource "aws_api_gateway_deployment" "cars_2_deployment" {
  depends_on = [
    aws_api_gateway_integration.lambda_cars_2
  ]

  rest_api_id = aws_api_gateway_rest_api.api_cars_2.id
  stage_name  = "prod"
}


# 1. Create API API Key
resource "aws_api_gateway_api_key" "cars_2_key" {
  name        = "Cars_2_API_Key"
  description = "API key for Cars_2 API"
  enabled     = true
 # lifecycle {
 #   prevent_destroy = true
 # }
}



# Create Usage Plan
resource "aws_api_gateway_usage_plan" "cars_2_plan" {
  name = "Cars_2_UsagePlan"
  description = "Usage plan for Cars_2 API"

  api_stages {
    api_id = aws_api_gateway_rest_api.api_cars_2.id
    stage  = aws_api_gateway_deployment.cars_2_deployment.stage_name
  }

  throttle_settings {
    burst_limit = 10
    rate_limit  = 10
  }

  quota_settings {
    limit  = 1000
    period = "MONTH"
  }
}



# Assign Key to Usage Plan
resource "aws_api_gateway_usage_plan_key" "cars_2_key_attachment" {
  key_id        = aws_api_gateway_api_key.cars_2_key.id
  key_type      = "API_KEY"
  usage_plan_id = aws_api_gateway_usage_plan.cars_2_plan.id
}










  
