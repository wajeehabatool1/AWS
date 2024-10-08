# Mass Emailing System using lambda, s3, ses and eventbridge
## Services Covered
- Lambda
- S3
- SES
- Eventbridge

## Overview
This project automates the process of sending bulk emails using AWS Lambda, Amazon SES (Simple Email Service), and S3. The Lambda function retrieves recipient information from a CSV file stored in an S3 bucket, reads an email template also from S3, and sends personalized emails to each recipient using SES. The system can be triggered manually or scheduled via Amazon EventBridge to send emails at a specific time.

Now, lets start with the implementation

## S3
- create s3 bucket
- upload .csv file for recipient information (name and email) and .txt file for email template
- 
