import os
import torchaudio

in_dir = "datasets/wavs"
out_dir = "datasets/wavs_22050"
os.makedirs(out_dir, exist_ok=True)

for file in os.listdir(in_dir):
    if file.endswith(".wav"):
        wav, sr = torchaudio.load(os.path.join(in_dir, file))
        wav_22k = torchaudio.functional.resample(wav, sr, 22050)
        torchaudio.save(os.path.join(out_dir, file), wav_22k, 22050)

print("Resampling done!")
