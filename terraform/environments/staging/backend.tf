terraform {
  backend "s3" {
    bucket         = "cloudops-terraform-state-staging"
    key            = "staging.tfstate"
    region         = "us-east-1"
    dynamodb_table = "cloudops-tf-locks-staging"
    encrypt        = true
  }
}
