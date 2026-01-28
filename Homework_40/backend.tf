terraform {
  backend "s3" {
    bucket = "VV-demo-bucket"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}
  
