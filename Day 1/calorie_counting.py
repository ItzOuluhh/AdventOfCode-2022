path = 'data/calories.txt'
fileContent = open(path, 'r').readlines()

calorieGroups = []
currentGroup = []

for line in fileContent:
    if line.strip() == '':
        if currentGroup:
            calorieGroups.append(currentGroup)
            currentGroup = []
    else:
        currentGroup.append(line.strip())

if currentGroup:
    calorieGroups.append(currentGroup)

totalCaloriesPerGroup = []

for group in calorieGroups:
    totalGroupCalories = 0

    for i in group:
        totalGroupCalories += int(i)
    totalCaloriesPerGroup.append(totalGroupCalories)

topThreeGroups = sorted(totalCaloriesPerGroup, reverse=True)[:3]
topThreeTotal = sum(topThreeGroups)

print(topThreeTotal)
        


