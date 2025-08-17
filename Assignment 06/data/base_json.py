MAJOR_DISCOVERY_POINTS = 2
MINOR_DISCOVERY_POINTS = 1
NEGATIVE_DISCOVERY_POINTS = -1

HORROR_STORY_TF = {
    "metadata": {
        "genre": "horror",
        "title": "Black Hollow Academy",
        "description": "A chilling tale set in a haunted academy where dark secrets lurk in the shadows.",
        "max_success_points": 4,
        "min_success_points": 2,
        "genre_id": 0,  # Numeric encoding for genre
    },
    
    # Text data for processing
    "texts": {
        "opening_story": """Black Hollow Academy was built in 1812, a sprawling estate of cold stone and older secrets. 
        The new scholarship students arrived just before winter—seven of them, handpicked. 
        The eighth bed in the dormitory is always made, though no one remembers doing it...""",
        
        "opening_choice_text": "You hear whispers in the hallways, shadows moving where there should be none. The headmaster is strict, but there's something off about him. The other students are friendly, but their eyes seem to hold secrets. Do you want to visit the library or talk to the headmaster? Alternatively, you can gather with the other students to share stories of the strange occurrences.",
        
        "positive_message": "The whispers in your head only seem to grow louder, but you feel a sense of determination to uncover the truth.",
        "negative_message": "Your head is swimming as the voices swell and you're not sure how much more of this school you can take.",
        
        "max_success_text": "You have successfully uncovered the dark secrets of Black Hollow Academy. The feeling of dread lingers, but you have the knowledge to protect yourself and others.",
        "min_success_text": "You have discovered some unsettling truths about Black Hollow Academy. You know there is more to discover but you need to be careful. Next year.",
        "failure_text": "You have failed to uncover the secrets of Black Hollow Academy. The whispers grow louder, and you feel a sense of dread as you leave the academy behind.",
        
        "end_story_text": "The end of the year is wrapping up. The whispers in your head are louder than ever, but you feel a sense of accomplishment for surviving a year at Black Hollow Academy. Some were not as accomplished as you.",
    },
    
    # Choice mappings for model training
    "choice_mappings": {
        "valid_choices_1": ["library", "headmaster", "students"],
        "valid_choices_2": ["explore", "confront", "leave"],
        "choice_to_id_1": {"library": 0, "headmaster": 1, "students": 2},
        "choice_to_id_2": {"explore": 0, "confront": 1, "leave": 2},
    },
    
    # Training data structure
    "training_data": [
        # Each entry: (context_text, choice_options, optimal_choice_id, points_reward)
        {
            "context": "You enter the library, the smell of old books fills the air. You find a dusty tome that seems to call to you...",
            "choices": ["read", "put back"],
            "choice_ids": [0, 1],
            "outcomes": [
                {"choice_id": 0, "points": MINOR_DISCOVERY_POINTS, "text": "As you read, the words seem to shift and change, revealing a dark secret about the academy..."},
                {"choice_id": 1, "points": NEGATIVE_DISCOVERY_POINTS, "text": "You decide not to disturb the tome, but you can't shake the feeling that it holds important information..."}
            ]
        },
        {
            "context": "You try to meet with the headmaster but he's not there... You feel a sense of unease as you realize that he might be hiding something.",
            "choices": ["pick", "leave"],
            "choice_ids": [0, 1],
            "outcomes": [
                {"choice_id": 0, "points": MAJOR_DISCOVERY_POINTS, "text": "You manage to pick the lock and enter the office. The walls are lined with portraits of previous headmasters..."},
                {"choice_id": 1, "points": NEGATIVE_DISCOVERY_POINTS, "text": "You decide to leave the office alone, but you can't shake the feeling that the headmaster is hiding something important..."}
            ]
        },
        # Add more training examples...
    ]
}