import boto3
import json
import datetime
import os

def lambda_handler(event, context):
    ses_client = boto3.client('ses')
    aws_region = os.environ['AWS_REGION']
    
    try:
        response = ses_client.get_send_quota()
        
        send_quota = response['SentLast24Hours']
        max_send_rate = response['Max24HourSend']
        max_send_quota = response['MaxSendRate']
        
        utilization_percentage = (send_quota / max_send_rate) * 100
        
        if utilization_percentage <= 75:
            sns_client = boto3.client('sns')
            time = str(datetime.datetime.now())
            #send_SNS
            sns_client.publish(
                TopicArn='Your AWS SNS Topic ARN',
                Subject='ALARM:SES Sending Quota Alert',
                Message=f"You are receiving this email because the SES sending quota is {utilization_percentage:.2f}% utilized at {time} in {aws_region} \nView Daily email usage in the AWS Management Console: https://us-east-1.console.aws.amazon.com/ses/home?region={aws_region}"
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Alert sent successfully'})
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Quota utilization below 75%'})
            }
        
    except Exception as e:
        # Handle any errors
        error_message = str(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': error_message})
        }
