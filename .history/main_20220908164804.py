import librosa

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load('./audio/test.wav')
print ('Here')