# import sys library
import sys
# import likelihood weighting script
import weightEstimation

def main():
	#fetch arguments
	m = sys.argv[1]
	n = sys.argv[2]
	# call likelihood script with estimations (m) and repetition (n)
	weightEstimation.main(m, n)

if __name__ == "__main__":
    main()