# first of all open the names as read
with open("./Input/Names/invited_names.txt") as invited:
    # save it in a varianble as a list with the readslines function
    invited_names = invited.readlines()
    print(invited_names)

# open up the letter u want to send blue print 
with open("./Input/Letters/starting_letter.txt") as letters:
    letters = letters.read()
    # loop through it with respect to the list of names you called out firstly
    for name in invited_names:
        # strip each name item in invited names lists of its spaces 
        name = name.strip()
        # create a new letter for every name you loop changing the [name] in the main letteer to the new name you are looping with in the invited_names with the replace function
        new_letter = letters.replace("[name]", name)
        # for evey new letter you create write to hthe output folder a new file of the letter
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode = 'w') as Output_letter:
            saved = Output_letter.write(new_letter)