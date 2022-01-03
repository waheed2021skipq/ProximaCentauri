import pytest
from aws_cdk import core
from aws_cdk import core
from testenv.testenv_stack import waheedsprint3
app = core.App()
waheedsprint3(app,"waheedteststackk")
template=app.synth().get_stack_by_name('waheedteststackk').template

def test_lambda_stack():
    functions=[resource for resource in template['Resources'].values() if resource['Type']== 'AWS::Lambda::Function']
    assert len(functions)== 2
def test_alarms():
    functions= [resource for resource in template['Resources'].values() if resource['Type']=='AWS::CloudWatch::Alarm']
    assert len(functions)>=2
def test_bucket():
    buckets= [resource for resource in template['Resources'].values() if resource['Type']=='AWS::S3::Bucket']
    assert len(buckets)==1

