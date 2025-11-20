
class DFA:

  def __init__(self,sig,q=set()):
    self.sigma = sig
    self.states = q
    self.delta = {}
    self.start = None
    self.final = set()

  # getters and setters
  
  def set_start(self, state):
    """Set the start state of the DFA"""
    self.start = state
    self.add_state(state)
  
  def set_finals(self, finals):
    """Set the final/accepting states of the DFA"""
    if isinstance(finals, list):
      self.final = set(finals)
    else:
      self.final = {finals}
    for f in self.final:
      self.add_state(f)

  # add state s to DFA
  def add_state(self,s):
    """Add a state to the DFA's set of states"""
    self.states.add(s)

  # add transition (f,c,t) to DFA
  def add_transition(self,f,c,t):
    """Add a transition from state f on character c to state t"""
    self.add_state(f)
    self.add_state(t)
    if f not in self.delta:
      self.delta[f] = {}
    self.delta[f][c] = t
  
  def step(self, state, symbol):
    """Perform one step of the DFA: transition from state on symbol"""
    if state not in self.delta:
      raise Exception(f"No transitions from state '{state}'")
    if symbol not in self.delta[state]:
      raise Exception(f"No transition from state '{state}' on symbol '{symbol}'")
    return self.delta[state][symbol]
  
  def accepts(self, input_string):
    """Check if the DFA accepts the given input string"""
    current_state = self.start
    for symbol in input_string:
      current_state = self.step(current_state, symbol)
    return current_state in self.final

  # to String method
  def __str__(self):
    """String representation of the DFA"""
    result = "DFA:\n"
    result += f"  Alphabet: {self.sigma}\n"
    result += f"  States: {self.states}\n"
    result += f"  Start: {self.start}\n"
    result += f"  Final: {self.final}\n"
    result += f"  Transitions:\n"
    for state in self.delta:
      for symbol in self.delta[state]:
        result += f"    ({state}, {symbol}) -> {self.delta[state][symbol]}\n"
    return result

  # ...

class NFA:

  def __init__(self,sig,q=set()):
    self.sigma = sig
    self.states = q
    self.delta = []
    self.start = None
    self.final = None

  # getters and setters

  # add state s to NFA
  def add_state(self,s):
    pass

  # add transition (f,c,t) to NFA
  def add_transition(self,f,c,t):
    pass

  # to String method
  def __str__(self):
    pass

  # ...
