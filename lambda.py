import json

import json

def handler(event, context):
  message = 'Hello {}'.format(event['name'])
  return {
    'statusCode': 200,
    'headers': {
            "Content-Type": "application/json"
    },
    'body': json.dumps({
      "message": message
    })
  }