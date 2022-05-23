# Lambda Example

## Step 1

Create AWS ECR repository from AWS console.
https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html
## Step 2

Publish the docker image:

0. `aws configure` and set the credentials

1. `aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${registryUrl}`

2. `docker build -t lambda-test .`

3. `docker tag lambda-test:latest ${registryUrl}/lambda-test:latest`

4. `docker push ${registryUrl}/lambda-test:latest`

## Step 3

Create lambda function from AWS console

1. Choose create function
2. Choose container image
3. Choose Test & create an event with the JSON `{ "name": "John Smith" }`
4. Save the event & execute