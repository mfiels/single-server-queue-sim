#!/usr/bin/env python3
import rand

# Paramters for the LCG
LCG_A = 16807
LCG_M = 2147483647

# Parameters for interarrival time generation
INTARR_SEED = 1806794933
INTARR_EXP_MEAN = 5

# Parameters for service time generation
SERVC_SEED = 1806794933
SERVC_EXP_MEAN = 4

if __name__ == '__main__':
  intarr_gen = rand.ExpRand(INTARR_EXP_MEAN, rand.LCG(LCG_A, LCG_M, INTARR_SEED))
  servc_gen = rand.ExpRand(SERVC_EXP_MEAN, rand.LCG(LCG_A, LCG_M, SERVC_SEED))
  for i in range(0, 10):
    print("interarrival = %f" % (intarr_gen.next()))
    print("service = %f" % (servc_gen.next()))