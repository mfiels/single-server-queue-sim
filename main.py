#!/usr/bin/env python3
import rand
import sim

# Paramters for the LCG
LCG_A = 16807
LCG_M = 2147483647

# Parameters for interarrival time generation
INTARR_SEED = 1806794933
INTARR_EXP_MEAN = 5

# Parameters for service time generation
SERVC_SEED = 1806794933
SERVC_EXP_MEAN = 4

# Parameters for stopping conditions
SIM_TIME_LIMIT = 10
SIM_COMPLETIONS_LIMIT = 10

def time_stop_cond(simulation):
  return simulation.clock >= SIM_TIME_LIMIT

def completions_stop_cond(simulation):
  return simulation.completions >= SIM_COMPLETIONS_LIMIT

def run_sim(intarr_gen, servc_gen, stop_cond):
  simulation = sim.SingleServerQueueSimulation(intarr_gen, servc_gen, stop_cond)
  simulation.simulate()

if __name__ == '__main__':
  print("***")
  print("* Running M/M/1 for stopping condition of %d hours" % SIM_TIME_LIMIT)
  print("***")
  run_sim(
    rand.ExpRand(INTARR_EXP_MEAN, rand.LCG(LCG_A, LCG_M, INTARR_SEED)), 
    rand.ExpRand(SERVC_EXP_MEAN, rand.LCG(LCG_A, LCG_M, SERVC_SEED)), 
    time_stop_cond)

  print("***")
  print("* Running M/M/1 for stopping condition of %d completions" % SIM_COMPLETIONS_LIMIT)
  print("***")
  run_sim(
    rand.ExpRand(INTARR_EXP_MEAN, rand.LCG(LCG_A, LCG_M, INTARR_SEED)), 
    rand.ExpRand(SERVC_EXP_MEAN, rand.LCG(LCG_A, LCG_M, SERVC_SEED)), 
    completions_stop_cond)

  print("***")
  print("* Running M/D/1 for stopping condition of %d hours" % SIM_TIME_LIMIT)
  print("***")
  run_sim(
    rand.ExpRand(INTARR_EXP_MEAN, rand.LCG(LCG_A, LCG_M, INTARR_SEED)), 
    rand.Deterministic(SERVC_EXP_MEAN),
    time_stop_cond)

  print("***")
  print("* Running M/D/1 for stopping condition of %d hours" % SIM_COMPLETIONS_LIMIT)
  print("***")
  run_sim(
    rand.ExpRand(INTARR_EXP_MEAN, rand.LCG(LCG_A, LCG_M, INTARR_SEED)), 
    rand.Deterministic(SERVC_EXP_MEAN),
    completions_stop_cond)
