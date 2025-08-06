import asyncio
from googletrans import Translator

async def translate_text_print(text: str, dest_language: str) -> None:
    translator = Translator()
    translated = await translator.translate(text, dest=dest_language)
    print(translated.text)

async def translate_text(text: str, dest_language: str) -> str:
    translator = Translator()
    translated = await translator.translate(text, dest=dest_language)
    return translated.text