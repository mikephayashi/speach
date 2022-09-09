import librosa
import soundfile as sf

# THRESHOLD = 0.005
THRESHOLD = 5
# BUFFER = 0.1
FILE_NAME = "word.wav"

def calc_length(arr, sr):
    return len(arr) / sr

# def is_within_sound(sounds):
#     if len(sounds) == 0:
#         return True
#     if sum(abs(sounds)) / len(sounds) > THRESHOLD:
#         return True
#     return False

y, sr = librosa.load(f'./audio/input/{FILE_NAME}')

tenth = int(sr * 0.05)

new_y = []
total = len(y)
running_sum = 0
running_list = []
for idx, x in enumerate(y):
    abs_x=abs(x)
    if idx < tenth:
        running_sum += abs_x
        running_list.append(abs_x)
    else:
        running_sum -= running_list[0]
        running_sum += abs_x
        running_list.pop(0)
        running_list.append(abs_x)
        if running_sum > THRESHOLD:
            new_y.append(x)
    
    
    print(f'{idx}/{total}')

# new_y = [x for x in y if x > THRESHOLD or x < -THRESHOLD]
sf.write('./audio/output/test.wav', new_y, sr)
print("Original Length: ", calc_length(y, sr))
print("New Length: ", calc_length(new_y, sr))