import librosa
import soundfile as sf

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load('./audio/test.wav')
# librosa.output.write_wav('./output/test.wav', y, sr)
sf.write('stereo_file1.wav', reduced_noise, 48000, 'PCM_24')