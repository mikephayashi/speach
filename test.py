import librosa
y, sr = librosa.load('./audio/input/oneword.wav')
f = open('./amp.txt', 'w')
for x in y:
    f.write(f'{x}\n')
    print(x)