resource "aws_ecr_repository" "memory-tf" {
  name                 = format("%s-tf",var.project_name)
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}
