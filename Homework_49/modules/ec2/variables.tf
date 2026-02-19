variable "ami_id" {
  type = string
  default = "ami-0c42fad2ea005202d"
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "subnet_ids" {
  type = list(string)
}

variable "instance_count" {
  type    = number
  default = 2
}
