import time
import concurrent.futures
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils, logger):

        video_links = []
        video_ids = []

        for found in data:
            url = found.yt.url
            video_id = found.yt.id
            fast = inputs['fast']
            if utils.video_file_exists(video_id) and fast:
                logger.info(f'found video {video_id}.mp4')
                continue
            video_links.append(url)
            video_ids.append(video_id)
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for video in executor.map(self.download, video_links, video_ids):
                logger.info(f'downloading: video')
        end = time.time()
        logger.info(f'It took {(end - start) / 60} minutes to download all the videos.')
        return data

    @staticmethod
    def download(url, video_id):
        return YouTube(url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR, filename=video_id + '.mp4')
