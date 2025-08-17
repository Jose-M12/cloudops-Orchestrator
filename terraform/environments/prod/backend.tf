terraform {
  backend "s3" {
    bucket         = "cloudops-terraform-state-prod"
    key            = "prod.tfstate"
    region         = "us-east-1"
    dynamodb_table = "cloudops-tf-locks-prod"
    encrypt        = true
  }
}
