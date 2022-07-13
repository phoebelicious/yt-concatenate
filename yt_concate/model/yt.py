from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from youtube_transcript_api import NoTranscriptFound


class YT:
    def __init__(self, url, logger):
        self.url = url
        self.logger = logger
        self.id = self.get_video_id_from_url()
        self.captions = self.get_video_captions()

    def get_video_id_from_url(self):
        return self.url.split('watch?v=')[-1]

    def get_video_captions(self):
        try:
            return YouTubeTranscriptApi.get_transcript(self.id, languages=["en", "en-US"])

        except (TranscriptsDisabled, NoTranscriptFound):
            self.logger.warning(f'English subtitles are not available in the video {self.url}')
            return 0
