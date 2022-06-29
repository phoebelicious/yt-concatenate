import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import DOWNLOADS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        filepath = self.get_video_list_filepath(channel_id)
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    @staticmethod
    def get_video_filepath(video_id):
        return os.path.join(VIDEOS_DIR, video_id + '.mp4')

    def video_file_exists(self, video_id):
        filepath = self.get_video_filepath(video_id)
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0
