from texts.translate import translate_text, translate_text_print
from data.stories import MINOR_DISCOVERY_POINTS, MAJOR_DISCOVERY_POINTS, NEGATIVE_DISCOVERY_POINTS, HORROR_STORY

async def start_horror(language: str) -> tuple[str, str, str]:
    _ = await translate_text_print(HORROR_STORY["opening_story"], language)
    _ = await translate_text_print(HORROR_STORY["opening_choice_text"], language)
    return "👻"

async def choice_horror(user_input: str, language: str, step: int) -> int:
    """Process the first choice input from the user."""
    points = 0
    if step == 1:
        translated_choices = [await translate_text(choice, language) for choice in HORROR_STORY["valid_choices_1"]]
    else:
        translated_choices = [await translate_text(choice, language) for choice in HORROR_STORY["valid_choices_2"]]

    if user_input.lower() not in translated_choices:
        return points

    full_choice_array = [await translate_text(option["option"], language) for option in HORROR_STORY["options"]]

    for i, choice in enumerate(full_choice_array):
        if user_input.lower() in choice.lower():
            translated_sub_choices = [await translate_text(sub_choice["choice"], language) for sub_choice in HORROR_STORY["options"][i]["choices"]]
            second_choice_text = await translate_text(HORROR_STORY["options"][i]["text"], language)
            user_choice = input(second_choice_text + " ")
            for j, translated_sub_choice in enumerate(translated_sub_choices):
                if translated_sub_choice in user_choice.lower():
                    points += HORROR_STORY["options"][i]["choices"][j]["points"]
                    _ = await translate_text_print(HORROR_STORY["options"][i]["choices"][j]["text"], language)
                    break

    if points != 0:
        message = HORROR_STORY["negative_message"] if points < 0 else HORROR_STORY["positive_message"]
        _ = await translate_text_print(message, language)
        next_choice_text = HORROR_STORY["choice_text_1_max"] if points == MAJOR_DISCOVERY_POINTS else HORROR_STORY["choice_text_1_other"]
        _ = await translate_text_print(next_choice_text, language)
    return points

async def end_horror_story(language: str, points: int) -> str:
    """End the horror story based on the points."""
    if points >= HORROR_STORY["max_success_points"]:
        return await translate_text_print(HORROR_STORY["max_success_text"], language)
    elif points >= HORROR_STORY["min_success_points"]:
        return await translate_text_print(HORROR_STORY["min_success_text"], language)
    else:
        return await translate_text_print(HORROR_STORY["failure_text"], language)