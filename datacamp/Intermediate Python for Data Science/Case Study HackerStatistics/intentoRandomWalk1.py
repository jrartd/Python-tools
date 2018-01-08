#problema conocer la cantidad
#importar numpy 
import numpy as np 

np.random.seed(123)
random_walk = [0]


for x in range (10):
	step = random_walk[-1] #cadapaso
	dice = np.random.randint(1,7)

	if dice <= 2:
		step 
	elif dice <=5:
		step = step + 1
	else:
		step = step + np.random.randint(1,7)

	