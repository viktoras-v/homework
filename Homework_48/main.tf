
# DynamoDB
resource "aws_dynamodb_table" "Cars" {
  name           = "Cars"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "Cars_id"
  
   attribute {
    name = "Cars_id"
    type = "S"
  }
}


# Policy
resource "aws_iam_policy" "cars" {
  name = "Dynamo_cars"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow" 
        Action   = [ 
          "dynamodb:PutItem",
          "dynamodb:Scan"
        ]
        Resource = aws_dynamodb_table.Cars.arn
      }
    ]
  })
}


# Role
resource "aws_iam_role" "lambda_cars" {
  name = "role_cars"

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

resource "aws_iam_role_policy_attachment" "lambda_cars_attach" {
  role       = aws_iam_role.lambda_cars.name
  policy_arn = aws_iam_policy.cars.arn
}



# Lambda
resource "aws_lambda_function" "lambda_cars" {
  function_name = "cars-function"

  runtime = var.python_version  
  handler = "handler.handler"

  role = aws_iam_role.lambda_cars.arn

  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")

  timeout     = 10
  memory_size = 128
}



# API GW
resource "aws_api_gateway_rest_api" "api_cars" {
  name        = "Cars"
  description = "API for Cars Lambda integration"
#  lifecycle {
#    prevent_destroy = true
#  }
}

resource "aws_api_gateway_resource" "root" {
  rest_api_id = aws_api_gateway_rest_api.api_cars.id
  parent_id   = aws_api_gateway_rest_api.api_cars.root_resource_id
  path_part   = "cars"
}

# POST
resource "aws_api_gateway_method" "post_cars" {
  rest_api_id   = aws_api_gateway_rest_api.api_cars.id
  resource_id   = aws_api_gateway_resource.root.id
  http_method   = "POST"
  authorization = "NONE"
  api_key_required = true
}
resource "aws_api_gateway_integration" "lambda_post_cars" {
  rest_api_id = aws_api_gateway_rest_api.api_cars.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.post_cars.http_method
  type        = "AWS_PROXY"
  integration_http_method = "POST"
  uri         = aws_lambda_function.lambda_cars.invoke_arn
}



# GET
resource "aws_api_gateway_method" "get_cars" {
  rest_api_id   = aws_api_gateway_rest_api.api_cars.id
  resource_id   = aws_api_gateway_resource.root.id
  http_method   = "GET"
  authorization = "NONE"
  api_key_required = true
}
resource "aws_api_gateway_integration" "lambda_get_cars" {
  rest_api_id = aws_api_gateway_rest_api.api_cars.id
  resource_id = aws_api_gateway_resource.root.id
  http_method = aws_api_gateway_method.get_cars.http_method
  type        = "AWS_PROXY"
  integration_http_method = "POST"
  uri         = aws_lambda_function.lambda_cars.invoke_arn
}



resource "aws_lambda_permission" "apigw_invoke" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_cars.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api_cars.execution_arn}/*/*"
}

# Deploy
resource "aws_api_gateway_deployment" "cars_deployment" {
  depends_on = [
    aws_api_gateway_integration.lambda_get_cars,
    aws_api_gateway_integration.lambda_post_cars
  ]

  rest_api_id = aws_api_gateway_rest_api.api_cars.id
  stage_name  = "dev"
  

# Triggers for automatic re-deploy
 triggers = {
    redeploy = sha1(jsonencode([
      aws_api_gateway_method.get_cars.id,
      aws_api_gateway_method.post_cars.id,
      aws_api_gateway_integration.lambda_get_cars.id,
      aws_api_gateway_integration.lambda_post_cars.id
    ]))
  }
}


 


# Create API key
resource "aws_api_gateway_api_key" "cars_key" {
  name        = "Cars_API_Key"
  description = "API key for Cars API"
  enabled     = true
 # lifecycle {
 #   prevent_destroy = true
 # }
}



# Create Usage Plan
resource "aws_api_gateway_usage_plan" "cars_plan" {
  name = "Cars_UsagePlan"
  description = "Usage plan for Cars API"

  api_stages {
    api_id = aws_api_gateway_rest_api.api_cars.id
    stage  = aws_api_gateway_deployment.cars_deployment.stage_name
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
resource "aws_api_gateway_usage_plan_key" "cars_key_attachment" {
  key_id        = aws_api_gateway_api_key.cars_key.id
  key_type      = "API_KEY"
  usage_plan_id = aws_api_gateway_usage_plan.cars_plan.id
}










  
