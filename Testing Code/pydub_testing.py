from pydub import AudioSegment
from pydub.playback import play



track1 = AudioSegment.from_mp3('AudioSamples/Track1.mp3')
track2 = AudioSegment.from_mp3('AudioSamples/Track2.mp3')
print(track1.dBFS)
print(track2.dBFS)
combined = track1.overlay(track2)
play(combined)


#print(type(track1))