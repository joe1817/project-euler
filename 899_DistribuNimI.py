'''
Joe Walter

difficulty: 15%
run time:   0:00
answer:     10784223938983273

	***

899 DistribuNim I

Two players play a game with two piles of stones. The players alternately take stones from one or both piles, subject to:

    1. the total number of stones taken is equal to the size of the smallest pile before the move;
    2. the move cannot take all the stones from a pile.

The player that is unable to move loses.

Let L(n) be the number of ordered pairs (a,b) with 1<=a,b<=n such that the initial game position with piles of sizes a and b is losing for the first player assuming optimal play.

You are given L(7)=21 and L(7**2)=221.

Find L(7**17).

	***

1,even = win
1,odd = lose
even,even = win
2,4k+1 = win
2,4k+3 = lose
x>1,4k+1 = win
4,4k+3, k even = win, k odd = lose

Given a <= b, the pair a,b *may* lose for player 1 only if [a=1 and b is odd] or [b=4k+3]
'''

from functools import cache
from math import floor, log

from random import randint

def val(a, b):
	if b < a:
		a, b = b, a
	return _val(a, b)

@cache
def _val(a, b):
	if a == 1 and b == 1:
		return False
	move = min(a, b)
	for i in range(move+1):
		if a-i > 0 and b - (move-i) > 0:
			if val(a-i, b - (move-i)) == False:
				return True
	return False

'''
n = 45
a = 35
print(f"{a=}")
for b in range(1, n+1):
	#print(f"{str(b).zfill(2)}: {"" if val(a, b) else "L"}")
	print(f"{str(b).zfill(2)}: {"" if val(a, b) else "L"}")
	if b >= a:
		print(f"{str(b).zfill(2)}: {"" if val(a, b) else "L"}")
	else:
		print(f"{str(b).zfill(2)}: -")
losses_for_a = (n+1) // (4 * 2**(floor(log(a, 2))-1))
print(losses_for_a)
'''

def test():
	for _ in range(100):
		a = randint(1,100)
		n = randint(1,100)
		if a > n:
			a,n = n,a
		count = 0
		for b in range(a, n+1):
			if not val(a,b):
				count += 1

		losses_for_a = (n+1) // (4 * 2**(floor(log(a, 2))-1))
		assert count == losses_for_a, f"{n=}, {a=}, {count=}, {losses_for_a=}"
test()



def L(n):
	if n == 1:
		return 1

	# count 1,odd and odd,1
	count = ((n-1)//2) * 2 + 1
	#print(f"** {count}")

	# count for a >= 2
	p = 1
	while True:
		rep = 2**p # representative 'a' for this class

		losses_for_rep = (n+1) // (4 * 2**(floor(log(rep, 2))-1))
		class_size = min(2**(p+1), n+1) - rep
		# account for swapping a,b
		count += 2 * losses_for_rep * class_size

		if rep >= n:
			break
		p += 1

	# account for the cases where a = b = 4k+3 and a loss
	a = 4
	while a-1 <= n:
		count -= 1
		a *= 2

	return count

assert L(7) == 21
assert L(7**2) == 221

print(L(7**17))
