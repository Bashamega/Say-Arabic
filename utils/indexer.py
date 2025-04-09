import os
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