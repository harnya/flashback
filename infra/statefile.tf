terraform {
  backend "s3" {
    bucket         = "memory-339713056590"
    key            = "memory_ops/memory-state-file.tfstate"
    region         = "ap-south-1"
    encrypt        = true
  }
}
