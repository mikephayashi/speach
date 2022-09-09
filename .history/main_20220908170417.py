import librosa
import soundfile as sf

THRESHOLD = 0.1

def calc_length()

y, sr = librosa.load('./audio/test.wav')
new_y = [x for x in y if x > THRESHOLD]
sf.write('./output/test.wav', new_y, sr)
print("Original Length: ", )
print("New Length: ", new_y)