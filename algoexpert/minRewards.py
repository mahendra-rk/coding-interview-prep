def minRewards(scores):
	rewards = [1] * len(scores)
	#start from index 1, move left to right
	for i in range(1, len(scores)):
		#if number greater then prev num, reward = reward of prev num +1
		if scores[i] > scores[i-1]: 
			rewards[i] = rewards[i-1] + 1
	print(rewards)		
	#start at one before last, move right to left(reversed)
	for i in range(len(scores)-2, -1, -1):
		#if number greater then next num, reward = MAX OF reward of next num +1 OR current reward
		# max for accomodating edge case where current reward is higher because of left to right iteration
		if scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i+1]+1, rewards[i]) 
	print(rewards)				
	return sum(rewards)
    