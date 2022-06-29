from .step import Step

from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        video_links = []
        video_ids = []

        for found in data:
            url = found.yt.url
            video_id = found.yt.id
            if utils.video_file_exists(video_id):
                print(f'found video {video_id}.mp4')
                continue
            video_links.append(url)
            video_ids.append(video_id)
            print('Downloading', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=video_id + '.mp4')

        return data
