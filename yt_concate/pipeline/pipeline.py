from .steps.step import StepException


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils, logger):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils, logger)
            except StepException as e:
                logger.warning('Exception occurred: ', e)
                break
