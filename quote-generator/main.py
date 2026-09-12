# main.py

import random

quotes = [
    ("Do not go where the path may lead, go instead where there is no path and leave a trail.", "Ralph Waldo Emerson"),

    ("A successful book is not made of what is in it, but what is left out of it.", "Mark Twain"),

    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),

    ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis"),

    ("A man who moves mountains begins by carrying away small stones.", "Confucius"),

    ("We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "Aristotle"),

    ("He who is not courageous enough to take risks will accomplish nothing in life.", "Muhammad Ali"),

    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),

    ("Be daring, be different, be impractical, be anything that will assert integrity of purpose and imaginative vision against the play-it-safers, the creatures of the commonplace, the slaves of the ordinary.", "Cecil Beaton"),

    ("Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.", "Roy T. Bennett")
]

def generate_quote(quotes):
    (quote, author) = random.choice(quotes)
    return f'\n"{quote}" - {author}\n'

print(generate_quote(quotes))