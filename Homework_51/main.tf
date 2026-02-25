
variable "environment" {
    type = string
    default = "dev"
}

locals {
  ingress_by_env = {
    dev = [
      { port = 22, cidr = "10.0.0.0/16", desc = "SSH dev" }
      { port = 80, cidr = "10.0.0.0/16", desc = "HTTP" }
    ]
    prod = [
      { port = 22, cidr = "10.0.0.0/16", desc = "SSH internal" },
      { port = 443, cidr = "0.0.0.0/0", desc = "HTTPS" }
    ]
  }
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "vpc"
  }
}


resource "aws_security_group" "sg" {
  name   = "sg"
  vpc_id = aws_vpc.main.id
  depends_on = [ aws_vpc.main ]    # Explicite

  dynamic "ingress" {
    for_each = local.ingress_by_env[var.environment]
    content {
      description = ingress.value.desc
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = [ingress.value.cidr]
    }
  }
  lifecycle {
  create_before_destroy = true
}
}