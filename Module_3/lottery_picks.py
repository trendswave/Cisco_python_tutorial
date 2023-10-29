#The draw from the lottery organisation
 
lotteryDraw = [98, 1, 59, 70, 37, 4]

#your picks for lucks

picks = [3, 7, 11, 42, 34, 49]
#the matching outcome from their draw

matchs = 0
 
for number in picks:
    if number in lotteryDraw:
        matchs += 1 # Or matchs = matchs + 1
	
 
print("This are the numbers you got":, matchs)
