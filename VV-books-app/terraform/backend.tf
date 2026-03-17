terraform {
  backend "s3" {
    bucket = "book-app-ca-terraform-state"
    key    = "VV-book-app-ca/terraform.tfstate"
    region = "eu-central-1"
  }
}



