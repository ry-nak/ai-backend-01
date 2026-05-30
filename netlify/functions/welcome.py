import json

def handler(event, context):
    # Safe check for query parameters (e.g., /?name=Alex)
    query_params = event.get("queryStringParameters") or {}
    name = query_params.get("name", "Guest")
    
    # Construct the response dictionary
    response_body = {
        "message": f"Welcome, {name}! Great to have you here."
    }
    
    # Netlify requires this specific return structure
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # Allows frontend apps to fetch this API safely
        },
        "body": json.dumps(response_body)
    }