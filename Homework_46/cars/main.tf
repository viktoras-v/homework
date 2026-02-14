provider "aws" {
  region = "eu-central-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

resource "aws_s3_bucket" "cars" {
  bucket = "aws-sam-cli-managed-default-samclisourcebucket-spabc1v0h9ox"
}
