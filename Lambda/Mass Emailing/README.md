# Mass Emailing System using lambda, S3, SES and Cloudwatch
## Services Covered
- Lambda
- S3
- SES
- Cloudwatch

## Overview
This project automates the process of sending bulk emails using AWS Lambda, Amazon SES (Simple Email Service), and S3. The Lambda function retrieves recipient information from a CSV file stored in an S3 bucket, reads an email template also from S3, and sends personalized emails to each recipient using SES. The system can be triggered manually or scheduled via Amazon EventBridge to send emails at a specific time.

Now, lets start with the implementation

## S3
- create s3 bucket
- enable bucket versioning if want to add different versions of csv and template files
- Block public access to bucket as a good security practice
- upload .csv file for recipient information (name and email) and .txt file for email template
  

## Lambda 
- Create a new function with python runtime
- **choose an existing role**  with the desired permission or go with **create a new role with basic lambda permission** and assign it the required permission later
- Use the code provided in the **mass-email.py** file for writing lambda function
- now,  you have to provide permissions to IAMROLE of lambda function to access specific AWS services in order to execute lambda function successfully
### IAMROLE Permission Policiy
You can attach permission policies to *IAMROLE in two ways*. One is AWS provided policies or you can make *inline policy using the least privillage appraoch. Inline policy is a recommended option*

#### AWS provided Policy
you need to provide :
- AmazonCloudWatchEvidentlyFullAccess
- AmazonS3FullAccess
- AmazonSESFullAccess

  
**OR**

#### Inline Permission Policy
you need to provide:
- *S3 Inline permissions :* GetObject
- *SES Inline permissions:* SendEmail
- *Cloudwatch Logs permissions:* CreateLogGroup && CreateLogStream && PutLogEvents

## SES
- You need to verify your email through which you are sending the emails
- Add your email for verification , SES will send a notification to your email address , click on that to verify your email


**Note:**
  If your using SES sandbox enviroment , then you have verify all the emails present in your csv file , otherwise the SES will not validate the recipient emails

## Cloud Watch && Event Bridge
- go to cloud watch
- go to event, click on Rules, creating rules will open under the service of event bridge.
- create rule , select rule type to **Schedule**
- Set the date, time and time zone
- Select target API , in this case our target API is AWS lambda Invoke
-  Select the lambda function you want to invoke
-  Decide you want to create a new Role for eventbridge or use an existing one and then create schedule
-  now , the lambda function will be triggered on the specified day and time
-  Logs will be saved in the cloudwatch under the lambda function you have created for this purpose 


Thats how you can automate the process of sending emails in bulk using different templates or different csv files.
