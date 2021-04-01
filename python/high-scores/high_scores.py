def latest(scores):
    return scores[-1]

def personal_best(scores):
    return sorted(scores)[-1]

def personal_top_three(scores):
    sorted_scores = sorted(scores)
    if len(sorted_scores) <= 3:
        sorted_scores.reverse()
        return sorted_scores
    else:
        top_three = sorted_scores[-3:None]
        top_three.reverse()
        return top_three