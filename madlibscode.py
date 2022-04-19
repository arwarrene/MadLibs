"""
Name: Audrey Warrene
Date: 08/26/2021
"""

def intro():
    """
    This simply prints out the intro to the user
    """
    print("\nWelcome to the game of Mad Libs.")
    print("I will ask you to provide several words and phrases to fill in a mad lib story.")
    print("The result will be written to an output file.")
    print("")

def file_name():
    """
    This will ask the user for a input file, searches if that input file exists, and if it does, returns the file.
    Otherwise, the user has three attempts to enter a file that exists, or else the program stops.
    :return: returns the file name that the original story is on, or else "false" to show the user failed all attempts
    """
    import os.path
    x = 0
    file = input("Input file name: ")
    file = file.lower()
    exists = os.path.isfile(file)
    if exists == True:
        return file
    else:
        while x < 2:
            retry = input("File not found. Try again: ")
            retry = retry.lower()
            exists2 = os.path.isfile(retry)
            x += 1
            if exists2 == True:
                return retry
        if x == 2:
            print("\nFile cannot be found. Please restart and try again.\n")
            return False

def output_name():
    """
    This function simply asks the user for a output file. The name given will be turned into a
    file even if it doesn't exist.
    :return: returns the name of the output file that the final story will be written to
    """
    output = input("Output file name: ")
    if ".txt" not in output:
        output = output + ".txt"
        return output
    else:
        return output

def reading_file(inputname):
    """
    This function reads the input file given and finds the words that will be replaced by the users words.
    :param inputname: the file that contains the original story
    :return: returns the words that need to be replaced in the original story
    """
    fillins = []
    others = []

    file = open(inputname, "r")
    lines = file.readlines()
    for line in lines:
        line = line.split(" ")
        for word in line:
            if "<" in word:
                fillins.append(word)
            else:
                others.append(word)
    file.close()
    return fillins

def fillins2(fillins):
    """
    This function creates a copy of the words that will be replaced, so that the newline characters are not lost
    :param fillins: the words that need to be replaced by the user
    :return: returns a copy of fillins that contains the new line character
    """
    fillins2 = []

    for word in fillins:
        fillins2.append(word)
    return fillins2


def asking_user(fillins):
    """
    This function uses the words that will be replaced and asks the user to enter a new one, then saves the new
    words and returns a list of them.
    :param fillins: this is a list that contains the words that need to be replaced.
    :return: returns the new words that will be used in the original story
    """
    vowels = ["a", "e", "i", "o", "u"]
    newwords = []

    for word in fillins:
        word = word.strip()
        word = word.strip("<")
        word = word.strip(">")
        word = word.replace("-", " ")
        if word[0] in vowels:
            new = input("Please type an "+ word + ": ")
            newwords.append(new)
        else:
            new2 = input("Please type a "+ word + ": ")
            newwords.append(new2)
    return newwords

def replacing(newwords, inputname):
    """
    This function takes the original story, replaces the original words with the new words the user gave, and then
    returns this list.
    :param newwords: the words that were inputted by the user to replace the old storys words.
    :param inputname: the file that contains the original story.
    :return: returns the new story in a list.
    """
    file = open(inputname, "r")
    story = file.readlines()
    lst = []
    lst2 = []

    for line in story:
        line = line.split(" ")
        for word in line:
            lst.append(word)

    index = 0
    for word in lst:
        if "<" in word:
            if "\n" in word:
                new = word.replace(word, newwords[index] +"\n")
                lst2.append(new)
                index += 1
            else:
                new = word.replace(word, newwords[index])
                lst2.append(new)
                index += 1
        else:
            lst2.append(word)
    return lst2

def outputing(finalstory, outputname):
    """
    This function asks the user if they would like to see the updated story. If they do, the story is written
    to the output file that was chosen, and then is printed to the screen.
    :param finalstory: The final story that was created with new words.
    :param outputname: The file that the final story will be written to.
    :return: Only returns false if story does not want to be seen.
        """

    print("\nYour MadLib story has been created.")
    y_or_n = input("\nDo you want to see the resulting story? (Y|N) ")
    y_or_n = y_or_n.lower()
    if y_or_n == "y":
        print("\nHere is the resulting MadLib: ")
        file = open(outputname, "w")
        file.writelines(" ".join(finalstory))
        file.close()

        final = open(outputname, "r")
        print(final.read())
    else:
        print("Okay. Goodbye!")
        return False



def main():
    intro()
    inputname = file_name()
    if inputname == False:
        return
    else:
        outputname = output_name()
        fillinwords = reading_file(inputname)
        fillincopy = fillins2(fillinwords)
        newwords = asking_user(fillinwords)
        finalstory = replacing(newwords, inputname)
        output = outputing(finalstory, outputname)

    replay = True
    if output == False:
        return
    else:
        while replay == True:
            """
            This while function is letting the user replay the MadLibs until they choose not to.
            """
            replaying = input("\nDo you want to process another MadLib? (Y|N) ")
            replaying = replaying.lower()
            if replaying == "y":
                intro()
                inputname = file_name()
                outputname = output_name()
                fillinwords = reading_file(inputname)
                fillincopy = fillins2(fillinwords)
                newwords = asking_user(fillinwords)
                finalstory = replacing(newwords, inputname)
                outputing(finalstory, outputname)
                replay = True
            else:
                replay = False
                break

if __name__ == "__main__":
    main()
