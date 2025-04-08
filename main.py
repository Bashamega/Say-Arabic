import json
import os
import requests
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip
import arabic_reshaper
from bidi.algorithm import get_display

# Load JSON (you can switch to a URL too)
def load_words(source='words.json'):
    if source.startswith("http"):
        response = requests.get(source)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to load data from URL. Status code: {response.status_code}")
    else:
        with open(source, encoding="utf-8") as f:
            return json.load(f)

# Generate a video from a word
def make_video(word_data, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    word = word_data["word"]
    meaning = word_data.get("meaning", "")

    # Use the word for filenames instead of meaning (avoid special characters)
    safe_word = word.replace(" ", "_").replace("ء", "").replace("ً", "").replace("ٌ", "").replace("ٍ", "")

    # Text-to-speech
    tts = gTTS(text=word, lang='ar')
    audio_path = os.path.join(output_dir, f"{safe_word}_audio.mp3")
    tts.save(audio_path)

    # Reshape and fix Arabic direction
    reshaped_word = arabic_reshaper.reshape(word)
    bidi_word = get_display(reshaped_word)

    reshaped_meaning = arabic_reshaper.reshape(f"المعنى: {meaning}")
    bidi_meaning = get_display(reshaped_meaning)

    final_text = f"{bidi_word}\n{bidi_meaning}"

    # Make sure the font supports Arabic! Try 'Amiri' or 'Arial' if Poppins doesn't.
    clip = TextClip(txt=final_text, fontsize=70, color='white', bg_color='black',
                    size=(720, 1280), font="./fonts/Amiri-Poppins/Amiri/Amiri-Regular.ttf")
    clip = clip.set_duration(3)

    # Add audio
    audio = AudioFileClip(audio_path)
    clip = clip.set_audio(audio)

    # Export video
    video_path = os.path.join(output_dir, f"{safe_word}.mp4")
    clip.write_videofile(video_path, fps=24)

def main():
    try:
        words = load_words()
        for item in words:
            make_video(item)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
