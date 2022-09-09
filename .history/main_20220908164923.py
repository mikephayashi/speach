import librosa

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load('./audio/test.wav')
librosa.output.write_wav('file_trim_5s.wav', y, sr)
print ('Here')