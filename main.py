import os
import argparse

def find_replace(folder, find_word, replace_word):
    """Recursively finds and replaces words in all files within a folder."""
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                new_content = content.replace(find_word, replace_word)
                if content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Replaced in: {file_path}")
            except Exception as e:
                print(f"Skipping {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Find and replace words in all files within a folder.")
    parser.add_argument("folder", help="Path to the folder containing files.")
    parser.add_argument("find_word", help="Word to find.")
    parser.add_argument("replace_word", help="Word to replace with.")
    args = parser.parse_args()
    
    find_replace(args.folder, args.find_word, args.replace_word)

if __name__ == "__main__":
    main()
