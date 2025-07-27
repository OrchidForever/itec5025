def start_horror():
    print("Black Hollow Academy was built in 1812, a sprawling estate of cold stone and older secrets. The new scholarship students arrived just before winter—seven of them, handpicked. The eighth bed in the dormitory is always made, though no one remembers doing it. At night, they hear it creak as if someone is lying down… and each morning, one of them wakes up with someone else's nightmare.")
    characterName = input("What's your student's name: ")
    characterDescription = input("Describe your student: ")
    print(f"Brace yourself {characterName}, the nightmare is just beginning!")
    print("\n\nYou hear whispers in the hallways, shadows moving where there should be none. The headmaster is strict, but there's something off about him. The other students are friendly, but their eyes seem to hold secrets.")
    print("Do you want to visit the library or talk to the headmaster? Alternatively, you can gather with the other students to share stories of the strange occurrences.")
    return characterName, characterDescription, "👻"

def first_choice(user_input: str):
    """Process the first choice input from the user."""
    points = 0
    if "library" in user_input.lower():
        print("You enter the library, the smell of old books fills the air. You find a dusty tome that seems to call to you...")
        value = input("Do you want to read the tome or put it back? (read/put back): ")
        if "read" in value.lower():
            print("As you read, the words seem to shift and change, revealing a dark secret about the academy...")
            print("You gain the tome's knowledge, but at a cost. You feel a chill run down your spine as you realize the truth about the academy's past.")
            print("You now have a clue about the headmaster's true intentions and the dark history of Black Hollow Academy.")
            points += 1
        elif "back" in value.lower():
            print("You decide not to disturb the tome, but you can't shake the feeling that it holds important information.")
            print("You leave the library, but the whispers seem louder now, as if the tome is angry at being ignored.")
            points -= 1
        else:
            print("That's not a valid choice. Please try again.")
    elif "headmaster" in user_input.lower():
        print("You try to meet with the headmaster but he's not there... You feel a sense of unease as you realize that he might be hiding something.")
        print("You decide to investigate his office, but it's locked. You hear strange noises coming from behind the door...")
        value = input("Do you want to try to pick the lock or leave it alone? (pick/leave): ")
        if "pick" in value.lower():
            print("You manage to pick the lock and enter the office. The walls are lined with portraits of previous headmasters, their eyes seeming to follow you.")
            print("You find a hidden drawer in the desk containing a key and a letter revealing the headmaster's dark past.")
            points += 2
        else:
            print("You decide to leave the office alone, but you can't shake the feeling that the headmaster is hiding something important.")
            print("As you walk away, you hear a faint whisper behind you, as if the headmaster is watching you...")
            points -= 1
    elif "students" in user_input.lower():
        print("You gather with the other students, sharing stories of strange occurrences...")
        print("One of them mentions a secret passage in the basement that leads to an old chapel.")
        value = input("Do you want to explore the passage or stay with the group? (explore/stay): ")
        if "explore" in value.lower():
            print("You decide to explore the passage. As you descend into the darkness, the air grows colder...")
            points += 1
        else:
            print("You choose to stay with the group, but the whispers in the back of your mind grow louder...")
            points -= 1
    else:
        print("That's not a valid choice. Please try again.")

    if points != 0:
        message = "Your head is swimming as the voices swell and you're not sure how much more of this school you can take." if points < 0 else "The whispers in your head only seem to grow louder, but you feel a sense of determination to uncover the truth."
        print(message)

    return points