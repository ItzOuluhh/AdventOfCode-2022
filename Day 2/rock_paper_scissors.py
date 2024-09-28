path = "data/database.txt"
fileContent = open(path, "r").readlines()

score = {'X': 1, 'Y': 2, 'Z': 3}
outcome = {'win': 6, 'draw': 3, 'loss': 0}

gameMatches = []

for line in fileContent:
    gameMatches.append(line.split())

def determineOutcome(opponent, me):
    if opponent == 'A':
        if me == 'X': 
            return 'draw'
        elif me == 'Y':
            return 'win'
        elif me == 'Z':
            return 'loss'
    elif opponent == 'B':
        if me == 'X':
            return 'loss'
        elif me == 'Y':
            return 'draw'
        elif me == 'Z':
            return 'win'
    elif opponent == 'C':
        if me == 'X':
            return 'win'
        elif me == 'Y':
            return 'loss'
        elif me == 'Z':
            return 'draw'

def calculateScore(strategyGuide):
    total_score = 0
    for opponent, you in strategyGuide:
        outcome = determineOutcome(opponent, you)
        total_score += score[you] + outcome[outcome]
    return total_score

totalScore = calculateScore(gameMatches)

print(totalScore)

