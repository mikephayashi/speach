import librosa
import soundfile as sf

THRESHOLD = 0.1

y, sr = librosa.load('./audio/test.wav')
new_y = 
sf.write('./output/test.wav', y, sr)