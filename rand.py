import math

class ExpRand(object):

  def __init__(self, parameter, generator):
    self.parameter = parameter
    self.generator = generator

  def next(self):
    return -1 / self.parameter * math.log(self.generator.next())


class LCG(object):

  def __init__(self, a, m, seed):
    self.a = a
    self.m = m
    self.previous = seed

  def next(self):
    u = self.previous / self.m
    self.previous = (self.a * self.previous) % self.m
    return u

class Deterministic(object):

  def __init__(self, value):
    self.value = value

  def next(self):
    return self.value
