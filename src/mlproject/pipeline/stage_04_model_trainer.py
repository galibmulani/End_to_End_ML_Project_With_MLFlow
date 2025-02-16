from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_trainer import ModelTrainer
from src.mlproject import logger


STAGE_NAME="Model Trainer stage"


class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            model_trainer_config=config.get_model_trainer_config()
            model_trainer=ModelTrainer(config=model_trainer_config)
            model_trainer.train()
 
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e