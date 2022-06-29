from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYt
from yt_concate.pipeline.steps.search_word import SearchWord
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils


CHANNEL_ID = 'UCoOss5XiPpnLHGmLrBvNkJg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'fashion',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYt(),
        SearchWord(),
        Postflight(),
        ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
