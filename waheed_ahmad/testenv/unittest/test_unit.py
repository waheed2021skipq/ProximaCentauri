import pytest
from aws_cdk import core
from aws_cdk import core
from testenv.testenv_stack import waheedsprint33


def test_lambda_stack():
    app = core.App()
    waheedsprint33(app,"waheedteststackk")
    template=app.synth().get_stack_by_name('waheedteststackk').template
    functions=[resource for resource in template['Resources'].values() if resource['Type']== 'AWS::Lambda::Function']
    assert len(functions)>=1
    functions= [resource for resource in template['Resources'].values() if resource['Type']=='AWS::CloudWatch::Alarm']
    assert len(functions)>=1
