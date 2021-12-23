from aws_cdk import core as cdk

from aws_cdk import core
from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines
from resources.pipelinewaheed_stage import ProductionStage

class waheedsprint(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
       

        
        source= pipelines.CodePipelineSource.git_hub(repo_string ='waheed2021skipq/ProximaCentauri',
        branch= 'master',
        authentication =core.SecretValue.secrets_manager('github-oauthwaheedtokeneast'),
        trigger=cpactions.GitHubTrigger.POLL
        )
        
        
        synth= pipelines.ShellStep('synth', input= source,
        commands=[
            "cd /waheed_ahmad/sprint2" , 
            "python -m pip install -r requirements_aws.txt" ,
            "python -m pip install -r requirements.txt"
            ],
            primary_output_directory= "/waheed_ahmad/sprint2/cdk.out")
            
            
            
        pipeline = pipelines.CodePipeline(self, "waheedMyFirstPipeline", synth= synth)
        #this is beta stage of CI/cD    
        # beta= ProductionStage(self,'beta',env={
        #     'account':'315997497220',
        #     'region':'us-east-2'
        # })
        
        #add tests stages here
        
        #  beta= ProductionStage(self,'beta',env={
        #     'account':'315997497220',
        #     'region':'us-east-2'
        # })
        
        #pipeline.add_stage(beta)
