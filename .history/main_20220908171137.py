import librosa
import soundfile as sf

THRESHOLD = 0.0001

def calc_length(arr, sr):
    return len(arr) / sr

y, sr = librosa.load('./audio/test.wav')
new_y = [x for x in y if x > THRESHOLDor ]
sf.write('./output/test.wav', new_y, sr)
print("Original Length: ", calc_length(y, sr))
print("New Length: ", calc_length(new_y, sr))