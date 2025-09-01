from stats import get_num_words
from stats import char_counter
from stats import sort_on
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		filepath = sys.argv[1]
	
	book_contents = get_book_text(filepath)
	word_count = get_num_words(book_contents)
	chars = char_counter(book_contents)
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for item in chars:
    		ch = item["char"]
    		if ch.isalpha():
        		print(f"{ch}: {item['num']}")
	print("============= END ===============")


main()
