#!/usr/bin/env python3

from aws_cdk import core

from python.python_stack import PythonStack


app = core.App()
PythonStack(app, "CDKPython", env={'region': 'us-east-1'})

app.synth()
