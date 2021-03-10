import json
import pytest

from aws_cdk import core
from python.python_stack import PythonStack


def get_template():
    app = core.App()
    PythonStack(app, "python")
    return json.dumps(app.synth().get_stack("python").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
