import argparse
from concurrent.futures import ThreadPoolExecutor
from cwhisper import CWhisper


def transcribe_audio(file):
    cwhisper = CWhisper()
    result = cwhisper.transcribe(file)
    return result['text']


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Audio Transcription Script")
    parser.add_argument('-f', '--file', type=str,
                        required=True, help="Path to the audio file")

    args = parser.parse_args()

    # Process transcription in parallel (expandable for multiple tasks)
    with ThreadPoolExecutor() as executor:
        future = executor.submit(transcribe_audio, args.file)
        print("Working in progress...")

        # Get the transcription result
        result_text = future.result()
        print(result_text)
