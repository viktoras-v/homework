variable "region" {
  type    = string
  default = "eu-central-1"
}

variable "ami_id" {
  type = string
}

variable "subnet_ids" {
  type = list(string)
  default = [
  "subnet-aaa",
  "subnet-bbb"
]
}

variable "public_subnet_cidrs" {
  type = list(string)
}

variable "azs" {
  type = list(string)
}


