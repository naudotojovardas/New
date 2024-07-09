# Design a MediaPlayer class structure that uses polymorphism to play different types of media files.
# Implement subclasses for AudioPlayer and VideoPlayer, each overriding a common method to play their specific type of media.
            # Requirements
# Abstract method play in the MediaPlayer base class.
# Each subclass should have its own implementation of the play method that reflects the specific media type it handles.


class MediaPlayer:
    def play(self):
        pass

class AudioPlayer(MediaPlayer):
    def play(self):
        print('Playing audio file')

class VideoPlayer(MediaPlayer):
    def play(self):
        print('Playing video file')

audio_player = AudioPlayer()
audio_player.play()

video_player = VideoPlayer()
video_player.play()

