import logging
import time
import os

from threading import Thread
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils, logger):
        logger = logging.getLogger()
        start = time.time()
        yt_set = list(set([found.yt for found in data]))
        logger.info(f'{len(yt_set)} videos to  be downloading')
        yt_list = [yt_set[i:i + (len(yt_set) // os.cpu_count()+1)] for i in range(0, len(yt_set), (len(yt_set) // os.cpu_count()+1))]
        threads = []
        for i in range(os.cpu_count()):
            threads.append(Thread(target=self.multi_download2, args=(yt_list[i], utils)))
            threads[i].start()
        for thread in threads:
            thread.join()
        end = time.time()
        logger.info(f'It took {(end - start)/60} minutes to download the videos.')

        return data

    @staticmethod
    def multi_download2(yt_set, utils):
        logger = logging.getLogger()
        for yt in yt_set:
            if utils.video_file_exists(yt):
                logger.info(f'Found existing video file for {yt.url}, skipped')
                continue
            logger.info(f'Downloading: {yt.url}')
            yt_dl = YouTube(yt.url).streams.get_highest_resolution()
            yt_dl.download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
