#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(dict):
    
    screat={"COUCH_URL": "https://e03960c7-5bd1-47b3-aa1a-eed32cbb0cc7-bluemix.cloudantnosqldb.appdomain.cloud",
            "IAM_API_KEY": "DfzOwkwtYdDS38XjyotiB9c12ezmP7zY9Idjh16U90E9",
            "COUCH_USERNAME": "e03960c7-5bd1-47b3-aa1a-eed32cbb0cc7-bluemix"}
    try:
        client = Cloudant.iam(
            account_name=screat["COUCH_USERNAME"],
            api_key=screat["IAM_API_KEY"],
            connect=True,
        )
        database= client["reviews"]
        document=database.create_document(dict)
        if document.exists():
            result= {
            'headers':{'Content-Type':'application/json'},
            'body':{'message':"DataInserted"}
            }
            return result
    except:
        return {
            'statusCode': 500,
            'message': "Something went wrong on the server"
            }
