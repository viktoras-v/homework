terraform {
  backend "s3" {
    bucket = "book-app-ca-terraform-state"
    key    = "book-app-ca/terraform.tfstate"
    region = "eu-central-1"
  }
}



