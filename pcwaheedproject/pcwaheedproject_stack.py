from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_iam,
    aws_cloudwatch as cloudwatch_,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as actions_,
    aws_dynamodb as db
)


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
#
from aws_cdk import core


class PcwaheedprojectStack(cdk.Stack):

    
    
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role= self.create_lambda_role()
        hw_lambda = self.create_lambda('lambda', './resources', 'webhealthmonitor.lambda_handler', lambda_role)
        #2 db_lambda = self.create_lambda("DynamoDBLambda", "./resources", dynamodb_lambda.lambda_handler, lambda_role)
        lambda_schedule= events_.Schedule.rate(cdk.Duration.minutes(1))
        lambda_target=targets_.LambdaFunction(handler=hw_lambda)
        rule= events_.Rule(self, "webHealth_invoke", 
                            description= "call lambda periodic", 
                            enabled= True ,
                            schedule= lambda_schedule,
                            targets= [lambda_target]) #remeber the braces, i spent so much time to figure out this error, cz this is treateda as array
        #2 create table here 
        #2dynamo_table=self.create_table()
        #####also provide full read write access to table
        
        #####module code for sending sns notifications########################################################
        #1topic = sns.Topic(self, "webhealth")
        #1topic.add_subscription(subscriptions_.EmailSubscription('waheed.ahmad.s@skipq.org'))
        #2topic.add_subscription(subscription_.LambdaSubscription(fn=db_lambda))
        
        
        dimension={'URL' : constants.URL_TO_MONITOR}
        availability_metric=cloudwatch_.Metric(namespace=constants.URL_MONITOR_NAMESPACE, 
                                                metric_name= constants.URL_MONIROR_NAME_AVAILABILITY,
                                                dimensions_map=dimension,
                                                period=cdk.Duration.minutes(1),
                                                label= 'Availability Metric')
        availability_alarm= cloudwatch_.Alarm(self, 
			id='AvailabilityAlarm',
			metric= availability_metric , 
			comparsion_operator= cloudwatch_.ComparisonOperation.LESS_THAN_OPERATOR  , 
			datapoint_to_alarm=1, evaluation_periods=1,
		 	threshold=1) 
    
        dimension={'URL':constants.URL_TO_MONITOR}
        latency_metric=cloudwatch_.Metric(namespace=constants.URL_MONITOR_NAMESPACE, 
                                         metric_name= constants.URL_MONIROR_NAME_LATENCY,
                                         dimensions_map=dimension,
                                         period=cdk.Duration.minutes(1),
                                         label= 'latency Metric' )
        latency_alarm= cloudwatch_.Alarm(self, 
			id='LatencyAlarm',
			metric= latency_metric , 
			comparsion_operator= cloudwatch_.ComparisonOperation.GREATER_THAN_THRESHOLD  , 
			datapoint_to_alarm=1, evaluation_periods=1,
		 	threshold=0.26 )
    
    ###########link the alarm to subscription
    #1availability_alarm.add_alarm_action(actions_.sns_action(topic))
    #1latency_alarm.add_alarm_action(actions_.sns_action(topic))
    
    
    def create_lambda_role(self):
        lambdaRole = aws_iam.Role(self, "lambda-role", 
                    assumed_by= aws_iam.ServicePrincipal('lambda.amazonaws.com'),
                    managed_policies=[
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'),
                            aws_iam.ManagedPolicy.from_aws_managed_policy_name('CloudwatchFullAccess')
            ]
            )
        return lambdaRole
    def create_lambda(self, id, asset,handler, role):
        return lambda_.Function(self, id,
        runtime=lambda_.Runtime.PYTHON_3_6 ,
        handler=handler,
        code=lambda_.Code.from_asset(asset),
        role=role
)

    #2def create_table():
     #2   return db.Table