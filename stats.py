def get_num_words(text):
        words = text.split()
        return len(words)

def sort_on(items):
        return items["num"]


def char_counter(text):
	#convert the text to lowercase
	lower_case = text.lower()

	#create a dictionary to store values
	char_dict = {}

	#iterate through the character in the lowercase text
	for  char in lower_case:
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	
	
	result = []
	for letter, count in char_dict.items():
		item = {"char": letter, "num": count}
		result.append(item)
	
	result.sort(reverse=True, key=sort_on)
	return result
