# VITS-TTS-Tamil
Setup configurations:
git clone https://github.com/coqui-ai/TTS.git

Python version required : 3.10 :-
python3.10 -m venv vits_env
source vits_env/bin/activate
Install TTS

metadata.csv format: <file_name>|<speaker_name>|<text>

Convert the dataset .wav audio files into 22050 HZ

Training: python TTS/TTS/bin/train_tts.py --config_path config.json

Inference: python inference_tamil.py

For running on edge devices: convert the best_model.path which gets saved after training your model to a .onnx file which can be directly imported in the backend during app development which can run without any external environment requirement.
