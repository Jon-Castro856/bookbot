def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    wordcount(file_contents)
    lettercounter(file_contents)

def wordcount(words):
    split_string = words.split()
    print(f"Frankenstein has {len(split_string)} words in it.")

def lettercounter(file_contents):
    lower_case = file_contents.lower()
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
                "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
                "k": 0, "l": 0 , "m": 0, "n": 0, "o": 0, 
                "p":0, "q": 0, "r": 0, "s": 0, "t": 0, 
                "u": 0,"v": 0, "w": 0, "x": 0, "y": 0, 
                "z": 0, " ": 0, "'": 0, ".": 0, "!": 0,
                "?":0, '"': 0,} 
    for char in alphabet:
        counter = 0
        for s in lower_case:
            if s == char:
                counter += 1
        alphabet[char] = counter
    print(alphabet)
main()