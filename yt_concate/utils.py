import os
import shutil

from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import OUTPUT_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        filepath = self.get_video_list_filepath(channel_id)
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    @staticmethod
    def get_video_filepath(video_id):
        return os.path.join(VIDEOS_DIR, video_id + '.mp4')

    @staticmethod
    def video_file_exists(yt):
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    @staticmethod
    def get_output_video_filepath(channel_id, search_word):
        filename = channel_id + '_' + search_word + '.mp4'
        return os.path.join(OUTPUT_DIR, filename)

    @staticmethod
    def remove_dirs():
        shutil.rmtree(VIDEOS_DIR, ignore_errors=True)
