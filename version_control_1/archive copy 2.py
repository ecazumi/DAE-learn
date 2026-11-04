#this is archive, peace and love
def search_texts(keyword, files):
    total_matches = 0
#before the program runs, the matches found will always be 0
    for filename in files: 
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
#the above 3 lines open each file in a list of files (see line 33-39)
        paragraphs = text.split("\n\n")
#\n is newline (spacing). it splits a text based on the spacing
        for paragraph in paragraphs:
            if keyword.lower() in paragraph.lower():
                print(f"\nEntry ({filename}): {paragraph}")
                total_matches += 1
#the previous lines lowercase the input and the text so it can search for the keyword without being caps-sensitive.
#it prints the entry name and paragraph and add one number to the number of matches found.
    if total_matches == 0:
        print("No matches were found.")
    else:
        print(f"\nTotal number of matching entries found: {total_matches}")
#prints the number of matches found, and the names of the text files that contain the keyword input.

def count_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    
    words = text.split()
    word_count = len(words)

    print(f"\nEntry: {filename}")
    print(f"Number of words: {word_count}")
#This function is for option 2, counting the number of words in a certain text file. It uses the split function to split the paragraphs/sentences/lines in the text file
#it reads the words one by one and counts them with the len function, and prints the name of the entry and words in it.
files = [
    "texts/optimusprime.txt",
    "texts/bumblebee.txt",
    "texts/ratchet.txt",
    "texts/starscream.txt",
    "texts/knockout.txt"
]
#above is a list of the entries
while True:
    print("\n This is the Archive.")
    print("To search entries for a keyword, enter 1.")
    print("To count the words of an entry, enter 2.")
    print("To leave, enter 3.")
#the while true makes sure it always prints the opening after every choice or running of the program
    choice = input("Enter an option: ")
    if choice == "1":
        keyword = input("Enter keyword to search for: ")
#this creates input, telling the system what to ask for (to run function 1, function 2, or exit.)
        if keyword.strip() != "":
            search_texts(keyword, files)
        else:
            print("Enter a keyword.")
#If the stripped input is equal to nothing, it will ask for a keyword again. 
    elif choice == "2":
        print("\n Available entries:")
        for filename in files:
            print(filename)
#this runs a loop so it prints every entry and its name, so the user can pick one to count words of.
        picked_file = input("Which entry to count? ")
        # sets a variable, which is the file the user wants to count.
        if picked_file in files:
            count_words(picked_file)
        else:
            print("Entry not found within the list.")
    #prints the wordcount (see the function def) and if the file you entered wasn't on the list, it would say so.
    elif choice == "3":
        print("So long.")
        break
#exits the Archive with a message. 