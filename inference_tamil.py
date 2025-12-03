from TTS.utils.synthesizer import Synthesizer

TEXT = "வணக்கம், நான் ரித்விக்."

MODEL_PATH = "outputs/tamil_vits/tamil_vits-November-26-2025_8+50PM-0000000/best_model_7348.pth"
CONFIG_PATH = "outputs/tamil_vits/tamil_vits-November-26-2025_8+50PM-0000000/config.json"

OUT_PATH = "output_tamil.wav" 

def run():
    synth = Synthesizer(
        tts_checkpoint=MODEL_PATH,
        tts_config_path=CONFIG_PATH,
        tts_speakers_file=None,
        tts_languages_file=None,
        vocoder_checkpoint=None,
        vocoder_config=None,
        encoder_checkpoint=None,
        encoder_config=None,
        use_cuda=False,
    )

    wav = synth.tts(TEXT)
    synth.save_wav(wav, OUT_PATH)

    print(f" Saved: {OUT_PATH}")

if __name__ == "__main__":
    run()
