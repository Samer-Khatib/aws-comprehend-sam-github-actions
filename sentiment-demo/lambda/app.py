import json, boto3

comprehend = boto3.client("comprehend")

def lambda_handler(event, context):
    text = event["body"]
    result = comprehend.detect_sentiment(Text=text, LanguageCode="en")
    sentiment = result["Sentiment"]
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"Sentiment": sentiment})
    }
