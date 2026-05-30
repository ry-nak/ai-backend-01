import json

def handler(event, context):
    query_params = event.get("queryStringParameters") or {}
    name = query_params.get("name", "Guest")
    
    response_body = {
        "message": f"Welcome, {name}! Great to have you here."
    }
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(response_body)
    }