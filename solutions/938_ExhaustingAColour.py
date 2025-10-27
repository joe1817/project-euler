'''
Joe Walter

difficulty: 5%
run time:   0:16
answer:     0.2928967987

	***

938 Exhausting a Colour

A deck of cards contains R red cards and B black cards.
A card is chosen uniformly randomly from the deck and removed. A second card is then chosen uniformly randomly from the cards remaining and removed.

    - If both cards are red, they are discarded.
    - If both cards are black, they are both put back in the deck.
    - If they are different colours, the red card is put back in the deck and the black card is discarded.

Play ends when all the remaining cards in the deck are the same colour and let P(R,B) be the probability that this colour is black.

You are given P(2, 2) = 0.4666666667, P(10, 9) = 0.4118903397, and P(34, 25) = 0.3665688069.

Find P(24690, 12345). Give your answer with 10 digits after the decimal point.
'''

from functools import cache

def P(R, B):
	arr = [0] + [1] * (B)
	for r in range(2, R+1, 2):
		prob_red  = r*(r-1)//2
		for b in range(1, B+1):
			prob_diff = r*b
			prob_black_removed = prob_diff / (prob_diff + prob_red)
			arr[b] = arr[b-1]*prob_black_removed + arr[b]*(1-prob_black_removed)
			#arr[b] = (arr[b-1]*2*b + arr[b]*(r-1))/(2*b+r-1)
	return f"{arr[B]:.10f}"


assert P(2, 2)   == "0.4666666667"
assert P(10, 9)  == "0.4118903397"
assert P(34, 25) == "0.3665688069"

print(P(24690, 12345))

"""
# testing
def diff(n, order=2, _diffs=[None]):
	for i in range(order):
		if _diffs[i] is None:
			_diffs[i] = n
			_diffs.append(None)
			break
		else:
			_diffs[i], n = n, n-_diffs[i]
	return _diffs
"""