def start_mystery(self):
    print("Starting a mystery adventure...")
    print("Imagine a world filled with secrets, hidden clues, and enigmatic characters.")
    print("You are a detective on a case to solve a perplexing crime.")
    characterName = input("What's your detective's name: ")
    characterDescription = input("Describe your detective: ")
    print(f"Welcome {characterName}, let's crack this case wide open!")
    #First Choice
    print("Rain slicked the pavement when she walked into my office—red lips, black veil, and a smell like trouble bottled in Chanel No. 5. Said her husband went out for cigarettes three nights ago and never came back. Funny thing is, he's the third man on that block to vanish this month… and they all left behind the same thing: a pack of smokes, unopened, on the kitchen table.")
    print("Do you want to talk to the wife, investigate the neighborhood and other missing men, or check the husband's workplace?")
    return characterName, characterDescription, "🕵️‍♂️"
