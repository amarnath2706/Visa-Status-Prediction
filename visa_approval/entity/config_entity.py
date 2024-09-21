import os
from visa_approval.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

"""Decorator for data class - without self keyword iam writing the variables
in our our normal class we define something like class abc:
def __init__(self):
self.test = "None"
"""

#With the help of data class decorator we can define the class variables without using any kind of self method

@dataclass
class TrainingPipelineConfig:
    #pipeline from constant 
    pipeline_name: str = PIPELINE_NAME
    #artifact from constant 
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    #it create the time stamp folder inside that it will ingest the data, so that i dont need to replace the data again and again, 
    #Because i need all of the artifacts generated by the components of the pipeline
    timestamp: str = TIMESTAMP

# variable------type---------class name
training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

