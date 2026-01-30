resource "aws_s3_bucket" "bucket1" {
  bucket = "vvv-demo-bucket1"
}


resource "aws_s3_bucket" "bucket2" {
  bucket = "vvv-demo-bucket2"
  force_destroy = true
}
resource "aws_s3_bucket" "bucket3" {
  bucket = "vvv-demo-bucket3"
  force_destroy = true
}
