# search a mapping function

def main():
    def word_lengths(my_string):
        my_string = my_string.replace(".", "")
        my_string = my_string.replace(",","")
        my_string = my_string.replace("?","")
        my_string = my_string.replace("!","")
        my_string = my_string.replace("'","")
        my_string = my_string.lower()
        my_string = my_string.split()
        word_dictionary = {}

        # 
        for word in my_string:
            if word in word_dictionary:
                word.strip()
                word_dictionary[word] = len(word)
            else:
                word.strip()
                word_dictionary[word] = len(word)
        return word_dictionary
    print(word_lengths("I hate a bowl of cereal out of a dog bowl today"))

if __name__ == "__main__":
    main()