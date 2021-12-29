#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from aws_cdk import core
from sprint3.pipelinewaheed_stack import waheedsprint
#from pcwaheedproject.pcwaheedproject_stack import PcwaheedprojectStack



app = core.App()
waheedsprint(app, "waheedsprint",
            env=core.Environment(account='315997497220', 
                                region='us-east-2'))

app.synth()
