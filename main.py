import json
import requests
from utils.generateVideo import make_video

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



def main():
    try:
        words = load_words()
        for item in words:
            make_video(item)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
