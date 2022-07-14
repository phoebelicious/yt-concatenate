from .step import Step
from yt_concate.model.found import Found


class SearchWord(Step):
    def process(self, data, inputs, utils, logger):
        search_word = inputs['search_word']
        found = []
        for yt in data:
            if yt.captions == 0:
                continue
            for caption in yt.captions:
                if search_word in caption['text']:
                    f = Found(yt, caption)
                    found.append(f)
        logger.info(f'{(len(found))} times of {search_word} were mentioned in the videos.')
        return found
