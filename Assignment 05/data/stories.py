MAJOR_DISCOVERY_POINTS = 2
MINOR_DISCOVERY_POINTS = 1
NEGATIVE_DISCOVERY_POINTS = -1

HORROR_STORY = {
    "genre": "horror",
    "title": "Black Hollow Academy",
    "description": "A chilling tale set in a haunted academy where dark secrets lurk in the shadows.",
    "opening_story": """Black Hollow Academy was built in 1812, a sprawling estate of cold stone and older secrets. 
    The new scholarship students arrived just before winter—seven of them, handpicked. 
    The eighth bed in the dormitory is always made, though no one remembers doing it...""",
    "opening_choice_text": "You hear whispers in the hallways, shadows moving where there should be none. The headmaster is strict, but there's something off about him. The other students are friendly, but their eyes seem to hold secrets.\n\nDo you want to visit the library or talk to the headmaster? Alternatively, you can gather with the other students to share stories of the strange occurrences. ( library / headmaster /students ): ",
    "positive_message": "The whispers in your head only seem to grow louder, but you feel a sense of determination to uncover the truth.",
    "negative_message": "Your head is swimming as the voices swell and you're not sure how much more of this school you can take.",
    "choice_text_1_max": "\nDo you want to continue exploring the academy or confront the headmaster? (explore/confront): ",
    "choice_text_1_other": "\nDo you want to continue exploring the academy or leave? ( explore / leave ): ",
    "max_success_text": "You have successfully uncovered the dark secrets of Black Hollow Academy. The feeling of dread lingers, but you have the knowledge to protect yourself and others.",
    "min_success_text": "You have discovered some unsettling truths about Black Hollow Academy. You know there is more to discover but you need to be careful. Next year.",
    "failure_text": "You have failed to uncover the secrets of Black Hollow Academy. The whispers grow louder, and you feel a sense of dread as you leave the academy behind.",
    "valid_choices_1": ["library", "headmaster", "students"],
    "valid_choices_2": ["explore", "confront", "leave"],
    "end_story_text": "The end of the year is wrapping up. The whispers in your head are louder than ever, but you feel a sense of accomplishment for surviving a year at Black Hollow Academy. Some were not as accomplished as you. (continue):",
    "max_success_points": 4,
    "min_success_points": 2,
    "options": [
        {
            "option": "library",
            "text": "You enter the library, the smell of old books fills the air. You find a dusty tome that seems to call to you...\n\nDo you want to read the tome or put it back? (read / put back): ",
            "choices": [
                {
                    "choice": "read",
                    "text": "As you read, the words seem to shift and change, revealing a dark secret about the academy...\nYou gain the tome's knowledge, but at a cost. You feel a chill run down your spine as you realize the truth about the academy's past.\nYou now have a clue about the headmaster's true intentions and the dark history of Black Hollow Academy.",
                    "points": MINOR_DISCOVERY_POINTS
                },
                {
                    "choice": "put back",
                    "text": "You decide not to disturb the tome, but you can't shake the feeling that it holds important information.\nYou leave the library, but the whispers seem louder now, as if the tome is angry at being ignored.",
                    "points": NEGATIVE_DISCOVERY_POINTS
                }
            ]
        },
        {
            "option": "headmaster",
            "text": "You try to meet with the headmaster but he's not there... You feel a sense of unease as you realize that he might be hiding something.\nYou decide to investigate his office, but it's locked. You hear strange noises coming from behind the door...\n\nDo you want to try to pick the lock or leave it alone? (pick the lock / leave):",
            "choices": [
                {
                    "choice": "pick",
                    "text": "You manage to pick the lock and enter the office. The walls are lined with portraits of previous headmasters, their eyes seeming to follow you.\nYou find a hidden drawer in the desk containing a key and a letter revealing the headmaster's dark past.",
                    "points": MAJOR_DISCOVERY_POINTS
                },
                {
                    "choice": "leave",
                    "text": "You decide to leave the office alone, but you can't shake the feeling that the headmaster is hiding something important.\nAs you walk away, you hear a faint whisper behind you, as if the headmaster is watching you...",
                    "points": NEGATIVE_DISCOVERY_POINTS
                }
            ]
        },
        {
            "option": "students",
            "text": "You gather with the other students, sharing stories of strange occurrences...\nOne of them mentions a secret passage in the basement that leads to an old chapel.\n\nDo you want to explore the passage or stay with the group? (explore/stay):",
            "choices": [
                {
                    "choice": "explore",
                    "text": "You decide to explore the passage. As you descend into the darkness, the air grows colder...\nYou find the chapel, its walls covered in strange symbols. In the center, a dark altar holds a weird artifact.\nYou gain some knowledge about the academy's dark rituals and the artifact's power.",
                    "points": MINOR_DISCOVERY_POINTS
                },
                {
                    "choice": "stay",
                    "text": "You decide to stay with the group. While you share stories, you can't shake the feeling that you're missing out on something important.\nYou leave the conversation with a sense of unease.",
                    "points": NEGATIVE_DISCOVERY_POINTS
                }
            ]
        }, 
        {
            "option": "explore",
            "text": "You decide to explore the academy further, delving into its dark corners and uncovering more secrets...\n\nYou come across a weird raven statue and you're not sure if it's a secret or not. The whispers in your head grow louder, urging you to investigate further. Do you want to touch the statue or find something else to do? (touch/next): ",
            "choices": [
                {
                    "choice": "touch",
                    "text": "You reach out and touch the raven statue. Suddenly, the whispers intensify, and you feel a surge of energy coursing through you...\nYou gain a new ability to communicate with the spirits of the academy.",
                    "points": MAJOR_DISCOVERY_POINTS
                },
                {
                    "choice": "next",
                    "text": "You decide to find something else to do. As you walk away from the statue, the whispers fade, but you can't shake the feeling that you missed an important opportunity.",
                    "points": NEGATIVE_DISCOVERY_POINTS
                }
            ]
        }, 
        {
            "option": "confront",
            "text": "You decide to confront the headmaster about the whispers and the strange occurrences...\n\nHe's not in his office, so you seek him out. He seems surprised but quickly regains his composure. He tells you that the academy has a long history of strange events and that you should not worry about it. After all, they have many distinguished graduates and you would do well to try to be one of them. Do you want to press him for more information or drop the subject? (press/drop): ",
            "choices": [
                {
                    "choice": "press",
                    "text": "You press the headmaster for more information, but he becomes defensive and tells you to focus on your studies.\nYou leave the conversation feeling frustrated and more determined to uncover the truth.",
                    "points": NEGATIVE_DISCOVERY_POINTS
                },
                {
                    "choice": "drop",
                    "text": "You try to reason with the headmaster, but he remains evasive. You decide to drop the subject for now, but you can't shake the feeling that he's hiding something important.\nYou leave the conversation with a sense of unease.",
                    "points": NEGATIVE_DISCOVERY_POINTS
                }
            ]
        },
        {
            "option": "leave",
            "text": "You decide to leave the academy, but the whispers follow you...\n\nAs you walk away, you feel a chill run down your spine. The academy's secrets may never be uncovered, but you can't shake the feeling that something dark is lurking just beneath the surface. Do you want to search outside the academy or leave your journey? (search/leave): ",
            "choices": [
                {
                    "choice": "search",
                    "text": "You search outside the academy, hoping to find clues about its dark past. As you explore the grounds, you come across an old, hidden entrance leading to the catacombs below.\nYou gain valuable knowledge about the academy's history and its connection to the supernatural.",
                    "points": MINOR_DISCOVERY_POINTS
                }, 
                {
                    "choice": "leave",
                    "text": "You decide to leave your journey, but the whispers continue to haunt you. You can't shake the feeling that the academy's secrets will always remain just out of reach.\nYou leave with a sense of unease, knowing that the truth may never be fully revealed.",
                    "points": -10
                }
            ]
        }
    ]
}