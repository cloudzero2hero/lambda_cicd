import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from updated CICD github actions workflow vscode with new credentials')
    }