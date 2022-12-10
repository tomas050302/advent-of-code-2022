# X -> Rock
# Y -> Paper
# Z -> Scissors
keys = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

outcomes = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

pretended_outcomes = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

with open("input.txt", 'r') as f:
    score = 0
    for line in f.readlines():
        line = line.strip()
        game = line.split(' ')
        opponent = game[0]
        played = game[1]

        score += keys[played]

        if (opponent == "A" and played == "X") or (opponent == "B" and played == "Y") or (opponent == "C" and played == "Z"):
            score += outcomes["draw"]
        elif (opponent == "A" and played == "Y") or (opponent == "B" and played == "Z") or (opponent == "C" and played == "X"):
            score += outcomes["win"]
        else:
            score += outcomes["lose"]
    print()
    print(f'Part 1 answer:', score)

with open("input.txt", 'r') as f:
    score = 0
    for line in f.readlines():
        line = line.strip()
        game = line.split(' ')
        opponent = game[0]
        pretended_outcome = game[1]

        score += pretended_outcomes[pretended_outcome]

        if (pretended_outcome == "Y"):
            score += keys[opponent]
        elif (pretended_outcome == "X"):
            # need to choose right key to loose
            if (opponent == "A"):
                score += keys["Z"]
            elif (opponent == "B"):
                score += keys["X"]
            else:
                score += keys["Y"]
        else:
            # need to choose right key to win
            if (opponent == "A"):
                score += keys["Y"]
            elif (opponent == "B"):
                score += keys["Z"]
            else:
                score += keys["X"]

    print(f'Part 2 answer:', score)
