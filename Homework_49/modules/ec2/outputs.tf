output "instance_ids" {
  value = aws_instance.my_ec2[*].id
}

output "private_ips" {
  value = aws_instance.my_ec2[*].private_ip
}
