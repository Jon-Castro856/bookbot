def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    wordcount(file_contents)

def wordcount(words):
    split_string = words.split()
    print(f"Frankenstein has {len(split_string)} words in it.")

main()