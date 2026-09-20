# StudyBuddy

**Author:** PULLURI VYSHNAVI

Paste your lecture notes and get a short summary and a 5-question practice quiz, in the language you choose. Built on AWS for the WeMakeDevs x AWS Bharat Builds Tour (First Commit).

## How it works
1. The user sends notes to the `POST /study` endpoint.
2. API Gateway passes the request to an AWS Lambda function.
3. Lambda asks Amazon Bedrock to write the summary and quiz.
4. The result is saved in DynamoDB and returned as JSON.

## AWS services
- **Lambda:** runs the backend (`lambda_function.py`)
- **API Gateway:** public `POST /study` endpoint
- **Amazon Bedrock:** generates the summary and quiz
- **DynamoDB:** stores each result
- **S3:** optional storage for uploaded notes
- **Amplify:** hosts the frontend (in progress)

## Setup
Set these environment variables on the Lambda function:
- `MODEL_ID`: a Bedrock model ID you have access to
- `TABLE_NAME`: your DynamoDB table name (optional)
- `UPLOAD_BUCKET`: your S3 bucket name (optional)

The Lambda role needs permission for `bedrock:InvokeModel` and `dynamodb:PutItem` (and `s3:GetObject` if you use S3).

## Example request
`{"text": "Photosynthesis converts light into chemical energy...", "language": "Hindi"}`

## License
MIT
