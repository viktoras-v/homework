terraform {
  backend "s3" {
    bucket = "ca-devops-ua6-demo-bucket"
    key    = "terraform.tfstate"
    region = "eu-central-1"
  }
}
  