from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from .step import Step


class EditVideos(Step):
    def process(self, data, inputs, utils, logger):
        videos = []
        for found in data:
            video_id = found.yt.id
            filepath = utils.get_video_filepath(video_id)
            start_time = found.start_time
            end_time = found.end_time
            video = VideoFileClip(filepath).subclip(start_time, end_time)
            videos.append(video)
            if len(videos) >= inputs['limits']:
                break

        final_video = concatenate_videoclips(videos)
        output_filepath = utils.get_output_video_filepath(inputs['channel_id'], inputs['search_word'])
        final_video.write_videofile(output_filepath, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")

        # closing VideoFileClips
        for video in videos:
            video.close()
        return data
