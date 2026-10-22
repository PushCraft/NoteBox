"""AWS Lambda entry point placeholder.

Implement in Phase 2 after writing and testing the local message model.
Do not deploy this as a production handler.
"""


def lambda_handler(event, context):
    return {
        "statusCode": 501,
        "headers": {"content-type": "application/json"},
        "body": '{"error":"Not implemented yet"}',
    }
