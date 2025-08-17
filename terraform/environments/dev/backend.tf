terraform {
  backend "s3" {
    bucket         = "cloudops-terraform-state-dev"
    key            = "dev.tfstate"
    region         = "us-east-1"
    dynamodb_table = "cloudops-tf-locks-dev"
    encrypt        = true
  }
}
