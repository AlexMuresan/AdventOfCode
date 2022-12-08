import itertools

def scoreRound(round: str):
    round = round.split(" ")
    score = 0

    enemyMap = {
        "A": 1, # rock
        "B": 2, # paper
        "C": 3 # scissors
    }

    scoreMap = {
        "X": 0, # loss
        "Y": 3, # draw
        "Z": 6  # win
    }

    enemy = enemyMap[round[0]]
    outcome = scoreMap[round[1]]

    score = outcome

    if outcome == 3:
        score += enemy
    elif outcome == 0:
        if enemy == 1:
            score += 3
        if enemy == 2:
            score += 1
        if enemy == 3:
            score += 2
    else:
        if enemy == 1:
            score += 2
        if enemy == 2:
            score += 3
        if enemy == 3:
            score += 1

    return score


if __name__ == "__main__":

    with open("guide_test.txt", "r")as f:
        lines = f.readlines()

    clean_lines = list(map(lambda x: x.strip("\n"), lines))
    
    scores = list(map(scoreRound, clean_lines))
    
     print(sum(scores))

    # A Y rock vs paper -> win = 6 + paper = 2 -> score = 8
    # B X paper vs rock -> win = 0 + rock = 1 -> score = 1
    # C Z scissors vs scissors -> win = 3 + paper = 3 -> score = 6
    # C X scissors vs rock -> win = 0 + rock = 1 -> score = 8