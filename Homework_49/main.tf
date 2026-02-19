

# Network Load Balancer
resource "aws_lb" "nlb" {
  name               = "example-nlb"
  load_balancer_type = "network"

  subnets = module.network.public_subnet_ids
}

resource "aws_lb_target_group" "tg" {
  name        = "example-tg"
  port        = 80
  protocol    = "TCP"
  vpc_id      = module.network.vpc_id
}

resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_lb.nlb.arn
  port              = 80
  protocol          = "TCP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.tg.arn
  }
}

resource "aws_lb_target_group_attachment" "ec2" {
  count = length(module.ec2.instance_ids)

  target_group_arn = aws_lb_target_group.tg.arn
  target_id        = module.ec2.instance_ids[count.index]
  port             = 80
}





module "network" {
  source = "./modules/network"

  public_subnet_cidrs = var.public_subnet_cidrs
  azs                 = var.azs
}

module "ec2" {
  source = "./modules/ec2"

  ami_id     = var.ami_id
  subnet_ids = module.network.public_subnet_ids
  instance_type = "t3.micro"
  instance_count = 2
}



