import moviepy 
import editor
video=editor.VideoFileClip('yahissen.mp4')
video.audio.write_audiofile('yahissen.mp3')