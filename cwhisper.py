import whisper
import warnings

warnings.simplefilter('ignore')


class CWhisper:
    def __init__(self):
        self.model = whisper.load_model("turbo")
        pass

    def transcribe(self, audio_path):
        return self.model.transcribe(audio_path)
