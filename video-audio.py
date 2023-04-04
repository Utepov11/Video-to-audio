import moviepy.editor
from pathlib import Path

file_video = Path('...') #In Path write your video file .mp4

video = moviepy.editor.VideoFileClip(f'{file_video}')
file_audio = video.audio
file_audio.write_audiofile(f'{file_video.stem}.mp3')