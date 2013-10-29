import sys

class SingleServerQueueSimulation(object):
  
  def __init__(self, intarr_gen, servc_gen, stop_cond):
    self.intarr_gen = intarr_gen
    self.servc_gen = servc_gen
    self.stop_cond = stop_cond

    self.arrival_event = Event(intarr_gen.next(), self.handle_arrival)
    self.departure_event = Event(sys.maxsize, self.handle_departure)
    self.next_event = self.arrival_event

    self.queue_size = 0
    self.clock = self.next_event.time
    self.occupied = False
    self.completions = 0

  def simulate(self):
    while not self.stop_cond(self):
      self.next_event.handler()
      self.next_event = min(self.arrival_event, self.departure_event)
      self.clock = self.next_event.time

  def handle_arrival(self):
    print("Handling arrival at time %f" % self.clock)
    if self.occupied:
      self.queue_size = self.queue_size + 1
    else:
      self.occupied = True
      self.departure_event = Event(self.clock + self.servc_gen.next(), self.handle_departure)
    self.arrival_event = Event(self.clock + self.intarr_gen.next(), self.handle_arrival)

  def handle_departure(self):
    print("Handling departure at time %f" % self.clock)
    self.occupied = False
    self.completions = self.completions + 1
    if self.queue_size > 0:
      self.queue_size = self.queue_size - 1
      self.occupied = True
      self.departure_event = Event(self.clock + self.servc_gen.next(), self.handle_departure)
    else:
      self.departure_event = Event(sys.maxsize, self.handle_departure)

class Event(object):

  def __init__(self, time, handler):
    self.time = time
    self.handler = handler

  def __lt__(self, other):
    return self.time < other.time

  def __le__(self, other):
    return self.time <= other.time

  def __eq__(self, other):
    return self.time == other.time

  def __ge__(self, other):
    return self.time >= other.time

  def __gt__(self, other):
    return self.time > other.time

  def __ne__(self, other):
    return self.time != other.time
