import json #import Json module

while True:
    Answer = input("""What do you want to do
                1. Find the meaning of words
                2. Insert new word
                3. Delete a word
                4. Exit the program
                Enter your choice:
                """) #Ask a question to choose between choices
    if Answer == "1":
        filename = "D:/Users/Chirag/Desktop/Python_Class/Data Structures/words.json" #The data base
        with open(filename, "r") as file: #to open words.json file
            try: #protect the code so if there is an error it wont stop the entire script
                fileDict = json.load(file) #convert Javascript json to Python Dictionary 
                FileFinding = input("What would you like to find? ") #The input for what you would like to find
                # print(json.dumps(fileDict, indent = 4, sort_keys= True)) #print entire database
                print(fileDict[FileFinding]) #print only the key words that you try to find
            except KeyError: #except for an error...
                print("there was a key error occured, there is no", FileFinding, "in the database ") #print this


    if Answer == "2":
        filename = "D:/Users/Chirag/Desktop/Python_Class/Data Structures/words.json" #the data base
        with open(filename, "r+") as file:
            try: 
                fileDict = json.load(file) #convert Javascript json to Python Dictionary
                FileFinding = input("What would you like to insert? ")
                if FileFinding in fileDict: 
                    print("that word already exists! Try again ")
                else:
                    Meaning = input("What is the meaning of this word? ")
                    fileDict.update( {FileFinding: [Meaning]} ) 
                    FileName2 = input("Is there another meaning of the word? y/n? ")
                    while FileName2 == "y" or FileName2 == "yes":
                        AddedResponse = input("What is the other meaning of the word? ")
                        fileDict[FileFinding].append(AddedResponse)
                        FileName2 = input("Is there another meaning of the word? y/n? ")
                    
            except KeyError:
                print("there was a key error occured, there is no", FileFinding, "in the database")
            file.seek(0)
            json.dump(fileDict, file, indent = 4)

    
    if Answer == "4":
        print("Thanks for using this program ")
        break
    
    if Answer == "3":
        filename = "D:/Users/Chirag/Desktop/Python_Class/Data Structures/words.json"
        with open(filename, "r+") as file:
            try:
                fileDict = json.load(file)
                FileFinding = input("What word would you like to delete? ")
                fileDict.pop( FileFinding)
            except KeyError:
                print("there was a key error occured, there is no", FileFinding, "in the database ")
        with open(filename, "w+") as file:
            file.seek(0)
            json.dump(fileDict, file, indent = 4)
    
        print("now the total amount of data is", len(fileDict))
    

            

    #MAKE MENU DRIVEN CODE LOOPS FOREVER, so that when you insert a new word you can find it after. It is is in circular QUeue, LInear Queue, and Stack using list. 
