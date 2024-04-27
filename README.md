# Clipboard-to-TTS

### Description:
Clipboard-to-TTS is a Python script designed to streamline the process of converting text content from the clipboard into speech using OpenAI's Text-to-Speech (TTS) API. This script offers a convenient way to quickly transform copied text into spoken audio, providing accessibility and efficiency for various applications.

### Setting Up:
I recommend using a virtual environment for managing dependencies (virtualenv) to isolate this project's environment from other Python projects.
```commandline
git clone https://github.com/tibssy/Clipboard-to-TTS.git
cd Clipboard-to-TTS
pip install -r requirements.txt
```

### Configuration:

Create a .env file in the root directory of the repository.
Add your OpenAI API key to the .env file:

```commandline
OPENAI_API_KEY="your_api_key_here"

```

### Running the Script:
```commandline
python clipboard_to_tts.py
```

Alternatively, you can create a single-file executable with PyInstaller for easier distribution and execution.

### Note:
Please ensure that mpg123 is installed on your system, as it is required for playing back the generated speech audio. You can install mpg123 using your package manager or by visiting the official website: https://www.mpg123.de/.
