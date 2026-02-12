WAKE_PHRASES = {
    "en": ["hi hercules", "hello hercules"],
    "pt": ["oi hercules", "olá hercules"],
    "es": ["hola hercules"],
    "fr": ["salut hercules"],
    "de": ["hallo hercules"]
}


def get_wake_phrases(lang_code: str):
    return WAKE_PHRASES.get(lang_code, WAKE_PHRASES["en"])
