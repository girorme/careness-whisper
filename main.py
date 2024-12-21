import argparse
from concurrent.futures import ThreadPoolExecutor
from cwhisper import CWhisper


def transcribe_audio(file, model):
    cwhisper = CWhisper(model)
    result = cwhisper.transcribe(file)
    return result['text']


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Audio Transcription Script")
    parser.add_argument('-f', '--file', type=str,
                        required=True, help="Path to the audio file")
    parser.add_argument('-m', '--model', type=str,
                        default='base', help="Model to use: tiny, base, small, medium, large, turbo")

    args = parser.parse_args()

    print("Working in progress...")
    print(transcribe_audio(args.file, args.model))
