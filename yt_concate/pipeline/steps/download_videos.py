import time
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils, logger):
        yt_set = set([found.yt for found in data])  # 過濾掉重複的影片
        logger.info(f'{(len(yt_set))} videos to download.')

        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                logger.info(f'Found video: {url}')
                continue

            logger.info(f'Downloading: {yt.id}.mp4')
            YouTube(url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
        start = time.time()
        end = time.time()
        logger.info(f'It took {(end - start) / 60} minutes to download all videos.')
        return data
