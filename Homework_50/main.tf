locals {
#   name_suffix = "${var.resource_tags["project"]}-${var.resource_tags["environment"]}"
    name_suffix = "${var.project_name}-${var.environment}"
}

locals {
    required_tags = {
    project= var.project_name,
    environment = var.environment
    }
tags = merge(var.resource_tags, local.required_tags)
}

resource "aws_instance" "app_server" {
    ami= "ami-01f79b1e4a5c64257"
    instance_type = "t2.micro"
#    tags = 
#       Name = "YetAnotherName"
#       Name = "app-server-${var.resource_tags["project"]}-${var.resource_tags["environment"]}"
#       Name = "app-server-${local.name_suffix}"
#       tags = merge(local.tags, {Name = "app-server-${local.name_suffix}"}")
        tags = merge(
  local.tags,
  {
    Name = "app-server-${local.name_suffix}"
  }
)
}

resource "aws_instance" "backend_server" {
    ami= "ami-0d118c6e63bcb554e"
    instance_type = "t2.micro"
#    tags = {
#       Name = "backend-server-${var.resource_tags["project"]}-${var.resource_tags["environment"]}"
#       Name = "backend-server-${local.name_suffix}"
        tags = merge(local.tags, {Name = "backend-server-${local.name_suffix}"})
}
