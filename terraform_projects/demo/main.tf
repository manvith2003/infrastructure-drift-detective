terraform {
  required_version = ">= 1.3.0"
}

provider "local" {}

resource "local_file" "example" {
  filename = "${path.module}/hello.txt"
  content  = "Hello Terraform"
}
