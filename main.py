import json
from os import remove
from utils.generateVideo import make_video
from utils.indexer import load_index, save_index
from utils.uploader import upload_video

# Load the JSON file
def load_words(source):
    with open(source, encoding="utf-8") as f:
        return json.load(f)


def main():
    words_file = "arabic-words/Datasets/startWithWords.json"
    index_file = "output/index.txt"

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
            path = make_video(word)
            save_index(index_file, index + 1)
            upload_video(path, word)
            remove(path)
        else:
            print("✅ All words have been processed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
