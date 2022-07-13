from .step import Step
from .step import StepException


class Preflight(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('In Preflight')
        utils.create_dirs()
