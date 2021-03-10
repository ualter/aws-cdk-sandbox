cdk init sample-app --language python

# Activate Python Virtual Environment
source .env/bin/activate
# Windows (if needed)
.env\Scripts\activate.bat
# Exit
deactivate

pip install -r requirements.txt

pip install aws-cdk.aws-lambda
pip install aws-cdk.aws_apigateway
pip install aws-cdk.aws_dynamodb


# Installing Libraries
pip install cdk-dynamo-table-viewer