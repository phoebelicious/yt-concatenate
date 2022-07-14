import sys
import getopt
import logging
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYt
from yt_concate.pipeline.steps.search_word import SearchWord
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_videos import EditVideos
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils

CHANNEL_ID = 'UCoOss5XiPpnLHGmLrBvNkJg'


def print_usage():
    print('python main.py OPTIONS')
    print('OPTIONS:')
    print('{:>6} {:<15} {}'.format('-c', '--channel_id', 'The channel ID of your target Youtube channel'))
    print('{:>6} {:<15} {}'.format('-s', '--search_word', 'The word that you would like to capture in the videos'))
    print('{:>6} {:<15} {}'.format('-l', '--limits', 'The maximum number of capture clips in the output video'))
    print('{:>6} {:<15} {}'.format('-g', '--logging_level', 'The logging level shown on the CMD screen. '
                                                            '[Fill a number only] '
                                                            '[1:DEBUG, 2:INFO, 3:WARNING, 4:ERROR, 5:CRITICAL]'))
    print('{:<24} {}'.format('', '--cleanup', 'Removing all of the downloaded videos'))
    print('{:<24} {}'.format('', '--fast', 'Skipping downloading video list and videos if exist'))


def command_line_arg():
    channel_id = CHANNEL_ID
    search_word = 'fashion'
    limits = 80
    logging_level = logging.DEBUG
    cleanup = False
    fast = False
    short_opt = 'hc:s:l:g:'
    long_opt = 'help channel_id= search_word= limits= logging_level= cleanup fast'.split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opt, long_opt)
        print(opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(0)
        elif opt in ("-c", "--channel_id"):
            channel_id = arg
        elif opt in ("-s", "--search_word"):
            search_word = arg
        elif opt in ("-l", "--limits"):
            limits = int(arg)
        elif opt in ("-g", "--logging_level"):
            if arg == '1':
                logging_level = logging.DEBUG
            elif arg == '2':
                logging_level = logging.INFO
            elif arg == '3':
                logging_level = logging.WARNING
            elif arg == '4':
                logging_level = logging.ERROR
            elif arg == '5':
                logging_level = logging.CRITICAL
        elif opt == '--cleanup':
            cleanup = True
        elif opt == '--fast':
            fast = True
    return channel_id, search_word, limits, logging_level, cleanup, fast


def config_logger(logging_level):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
    file_handler = logging.FileHandler('yt_concate_logging.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def main():
    channel_id, search_word, limits, logging_level, cleanup, fast = command_line_arg()
    inputs = {
        'channel_id': channel_id,
        'search_word': search_word,
        'limits': limits,
        'logging_level': logging_level,
        'cleanup': cleanup,
        'fast': fast,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYt(),
        SearchWord(),
        DownloadVideos(),
        EditVideos(),
        Postflight(),
    ]

    logger = config_logger(logging_level)
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils, logger)


if __name__ == '__main__':
    main()
