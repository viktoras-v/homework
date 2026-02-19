resource "aws_instance" "my_ec2" {
  count         = var.instance_count
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.subnet_ids[count.index % length(var.subnet_ids)]

  tags = {
    Name = "app-${count.index}"
  }
}
