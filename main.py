def clean_word(word):
    return word.strip().lower()

def word_value(word):
    word_value_sum = 0
    for char in word:
        word_value_sum = word_value_sum+ord(char)
    return(word_value_sum)    

# request the source and destination files for reading (source)
# and writing (destination)    
dictionary_file = input("Enter the dictionary file: ")


# Ensure that any file errors are caught
try:
    # Open the source and desitnation files
    dictionary = open(dictionary_file, "r")
    dictionary_sum = 0
    #print(dictionary.tell())
    
    # for each word in the source file, reverse the word and write it
    # to the destination file
    for word in dictionary:
        dictionary_sum = dictionary_sum + word_value(clean_word(word))
    
    # close the files
    dictionary.close()
    
    # indicate that the process has finished
    print("The value of all the characters in the dictionary file is: ",
          dictionary_sum)

except FileNotFoundError:
    print("The dictionary file was not found")