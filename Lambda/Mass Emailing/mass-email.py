import csv
import boto3

s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

sender = "your-verified-email@example.com"
subject = "Sample email"

def lambda_handler(event,context):
    bucket = "demo-email-bucket"
    csv_key = "email.csv"
    template_key = "email_template.txt"
    
    csv_file = s3_client.get_object(Bucket=bucket, Key= csv_key)
    csv_content = csv_file['Body'].read().decode('utf-8').splitlines()
    
    template_files = s3_client.get_object(Bucket=bucket, Key= template_key)
    body_template = template_files['Body'].read().decode('utf-8')
    
    reader = csv.DictReader(csv_content)
    
    for row in reader:
        name= row.get('name','name')
        recipient_email = row.get('email' , 'email')
        
        body = body_template.format(name=name)
        ses_client.send_email(
            Destination={'ToAddresses': [recipient_email]},
            Message={
                'Body' : {'Text':{'Charset' : "UTF-8", 'Data': body }},
                'Subject': {'Charset' : "UTF-8", 'Data': subject},
            },
                Source=sender,
            )
    return {"status": "emails sent sucessfully"}
    
