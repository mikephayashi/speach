import librosa
import soundfile as sf

y, sr = librosa.load('./audio/test.wav')
sf.write('./output/test.wav', y, sr)