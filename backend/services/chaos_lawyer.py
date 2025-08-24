import random

OPENERS = [
    "Your Honor, reality is a beta feature.",
    "Objection: physics took the day off.",
    "If the law had plot twists, this is one."
]

ANALOGIES = [
    "If a voicemail can defame, a parrot can sass.",
    "A drone is basically a flying intern with boundary issues.",
    "Intent travels faster than light—allegedly."
]

CLOSES = [
    "Therefore, acquit and award snacks.",
    "Hence, dismiss with celebratory cupcakes.",
    "I rest—on a beanbag of justice."
]

def chaos_response() -> dict:
    return {
        "argument": f"{random.choice(OPENERS)} {random.choice(ANALOGIES)} {random.choice(CLOSES)}",
        "rhetoric": "Loopholes and audacious hypotheticals."
    }
