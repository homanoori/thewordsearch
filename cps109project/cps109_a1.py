# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 01:42:13 2023

@author: Homa Ahmadinoori
PROBLEM DESCRIPTION:
    This code allows users to locate a specific word within a text file.
    Users are presented with a menu at the beginning, giving them the option to search or exit the program.
    There are two text files available in the 'data' folder named 'Hamlet' and 'Freedom', which the user can choose and search within that chosen file.
    The program is designed to provide the number of occurrences of the word and the lines where it is found.
    If the word is not found in the selected file, the program will display "not found". 
    Punctuation does not affect the program's ability to find the word.
    All the results obtained by the user are saved in an output file named "cps109_a1_output" at the end of their session.
    """

# Import string library  
import string 

# Declaring constant variables wich remain unchanged
DATA_PATH = "data/"
OUTPUT_FILE_NAME = "cps109_a1_output.txt"
PUNCTUATIONS = string.punctuation

    
def print_write(sentense):
    """
    Print to console and write to Ouput file

    Input: Sentense (str)
    """
    print(sentense)
    
    # Write to file
    with open(OUTPUT_FILE_NAME, mode = "a") as f:
        f.write(sentense + "\n")
    
    
def remove_punctuations(sentence):
    """
    Remove all punctions from a sentence
    
    Input: Sentence (str)
    Output: Cleared sentence
    """    
    for punc in PUNCTUATIONS:
        sentence = sentence.replace(punc, "")
        
    return sentence

def get_menu_from_user():
    """
    Recursively Get a menu (0 | 1) from user
    
    Output: 0 Exit | 1 Search
    """
    choice = input("\t\t1 Search | 0 Exit: ")
    
    # If user dosen't enter 1 or zero, program will get menu one more time
    if choice != "0" and choice != "1":
        print_write("Invalid input.")
        
        # Recursively get menu if user doesn't enter correct menu
        return get_menu_from_user()
    else:
        return int(choice)
    
    return choice


def get_valid_file_name_from_user():
    """
    Get a valid file name to search
    
    Output: file_name (str), None (if file doesn't exist'
    """
    file_name = input("\t\tEnter filename to search: ")
    file_name += ".txt"
    
    try:
        # Whether file is accessable or not
        with open(DATA_PATH + file_name, mode = "r") as f:
            pass
    except:
        print_write("Error in reading target file: '" + file_name + "' " + "doesn't exist.")  
        return None
    
    return file_name
    

def get_file_content(file_name):
    """
    Read and return all lines of a file.
    There is a \n at the end of each line
    
    Input: Filename
    Output: [] list of all lines of file
    """
    
    print_write(f"Processing {file_name}")
    
    # Open file with alias name f
    # This will close the file automatically
    with open(file_name, mode="r") as f:
        return f.readlines()
    
    
def main():
    print_write("")
    print_write("")
    print_write("Welcome to file searching program.")
    print_write("-" * 10)
    
    file_name = get_valid_file_name_from_user()     
    
    if file_name:
        content = get_file_content(DATA_PATH + file_name)
        
        choice = get_menu_from_user()
        
        while choice == 1:
            # Target user word to search
            word = input("Enter a word: ")
            
            # Number of the times where the word foound in the file
            count = 0
            
            # In which lines the word appeared
            indices = []
        
            # Whether word found or not
            is_found = False
        
            # Go through all lines of the file to find the word
            for i in range(len(content)):
                
                # i-th line of the file
                # Remove all punctuations from the current line
                line = remove_punctuations(content[i])
                
                if word in line.split():
                    # When word found in the current line of the file
                    is_found = True
                    
                    # We want line number, not index
                    indices.append(i + 1)
                    
                    # Default split character is space
                    n_line_word = line.split().count(word)
                    count += n_line_word
                    
            if is_found:
                print_write("'" + word + "' " + "found.")
                print_write("\t Count: " + str(count))
                print_write("\t Lines: " + str(indices))
            else:
                print_write("'" + word + "' " + "not found.")
            
            print_write("")
            
            choice = get_menu_from_user()
        
        
    print_write("-" * 10)
    print_write("Program ends successfully.")


if __name__ == "__main__":
    main()