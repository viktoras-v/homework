

resource "aws_instance" "example" {
  ami           = "ami-0b6c6ebed2801a5cb"  # замени на свой AMI
  instance_type = "t2.micro"
  key_name      = "MyKeyPair"              # твой ключ

  # Security Group
  vpc_security_group_ids = ["sg-0821e286182681ca7"]

  # public IP
  associate_public_ip_address = true

  tags = {
    Name = "MyTerraformInstance"
  }
}


#resource "aws_s3_bucket" "bucket1" {
 # bucket = "vvv-demo-bucket1"
  #force_destroy = true
#}


#resource "aws_s3_bucket" "bucket2" {
 # bucket = "vvv-demo-bucket2"
  #force_destroy = true
#}
#resource "aws_s3_bucket" "bucket3" {
 # bucket = "vvv-demo-bucket3"
  #force_destroy = true
#}
