provider "aws" {
  region = var.region
}


# Create EC2 MySql
resource "aws_instance" "app" {
  ami           = "ami-01f79b1e4a5c64257"
  instance_type = "t2.micro"
  key_name      = "my_key"
  vpc_security_group_ids = [aws_security_group.app.id]
  #subnet_id = aws_subnet.public_subnet.id
  associate_public_ip_address = true
  tags = {
    Name = "ec2-VV-book-app"
  }
}

resource "aws_security_group" "app" {
  name = "VV-books-app-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

