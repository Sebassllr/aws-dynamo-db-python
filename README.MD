# AWS-DynamoDB-Table-Registers-Cloner

Project to clone the registers from one aws-dynamodb table to another.

The script will look for the default aws credentials in the */.aws/credentials* file, and region on the */.aws/config* file
### Params

-**source table**: Name of the source table in dynamo DB
-**destination table**: Name of the destination table in dynamo DB