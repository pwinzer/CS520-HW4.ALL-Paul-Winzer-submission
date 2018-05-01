import math
import random

def find_r_and_d(n):
	n2,d = n-1,n-1
	#d = n-1
	r = 0

	while (d/2) == (d/2.0):
		d /= 2
		r += 1
	
	print "n-1 = {} = 2^{} * {}".format(n2, r, d)

	return {'r':r, 'd':d}

def miller_test(n):
	
	if n < 3:
		print 'n is too small'
		return
	
	rd = find_r_and_d(n)

	a = random.randint(3, n)
	print 'a = {}'.format(a)

	for i in range(0,rd['r']):
		t = pow(a, rd['d']*pow(2,i))
		t %= n
		print 'a^(2^r)*d) mod n == {}'.format(t)
		if i >= 1 and t == n-1:
			return 'probably prime'
		elif i == 0 and t == 1:
			return 'probably prime'

	return 'composite'


def driver(n=97, k=5):
	
	comp = 0
	prime = 0

	for i in range(0,k):
		print 'i = {}'.format(i)
		result = miller_test(n)
		if result == 'probably prime':
			prime += 1
		elif result == 'composite':
			comp += 1

	print '{} iterations of miller test of {}'.format(k,n)
	print '{} found "probably prime" and {} found "composite"'.format(prime, comp)
	print 'More that one "composite" result means that {} is composite'.format(n)
	if comp > 0:
		print '{} is composite'.format(n)
	else:
		print 'There\'s a good change {} is prime'.format(n)
