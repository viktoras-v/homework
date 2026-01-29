# resource "aws_iam_openid_connect_provider" "github" {
#   url = "https://token.actions.githubusercontent.com"

#   client_id_list = [
#     "sts.amazonaws.com"
#   ]

#   thumbprint_list = [
#     "6938fd4d98bab03faadb97b34396831e3780aea1" # Current GitHub OIDC thumbprint
#   ]

#   tags = {
#     Name = "github-oidc-provider"
#   }
# }

# IAM Role that GitHub Actions can assume
resource "aws_iam_role" "github_actions_role" {
  name = "github-actions-role-${var.repo_name}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Federated = "arn:aws:iam::413648731451:oidc-provider/token.actions.githubusercontent.com"
        },
        Action = "sts:AssumeRoleWithWebIdentity",
        Condition = {
          StringEquals = {"token.actions.githubusercontent.com:aud" = "sts.amazonaws.com"}
          StringLike = {"token.actions.githubusercontent.com:sub" = "repo:${var.repo_user}/${var.repo_name}:*"}
}

      }
    ]
  })

  tags = {
    Name = "github-actions-role-${var.repo_name}"
  }
}

# Example: Policy Attachment for the IAM Role
resource "aws_iam_role_policy_attachment" "attach_policy" {
  role       = aws_iam_role.github_actions_role.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess" # Example policy
}