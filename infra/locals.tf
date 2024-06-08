locals {
  aws_account_id = "${var.aws_account_id == "" ? data.aws_caller_identity.current.account_id : var.aws_account_id}"
}
locals {
  bucket_name = format("%s-%s",var.project_name, tostring(data.aws_caller_identity.current.account_id))
}