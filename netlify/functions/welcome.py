import json


def handler(event, context):
    # Get the name from the URL query parameters (e.g., ?name=Alex)
    query_params = event.get("queryStringParameters", {})
    name = query_params.get("name", "Guest")

    # Build the welcome message
    message = f"Welcome, {name}! Great to have you here."

    # Netlify functions must return a status code and a body
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": message}),
    }