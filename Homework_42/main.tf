# Creating VPC

resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "DevOpsVPC"
  }
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-central-1a"

  tags = {
    Name = "DevOpsPublicSubnet"
  }
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "eu-central-1a"

  tags = {
    Name = "DevOpsPrivateSubnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "DevOpsInternetGateway"
  }
}

resource "aws_route_table" "devops" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "DevOpsRouteTable"
  }
}

resource "aws_eip" "nat" {
  
  tags = {
    Name = "DevOpsNATElasticIP"
  }
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "DevOpsNATGateway"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.devops.id
}

resource "aws_route" "public_internet" {
  route_table_id         = aws_route_table.devops.id
  destination_cidr_block = var.public_route_cidr
  gateway_id             = aws_internet_gateway.igw.id
}

resource "aws_route" "private_nat" {
  route_table_id         = aws_route_table.devops.id
  destination_cidr_block = var.private_route_cidr
  nat_gateway_id         = aws_nat_gateway.nat.id
}


# Inbound rule SSH
resource "aws_security_group" "devops_sg" {
  name        = "devops-sg"
  description = "Security group for DevOps instances"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
# Create EC2
resource "aws_instance" "example" {
  ami           = "ami-01f79b1e4a5c64257"
  instance_type = "t2.micro"
  key_name      = "MyKeyPair"     

  vpc_security_group_ids = [aws_security_group.devops_sg.id]
  subnet_id = aws_subnet.public.id


  associate_public_ip_address = true

  tags = {
    Name = "MyTerraformInstance"
  }
}


