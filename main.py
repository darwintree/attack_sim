import math
import random
import pickle
import matplotlib.pyplot as plt
import numpy as np

def get_time(p):
	r = random.random()
	return -math.log(1-r)/p


def sim(attack_rate , z , trying_time = 10000):
	l = 1/10
	q = l * attack_rate
	p = l- q

	sum_of_catch_time = 0
	sum_of_block = 0

	for i in range(trying_time):
		p_block = z
		q_block = 0

		p_time = 0
		q_time = 0

		while p_block >= q_block:
			if p_time <= q_time:
				p_block += 1
				p_time += get_time(p)
			else:
				q_block += 1
				q_time += get_time(q)
			# print("p_time%f p_block%d\nq_time%f q_block%d"%(p_time, p_block, q_time, q_block))
		sum_of_catch_time += q_time
		sum_of_block += q_block
		# print("");

	return sum_of_catch_time/trying_time, sum_of_block/trying_time

def main():
	rates = [0.51, 0.53, 0.55, 0.57, 0.6, 0.65, 0.7, 0.75, 0.8]
	# zs = [6]
	zs = [5, 6, 8, 10, 15, 20, 25]
	d = {}

	for rate in rates:
		for z in zs:
			d[rate, z] = sim(rate,z)

	plt.xlabel("ATTACKING_RATE")
	plt.ylabel("BLOCKS_FOUND")
	print(d)
	for z in zs:
		plt.plot(rates, [d[rate, z][1] for rate in rates])

	plt.legend(zs)
	plt.show()

	# f = open("sim.dat", "wb")
	# pickle.dump(dict, f)
	# f.close

main()