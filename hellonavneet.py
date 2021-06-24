def lambda_handler(event, context):
    print("In lambda handler")
    
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Hello Navneet, Welcome to Lambda Demo project"
    }
    
    return resp
