from .step import Step
from .step import StepException


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in postflight')
