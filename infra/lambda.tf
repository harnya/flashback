

resource "aws_lambda_function" "memory_lambda_tf" {

  function_name = format("%s_lambda_tf", var.project_name)
  role          = aws_iam_role.iam_lambda.arn
  package_type = "Image"
  image_uri = format("%s:latest",aws_ecr_repository.memory-tf.repository_url)
  depends_on = [
    # aws_iam_role_policy_attachment.lambda_attach_policy,
    aws_cloudwatch_log_group.lambda_log,
    aws_ecr_repository.memory-tf,
  ]
}


resource "aws_lambda_function_url" "lambda_function_url" {
  function_name      = aws_lambda_function.memory_lambda_tf.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = false
    allow_origins     = ["*"]

  }
}

