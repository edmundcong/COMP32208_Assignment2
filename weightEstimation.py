import random
import sys

def randomise(prob):
	r = random.random()
	if r <= prob:
		return True
	return False

def create_sample():
	#clouds, sprinkler, rain, wet_grass
	weighting = 1.0

	# since S and W are evidence, fix them to 1
	sprinkler = True
	wet_grass = True

	clouds = randomise(.50)
	# if clouds is true then 
	# sprinkler will take on the weighting of 0.1. sprinkler always true.
	# not constrained to a predefined value in rain
	if clouds and sprinkler: 
		weighting *= .1 #visit s with c
		rain = randomise(.80) # < 0.8, 0.2 >, visit r with c
	else:
		weighting *= .5 #visit s with !c
		rain = randomise(.20) #visit r with !c 

	if sprinkler and rain: 
		weighting *= .99
	elif sprinkler and not rain:
		weighting *= .90
	elif rain and not sprinkler:
		weighting *= .90
	else:
		weighting *= 0

	return {"clouds": clouds, "sprinkler": sprinkler, "rain": rain, "wet_grass":wet_grass, "weighting":weighting}


def run(n_samples):
	positive = 0.0
	allSamples = 0.0
	for i in xrange(n_samples): #calculate sample n times
		x = create_sample()
		if x['clouds']:
			positive += x['weighting']
		allSamples += x['weighting']
	return float(positive/allSamples)

# calculate mean
def mean(sum_runs):
	mean = 0.0
	n = len(sum_runs)
	for i in xrange(n):
		mean += sum_runs[i]
	return mean/n

# calculate variance
def variance(sum_runs, mean):
	variance = 0.0
	n = len(sum_runs)
	totalDiffSquared = 0.0
	for i in xrange(n):
		difference = sum_runs[i] - mean
		totalDiffSquared += difference*difference
	return totalDiffSquared/n

def main(m, n):
	sum_runs = []

	for i in xrange(int(m)):
		sum_runs.append(run(int(n)))
	
	networkMean = mean(sum_runs) 
	networkVariance = variance(sum_runs, networkMean)
	print format(networkMean, '.6f'), format(networkVariance, '.6f')

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])


