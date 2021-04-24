placeholder = "[name]"

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as main_letter:
    letter_contents = main_letter.read()
    for name in names:
        new_letter = letter_contents.replace(placeholder, name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as guest_letter:
            guest_letter.write(new_letter)
