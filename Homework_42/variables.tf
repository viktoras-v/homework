variable "public_route_cidr" {
  description = "public_CIDR"
  type        = string
  default     = "0.0.0.0/0"
}

  variable "private_route_cidr" {
  description = "private_CIDR"
  type        = string
  default     = "10.2.0.0/24"
}
