
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents: str) -> int:
    counter = 0
    words = file_contents.split()
    for word in words:
        counter+=1
    
    return counter

def sort_on(dict):
    return dict["count"]

def count_chars(file_contents: str) -> dict[str:int]:
    char_counts = {}
    letters = set("abcdefghijklmnopqrstuvwxyz")

    chars = file_contents.lower()

    for char in chars:
        if char in letters:
            if char in char_counts:
                char_counts[char]+=1
            else:
                char_counts[char] = 1
    char_counts = [{"letter":key, "count":value} for key, value in char_counts.items()]

    char_counts.sort(reverse=True, key=sort_on)
    return char_counts

def message(char_count: list[dict]) -> str:
    for count in char_count:
        print(f"The '{count['letter']}' character was found {count['count']} times")
    

if __name__ == "__main__":
    file_contents = main()
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Count of words: {word_count}")
    print("-"*30)
    message(char_count)
    print("--- End of Report ---")

    
    

