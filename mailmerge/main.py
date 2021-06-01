PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_{stripped_name}.txt" ,mode="w") as completed:
            completed.write(letter)
