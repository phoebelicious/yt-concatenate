from .step import Step
from yt_concate.model.yt import YT


class InitializeYt(Step):
    def process(self, data, inputs, utils, logger):
        return [YT(url, logger) for url in data]
