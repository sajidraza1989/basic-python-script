from gtts import gTTS
from os import system
import os

def text_to_speech(input_file, output_audio):
    """Convert text from a file into audio speech and play it."""
    try:
        # Read the text from the file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():
            print("Error: The input file is empty.")
            return

        # Convert text to speech
        tts = gTTS(text, lang='en')
        tts.save(output_audio)

        print(f"Audio file '{output_audio}' created successfully.")

        # Play the audio file
        if os.name == 'posix':  # For Linux and MacOS
            os.system(f"afplay {output_audio}")  # For MacOS
        else:  # For Windows
            os.startfile(output_audio)  # For Windows
        #system("start output_audio")  # For Windows
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_file = "history.txt"  # Replace with your text file
    output_audio = "output_audio.mp3"  # Output audio file name

    text_to_speech(input_file, output_audio)