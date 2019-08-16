resource "local_file" "taskvars_yml" {
  content  = "API_GATEWAY_URL: ${aws_api_gateway_deployment.example.invoke_url}"
  filename = "${path.module}/taskvars.yml"
}
