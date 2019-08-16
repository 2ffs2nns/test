# Example lambda project

This project was created to provide an example on how to setup a CI pipeline to build, test, deploy a simple lambda function in AWS. It was built on osx and has some dependencies to get started.
* AWS account
* go-task - https://taskfile.dev/#/installation
* docker - https://docs.docker.com/install
* terraform - https://learn.hashicorp.com/terraform/getting-started/install.html
* aws-cli - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html 

# Getting started
* Ensure you're an admin in the AWS account and install the dependencies following their respective install docs.
* The taskfile.yml contains the execution bits. The list of targets can be found with `task --list`
```
task --list
task: Available tasks for this project:
* build: 	Run terraform init/apply cmds to "build" the project
and deploy a AWS apigateway and lambda function.

* ci: 			Run build, test, destroy tasks
* create_s3: 		Create a s3 bucket
* destroy: 		Teardown tf infrastructure
* package_lambda: 	Package up the python dependencies
* post_lambda: 		Post lambda function to s3
* test: 		Test terraform .tf files including integration tests.
The "{{.API_GATEWAY_URL}}" var is written by taskvars.tf
and made available by Taskvars.yml for a quick/dirty
integration test. Test tools:

tflint - linter for AWS provider-specific issues
terraform validate - syntax checker
curl - quick/dirty integration test utilizing dynamic variables
```

# Lambda function
Since I have no production experience w/lambda I thought I'd put together a simple, single function project. It sets up a lambda function in python that queries Google for the terms "devops" and "cancer"
