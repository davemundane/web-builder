import json
import boto3

def lambda_handler(event, context):

    inboundName = event["name"]
    inboundEmail = event["email"]
    formSubject = event["subject"]
    formMessage = event["message"]
    
    emailString = "Message From: " + inboundEmail + "\r\n"
    emailString += "Name: " + inboundName + "\r\n"
    emailString += "Subject: " + formSubject + "\r\n"
    emailString += "Message: " + formMessage 
    
    client = boto3.client('sns', region_name='us-east-1')
    client.publish(
        TopicArn="arn:aws:sns:us-east-1:943161404748:LamdbaHandler", 
        Message=emailString)
    
    return {
        'statusCode': 200,
        'body': "Thanks for your email"
    }
