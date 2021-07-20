def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    revScores = sorted(scores,reverse=True)
    return revScores[0:3]
