#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

model = open("Input/Letters/starting_letter.txt",'r')
model = model.read()
with open("Input/Names/invited_names.txt", 'r+') as file:
    for word in file.readlines():
        name = word.split("\n")
        letter = model.replace("[name]",name[0])
        with open(f"Output/ReadyToSend/letter_for_{name[0]}.txt",'w') as letter_finished:
            letter_finished.write(letter)
