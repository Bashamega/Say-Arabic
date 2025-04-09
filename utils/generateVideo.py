import os
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip
import arabic_reshaper
from bidi.algorithm import get_display
# Generate a video from a word
def make_video(word, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    # Use the word for filenames instead of meaning (avoid special characters)
    safe_word = word.replace(" ", "_").replace("ء", "").replace("ً", "").replace("ٌ", "").replace("ٍ", "")

    # Text-to-speech
    tts = gTTS(text=word, lang='ar')
    audio_path = os.path.join(output_dir, f"{safe_word}_audio.mp3")
    tts.save(audio_path)

    # Reshape and fix Arabic direction
    reshaped_word = arabic_reshaper.reshape(word)
    bidi_word = get_display(reshaped_word)

    # Make sure the font supports Arabic! Try 'Amiri' or 'Arial' if Poppins doesn't.
    clip = TextClip(txt=bidi_word, fontsize=70, color='white', bg_color='black',
                    size=(720, 1280), font="./fonts/Amiri/Amiri-Bold.ttf")
    clip = clip.set_duration(3)

    # Add audio
    audio = AudioFileClip(audio_path)
    clip = clip.set_audio(audio)

    # Export video
    video_path = os.path.join(output_dir, f"{safe_word}.mp4")
    clip.write_videofile(video_path, fps=24)