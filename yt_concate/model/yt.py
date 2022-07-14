import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from youtube_transcript_api import NoTranscriptFound
from yt_concate.settings import VIDEOS_DIR


class YT:
    def __init__(self, url, logger):
        self.url = url
        self.logger = logger
        self.id = self.get_video_id_from_url(self.url)
        self.video_filepath = self.get_video_filepath()
        self.captions = self.get_video_captions()

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_video_captions(self):
        try:
            return YouTubeTranscriptApi.get_transcript(self.id, languages=["en", "en-US"])

        except (TranscriptsDisabled, NoTranscriptFound):
            self.logger.warning(f'English subtitles are not available in the video {self.url}')
            return 0

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):
        return '<YT(' + self.id + ')>'

    def __repr__(self):
        content = ' : '.join([
            'id=' + str(self.id),
            'video_filepath=' + str(self.video_filepath)
        ])
        return '<YT(' + content + ')>'
