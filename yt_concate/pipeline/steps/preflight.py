from .step import Step
from .step import StepException


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in preflight')
        utils.create_dirs()
