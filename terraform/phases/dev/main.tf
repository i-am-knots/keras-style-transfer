provider "google" {
  project     = "257220959067"
  region      = "us-central1"
  zone        = "us-central1-c"
}

locals {
  environment   = "dev"
  instance_name = "knots-style-transfer-${local.environment}"
}

module "gcp_instance" {
  source = "../../modules/gcp-instance"

  environment   = local.environment
  instance_name = local.instance_name
}