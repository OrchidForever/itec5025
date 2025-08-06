from texts.translate import translate_text, translate_text_print

async def start_horror(language: str):
    _ = await translate_text_print("Black Hollow Academy was built in 1812, a sprawling estate of cold stone and older secrets. The new scholarship students arrived just before winter—seven of them, handpicked. The eighth bed in the dormitory is always made, though no one remembers doing it. At night, they hear it creak as if someone is lying down… and each morning, one of them wakes up with someone else's nightmare.", language)
    character_name_text = await translate_text("What's your student's name: ", language)
    characterName = input(character_name_text)
    character_description_text = await translate_text("Describe your student: ", language)
    characterDescription = input(character_description_text)
    _ = await translate_text_print(f"Brace yourself {characterName}, the nightmare is just beginning!", language)
    _ = await translate_text_print("\n\nYou hear whispers in the hallways, shadows moving where there should be none. The headmaster is strict, but there's something off about him. The other students are friendly, but their eyes seem to hold secrets.", language)
    _ = await translate_text_print("Do you want to visit the library or talk to the headmaster? Alternatively, you can gather with the other students to share stories of the strange occurrences.", language)
    return characterName, characterDescription, "👻"

async def first_choice_horror(user_input: str, language: str):
    """Process the first choice input from the user."""
    points = 0
    library = await translate_text("library", language)
    read = await translate_text("read", language)
    put_back = await translate_text("back", language)
    headmaster = await translate_text("headmaster", language)
    pick = await translate_text("pick", language)
    student = await translate_text("student", language)
    explore = await translate_text("explore", language)
    leave = await translate_text("leave", language)

    if library in user_input.lower():
        _ = await translate_text_print("You enter the library, the smell of old books fills the air. You find a dusty tome that seems to call to you...", language)
        choice_text = await translate_text("Do you want to read the tome or put it back? (read/put back): ", language)
        value = input(choice_text)
        if read in value.lower():
            _ = await translate_text_print("As you read, the words seem to shift and change, revealing a dark secret about the academy...", language)
            _ = await translate_text_print("You gain the tome's knowledge, but at a cost. You feel a chill run down your spine as you realize the truth about the academy's past.", language)
            _ = await translate_text_print("You now have a clue about the headmaster's true intentions and the dark history of Black Hollow Academy.", language)
            points += 1
        elif put_back in value.lower():
            _ = await translate_text_print("You decide not to disturb the tome, but you can't shake the feeling that it holds important information.", language)
            _ = await translate_text_print("You leave the library, but the whispers seem louder now, as if the tome is angry at being ignored.", language)
            points -= 1
        else:
            _ = await translate_text_print("That's not a valid choice. Please try again.", language)
    elif headmaster in user_input.lower():
        _ = await translate_text_print("You try to meet with the headmaster but he's not there... You feel a sense of unease as you realize that he might be hiding something.", language)
        _ = await translate_text_print("You decide to investigate his office, but it's locked. You hear strange noises coming from behind the door...", language)
        choice_text = await translate_text("Do you want to try to pick the lock or leave it alone? (pick/leave): ", language)
        value = input(choice_text)
        if pick in value.lower():
            _ = await translate_text_print("You manage to pick the lock and enter the office. The walls are lined with portraits of previous headmasters, their eyes seeming to follow you.", language)
            _ = await translate_text_print("You find a hidden drawer in the desk containing a key and a letter revealing the headmaster's dark past.", language)
            points += 2
        elif leave in value.lower():
            _ = await translate_text_print("You decide to leave the office alone, but you can't shake the feeling that the headmaster is hiding something important.", language)
            _ = await translate_text_print("As you walk away, you hear a faint whisper behind you, as if the headmaster is watching you...", language)
            points -= 1
        else:
            _ = await translate_text_print("That's not a valid choice. Please try again.", language)
    elif student in user_input.lower():
        _ = await translate_text_print("You gather with the other students, sharing stories of strange occurrences...", language)
        _ = await translate_text_print("One of them mentions a secret passage in the basement that leads to an old chapel.", language)
        choice_text = await translate_text("Do you want to explore the passage or stay with the group? (explore/stay): ", language)
        value = input(choice_text)
        if explore in value.lower():
            _ = await translate_text_print("You decide to explore the passage. As you descend into the darkness, the air grows colder...", language)
            points += 1
        else:
            _ = await translate_text_print("You choose to stay with the group, but the whispers in the back of your mind grow louder...", language)
            points -= 1
    else:
        _ = await translate_text_print("That's not a valid choice. Please try again.", language)

    if points != 0:
        message = "Your head is swimming as the voices swell and you're not sure how much more of this school you can take." if points < 0 else "The whispers in your head only seem to grow louder, but you feel a sense of determination to uncover the truth."
        _ = await translate_text_print(message, language)
        next_choice_text = "\n\nDo you want to continue exploring the academy or confront the headmaster? (explore/confront): " if points == 2 else "\n\nDo you want to continue exploring the academy or leave? (explore/leave): "
        _ = await translate_text_print(next_choice_text, language)
    return points

async def second_choice_horror(user_input, language):
    points = 0
    explore = await translate_text("explore", language)
    confront = await translate_text("confront", language)
    leave = await translate_text("leave", language)

    if explore in user_input.lower():
        explore_text = "You decide to explore the academy further, delving into its dark corners and uncovering more secrets...\n\nYou come across a weird raven statue and you're not sure if it's a secret or not. The whispers in your head grow louder, urging you to investigate further. Do you want to touch the statue or find something else to do? (touch/next): "
        _ = await translate_text_print(explore_text, language)
        points += 1
    elif confront in user_input.lower():
        confront_text = "You decide to confront the headmaster about the whispers and the strange occurrences...\n\nHe's not in his office, so you seek him out. He seems surprised but quickly regains his composure. He tells you that the academy has a long history of strange events and that you should not worry about it. After all, they have many distinguished graduates and you would do well to try to be one of them. Do you want to press him for more information or drop the subject? (press/drop): "
        _ = await translate_text_print(confront_text, language)
        points += 2
    elif leave in user_input.lower():
        leave_text = "You decide to leave the academy, but the whispers follow you...\n\nAs you walk away, you feel a chill run down your spine. The academy's secrets may never be uncovered, but you can't shake the feeling that something dark is lurking just beneath the surface. Do you want to search outside the academy or leave your journey? (search/leave): "
        _ = await translate_text_print(leave_text, language)
        points -= 1
    else:
        _ = await translate_text_print("That's not a valid choice. Please try again.", language)

    return points