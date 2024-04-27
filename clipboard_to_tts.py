import clipboard
import os
import sys
from datetime import datetime
import shutil
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError, Timeout, APIError


PATH = os.path.dirname(os.path.realpath(sys.argv[0]))


def read_last_text() -> str:
    with open(os.path.join(PATH, 'speech.txt'), "r") as f:
        return f.read().strip()


def write_text(text: str) -> None:
    with open(os.path.join(PATH, 'speech.txt'), "w") as f:
        f.write(text)


def text_to_speech(text: str) -> None:
    load_dotenv(os.path.join(PATH, '.env'))
    if (api_key := os.getenv('OPENAI_API_KEY')) is None:
        print("OpenAI API key not found.")
        play_mp3('ApiKeynotfound.mp3')
        return

    client = OpenAI(api_key=api_key)
    try:
        with client.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice="alloy",
                input=text,
        ) as response:
            response.stream_to_file(os.path.join(PATH, 'speech.mp3'))

    except APIConnectionError as e:
        print(f"OpenAI API request failed to connect: {e}")
        play_mp3('APIConnectionError.mp3')
    except APIError as e:
        print(f"OpenAI API returned an API Error: {e}")
        play_mp3('APIError.mp3')
    except AuthenticationError as e:
        print(f"OpenAI API request was not authorized: {e}")
        play_mp3('AuthenticationError.mp3')
    except Timeout as e:
        print(f"OpenAI API request timed out: {e}")
        play_mp3('Timeout.mp3')
    else:
        play_mp3()


def play_mp3(audio_file: str = 'speech.mp3') -> None:
    os.system(f'mpg123 -q {os.path.join(PATH, audio_file)}')


def copy_with_timestamp() -> None:
    src_file = os.path.join(PATH, 'speech.mp3')
    dest_folder = os.path.expanduser("~/Desktop/saved_speech")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(dest_folder, exist_ok=True)
    shutil.copy(src_file, os.path.join(dest_folder, f'speech_{timestamp}.mp3'))


def main() -> None:
    if (clipboard_text := clipboard.paste().strip()) == read_last_text():
        play_mp3()
    elif clipboard_text:
        write_text(clipboard_text)
        text_to_speech(clipboard_text)
        copy_with_timestamp()


if __name__ == '__main__':
    main()
