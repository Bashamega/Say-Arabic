import json
import os
from utils.generateVideo import make_video

# Load the JSON file
def load_words(source):
    with open(source, encoding="utf-8") as f:
        return json.load(f)

# Load index or default to 0
def load_index(index_file):
    if os.path.exists(index_file):
        with open(index_file, "r") as f:
            return int(f.read().strip())
    return 0

# Save the updated index
def save_index(index_file, index):
    with open(index_file, "w") as f:
        f.write(str(index))

def main():
    words_file = "arabic-words/Datasets/startWithWords.json"
    index_file = "index.txt"

    try:
        words = load_words(words_file)
        # Flatten the structure to a list of words
        all_words = []
        for outer_key, inner_dict in words.items():
            if isinstance(inner_dict, dict):
                for inner_key, word_list in inner_dict.items():
                    if isinstance(word_list, list):
                        for word in word_list:
                            all_words.append(word)

        index = load_index(index_file)

        if index < len(all_words):
            word = all_words[index]
            print(f"Processing word #{index}: {word}")
            make_video(word)
            save_index(index_file, index + 1)
        else:
            print("✅ All words have been processed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
