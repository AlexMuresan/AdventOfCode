import itertools

def scoreRound(round: str):
    round = round.split(" ")

    enemyMap = {
        "A": 1, # rock
        "B": 2, # paper
        "C": 3 # scissors
    }

    playerMap = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    # enemy = 3
    # player = 1

    score = playerMap[round[1]]

    player = playerMap[round[1]]
    enemy = enemyMap[round[0]]

    if player == enemy:
        score += 3
    elif (player == 1) and (enemy == 3):
        score += 6
    elif (player == 3) and (enemy == 1):
        score = score
    elif player > enemy:
        score += 6

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