from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from youtube_transcript_api import NoTranscriptFound

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    print('in get video list')  # to debug

    def process(self, data, inputs, utils):
        for url in data:
            print('Downloading caption for', url)
            try:
                srt = YouTubeTranscriptApi.get_transcript(utils.get_video_id_from_url(url), languages=["en", "en-US"])
            except (TranscriptsDisabled, NoTranscriptFound):
                print('Subtitles are not available in these videos: ' + url)
                continue

            with open(utils.get_caption_filepath(url), "w") as f:
                if utils.get_caption_filepath(url):
                    print('Found existing caption file')
                    continue
                for i in srt:
                    f.write("{}\n".format(i))


