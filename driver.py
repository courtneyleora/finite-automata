from FAParser import parser
from FA import DFA
from itertools import product
import sys

# generate all strings on an alphabet upto length m-1
def atm(sig, m) :

    result = []
    for i in range(m) :
        for string in product(sig, repeat = i) :
            result.append(''.join(string))

    return result

# parse info from FA encoding and display it

data = open('even.dfa').read()
start, finals, transitions = parser.parse(data)

print('start:', start)
print('finals:', finals)
print('transitions:', transitions)

# build DFA with this info

sig = set(t[1] for t in transitions) # obtain alphabet
print('alphabet:', sig)

dfa = DFA(sig,set()) # build DFA from alphabet, etc...

# populate DFA with parsed info
dfa.set_start(start)
dfa.set_finals(finals)
for (f,c,t) in transitions:
    dfa.add_transition(f,c,t)

# helper: one-step transition on a configuration (state, remaining_string)
def step_config(dfa, config):
    state, rem = config
    # print current configuration like ('even', "ababb")
    print((state, rem))
    if rem == "":
        return (state, rem)
    symbol = rem[0]
    try:
        next_state = dfa.step(state, symbol)
    except Exception as e:
        # if transition missing, print error and return unchanged
        print('No transition:', e)
        return (state, rem)
    return (next_state, rem[1:])

# helper: run step_config in a loop until input consumed
def show_run_steps(dfa, start_state, input_string):
    cfg = (start_state, input_string)
    # step_config prints each configuration; call it repeatedly until input consumed
    while True:
        cfg = step_config(dfa, cfg)
        state, rem = cfg
        if rem == "":
            break


# c) acceptance using the stepping function
def accepts_via_steps(dfa, start_state, input_string):
    cfg = (start_state, input_string)
    while True:
        state, rem = cfg
        if rem == "":
            return state in dfa.final
        # perform one step without printing
        symbol = rem[0]
        try:
            next_state = dfa.step(state, symbol)
        except Exception:
            return False
        cfg = (next_state, rem[1:])

# generate all strings on the alphabet upto length 4 and print them

at5 = atm(sig, 5)
print(at5)


print('\nStep-by-step run for input "ababb":')
show_run_steps(dfa, start, 'ababb')


print('\nAcceptance results for all strings up to length 4:')
for s in atm(sig, 5):
    # print quoted string like "" True
    print(f'"{s}"', accepts_via_steps(dfa, start, s))

# interactive prompt: enter string and show step-by-step run
if len(sys.argv) > 1:
    s = sys.argv[1]
    print("Running on:", s)
    show_run_steps(dfa, start, s)
    print("Accepted?", accepts_via_steps(dfa, start, s))
else:
    # fall back to interactive prompt
    s = input("Enter input string (or blank for none): ")
    if s != "":
        show_run_steps(dfa, start, s)
        print("Accepted?", accepts_via_steps(dfa, start, s))
