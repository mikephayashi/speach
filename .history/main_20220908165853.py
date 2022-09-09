import librosa
import soundfile as sf

y, sr = librosa.load('./audio/test.wav')
# librosa.output.write_wav('./output/test.wav', y, sr)
sf.write('./output/test.wav', y, sr)