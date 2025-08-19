from stats import get_num_words
from stats import get_num_chars
from stats import num_chars_report
import sys



def get_book_text (filepath):
    with open(filepath) as f:
        return f.read()

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    words = get_num_words(text)
    chars = get_num_chars(text)
    char_list = num_chars_report(chars)  
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in char_list:
        print(f"{entry["char"]}: {entry["count"]}")
    print("============= END ===============")    

main()