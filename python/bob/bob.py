def response(hey_bob):
    hey_bob = hey_bob.strip()

    def responses(statement):
        return {
            "question": "Sure.",
            "yell": "Whoa, chill out!",
            "yell_question": "Calm down, I know what I'm doing!",
            "nothing": "Fine. Be that way!",
            "nuetral": "Whatever."
        }.get(statement)

    if len(hey_bob) == 0:
        return responses("nothing")
    if hey_bob[-1] == "?":
        return responses("yell_question") if hey_bob.isupper() else responses("question")
    return responses("yell") if hey_bob.isupper() else responses("nuetral")
