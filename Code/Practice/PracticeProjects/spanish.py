## Made by following https://www.youtube.com/watch?v=4TZ1K8EHT2M
## Not perfect but will go in and make a V2 later

import random

spanish_words = [
    {"spanish": "de", "english": ["of", "from"]},
    {"spanish": "la", "english": ["the (feminine)"]},
    {"spanish": "que", "english": ["that", "which"]},
    {"spanish": "el", "english": ["the (masculine)"]},
    {"spanish": "en", "english": ["in", "on"]},
    {"spanish": "y", "english": ["and"]},
    {"spanish": "a", "english": ["to", "at"]},
    {"spanish": "los", "english": ["the (plural, masculine)"]},
    {"spanish": "se", "english": ["oneself", "himself", "herself"]},
    {"spanish": "del", "english": ["of the", "from the"]},
    {"spanish": "las", "english": ["the (plural, feminine)"]},
    {"spanish": "un", "english": ["a", "an (masculine)"]},
    {"spanish": "por", "english": ["for", "by", "through"]},
    {"spanish": "con", "english": ["with"]},
    {"spanish": "no", "english": ["no", "not"]},
    {"spanish": "una", "english": ["a", "an (feminine)"]},
    {"spanish": "su", "english": ["his", "her", "their", "your"]},
    {"spanish": "para", "english": ["for", "to", "in order to"]},
    {"spanish": "es", "english": ["is", "it is"]},
    {"spanish": "al", "english": ["to the", "at the"]},
    {"spanish": "lo", "english": ["it", "him"]},
    {"spanish": "como", "english": ["like", "as"]},
    {"spanish": "más", "english": ["more"]},
    {"spanish": "pero", "english": ["but"]},
    {"spanish": "sus", "english": ["his", "her", "their (plural)"]},
    {"spanish": "le", "english": ["to him", "to her"]},
    {"spanish": "ya", "english": ["already", "now"]},
    {"spanish": "o", "english": ["or"]},
    {"spanish": "este", "english": ["this (masculine)"]},
    {"spanish": "sí", "english": ["yes"]},
    {"spanish": "porque", "english": ["because"]},
    {"spanish": "esta", "english": ["this (feminine)"]},
    {"spanish": "entre", "english": ["between", "among"]},
    {"spanish": "cuando", "english": ["when"]},
    {"spanish": "muy", "english": ["very"]},
    {"spanish": "sin", "english": ["without"]},
    {"spanish": "sobre", "english": ["on", "about"]},
    {"spanish": "también", "english": ["also", "too"]},
    {"spanish": "me", "english": ["me", "myself"]},
    {"spanish": "hasta", "english": ["until", "up to"]},
    {"spanish": "hay", "english": ["there is", "there are"]},
    {"spanish": "donde", "english": ["where"]},
    {"spanish": "quien", "english": ["who"]},
    {"spanish": "desde", "english": ["from", "since"]},
    {"spanish": "todo", "english": ["all", "everything"]},
    {"spanish": "nos", "english": ["us", "ourselves"]},
    {"spanish": "durante", "english": ["during"]},
    {"spanish": "todos", "english": ["all (masculine, plural)"]},
    {"spanish": "uno", "english": ["one"]},
    {"spanish": "les", "english": ["to them", "you all"]},
    {"spanish": "ni", "english": ["neither", "nor"]},
    {"spanish": "contra", "english": ["against"]},
    {"spanish": "otros", "english": ["others (masculine, plural)"]},
    {"spanish": "ese", "english": ["that (masculine)"]},
    {"spanish": "eso", "english": ["that (neuter)"]},
    {"spanish": "ante", "english": ["before", "in front of"]},
    {"spanish": "ellos", "english": ["they (masculine)"]},
    {"spanish": "e", "english": ["and (before i- or hi- words)"]},
    {"spanish": "esto", "english": ["this (neuter)"]},
    {"spanish": "mí", "english": ["me"]},
    {"spanish": "antes", "english": ["before"]},
    {"spanish": "algunos", "english": ["some (masculine, plural)"]},
    {"spanish": "qué", "english": ["what", "which"]},
    {"spanish": "unos", "english": ["some (masculine)"]},
    {"spanish": "yo", "english": ["I"]},
    {"spanish": "otro", "english": ["other", "another (masculine)"]},
    {"spanish": "otras", "english": ["others (feminine, plural)"]},
    {"spanish": "otra", "english": ["other", "another (feminine)"]},
    {"spanish": "él", "english": ["he", "him"]},
    {"spanish": "tanto", "english": ["so much", "so many"]},
    {"spanish": "esa", "english": ["that (feminine)"]},
    {"spanish": "estos", "english": ["these (masculine)"]},
    {"spanish": "mucho", "english": ["much", "a lot"]},
    {"spanish": "quienes", "english": ["who (plural)"]},
    {"spanish": "nada", "english": ["nothing"]},
    {"spanish": "muchos", "english": ["many (masculine)"]},
    {"spanish": "cual", "english": ["which"]},
    {"spanish": "poco", "english": ["little", "few"]},
    {"spanish": "ella", "english": ["she", "her"]},
    {"spanish": "estar", "english": ["to be"]},
    {"spanish": "estas", "english": ["these (feminine)"]},
    {"spanish": "algunas", "english": ["some (feminine, plural)"]},
    {"spanish": "algo", "english": ["something"]},
    {"spanish": "nosotros", "english": ["we", "us (masculine)"]},
    {"spanish": "mi", "english": ["my"]},
    {"spanish": "mis", "english": ["my (plural)"]},
    {"spanish": "tú", "english": ["you (informal)"]},
    {"spanish": "te", "english": ["you (direct/indirect object)"]},
    {"spanish": "ti", "english": ["you (after preposition)"]},
    {"spanish": "tu", "english": ["your (informal)"]},
    {"spanish": "tus", "english": ["your (plural)"]},
    {"spanish": "ellas", "english": ["they (feminine)"]},
    {"spanish": "nosotras", "english": ["we", "us (feminine)"]},
    {"spanish": "vosotros", "english": ["you all (masculine, informal Spain)"]},
    {"spanish": "vosotras", "english": ["you all (feminine, informal Spain)"]},
    {"spanish": "os", "english": ["you all (Spain)"]},
    {"spanish": "mío", "english": ["mine (masculine)"]},
    {"spanish": "mía", "english": ["mine (feminine)"]},
    {"spanish": "míos", "english": ["mine (masculine, plural)"]},
    {"spanish": "mías", "english": ["mine (feminine, plural)"]},
    {"spanish": "tuyo", "english": ["yours (masculine)"]},
    {"spanish": "tuya", "english": ["yours (feminine)"]},
    {"spanish": "tuyos", "english": ["yours (masculine, plural)"]},
    {"spanish": "tuyas", "english": ["yours (feminine, plural)"]},
    {"spanish": "suyo", "english": ["his", "hers", "theirs", "yours (masculine)"]},
    {"spanish": "suya", "english": ["his", "hers", "theirs", "yours (feminine)"]},
    {"spanish": "suyos", "english": ["his", "hers", "theirs", "yours (masculine, plural)"]},
    {"spanish": "suyas", "english": ["his", "hers", "theirs", "yours (feminine, plural)"]},
    {"spanish": "nuestro", "english": ["our (masculine)"]},
    {"spanish": "nuestra", "english": ["our (feminine)"]}
]

def quiz_user(spanish_words):
    random.shuffle(spanish_words)
    score = 0
    for words in spanish_words:
        answer = input(f"What is the English translation of '{words['spanish']}'? ").strip().lower()
        # Check if answer matches any translation (case-insensitive)
        correct_answers = [e.lower() for e in words['english']]
        if answer in correct_answers:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answers are: {', '.join(words['english'])}.")
    print(f"Your score: {score}/{len(spanish_words)}")

def main():
    print("Welcome to the spanish.py flashcards!")
    input("Press Enter to see the first word...")
    quiz_user(spanish_words)

if __name__ == "__main__":
    main()
