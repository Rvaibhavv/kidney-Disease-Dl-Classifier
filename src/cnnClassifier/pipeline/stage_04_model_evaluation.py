from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation 
from cnnClassifier import logger
import os
STAGE_NAME ="model evaluation"


class EvaluationPipeLine:
    def __init__(self):
        pass

    def main(self):
    #    os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Rvaibhavv/kidney-Disease-Dl-Classifier.mlflow"
    #    os.environ["MLFLOW_TRACKING_USERNAME"]="Rvaibhavv"
    #    os.environ["MLFLOW_TRACKING_PASSWORD"]="a37ad20e3c8a402cd86cae1238ec2ef1bed9ba0d"
       config = ConfigurationManager()
       eval_config =config.get_evaluation_config()
       evaluation= Evaluation(eval_config)
       evaluation.evaluation()
       evaluation.save_score()
       evaluation.log_into_mlflow()
       


if __name__ =="__main__":
    try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=EvaluationPipeLine
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
    except Exception as e:
        logger.exception(e)
        raise e

