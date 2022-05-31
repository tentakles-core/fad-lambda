import boto3
import json

def lambda_handler(event, context):

    runtime = boto3.Session().client('sagemaker-runtime')
    
    payload = json.dumps(event)
    
    response = runtime.invoke_endpoint(EndpointName = 'test-1',    
                                       ContentType = 'application/json',               
                                       Body = payload)                     

    result = response['Body'].read().decode('utf-8')
    
    if result == '1':
        res = True
    else:
        res = False
    
    return {
        "result": res
    }
