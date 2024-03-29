from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeLine
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeLine

STAGE_NAME = "Data ingestion stage"


try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="prepare base model"

try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME ="TRAINING"

try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=ModelTrainingPipeLine()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME ="model evaluation"

try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=EvaluationPipeLine()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
except Exception as e:
        logger.exception(e)
        raise e

