def lambda_handler(event, context):
    # Your skill's logic goes here
    print("Received event:", event)
    # Example response
    return {
        'statusCode': 200,
        'body': 'Hello from Alexa Skill!'
    }