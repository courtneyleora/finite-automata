
class DFA:
    """Simple deterministic finite automaton implementation."""

    def __init__(self, sigma, q=None):
        self.sigma = set(sigma)
        self.states = set(q) if q is not None else set()
        self.delta = {}
        self.start = None
        self.final = set()

    def add_state(self, s):
        self.states.add(s)
        self.delta.setdefault(s, {})

    def set_start(self, s):
        self.add_state(s)
        self.start = s

    def add_final(self, s):
        self.add_state(s)
        self.final.add(s)

    def set_finals(self, finals):
        for st in finals:
            self.add_final(st)

    def add_transition(self, f, c, t):
        self.add_state(f)
        self.add_state(t)
        if c != "" and c not in self.sigma:
            self.sigma.add(c)
        self.delta[f][c] = t

    def step(self, state, symbol):
        if state not in self.delta or symbol not in self.delta[state]:
            raise KeyError(f"No transition from {state} on {symbol}")
        return self.delta[state][symbol]

    def run(self, inp):
        if self.start is None:
            raise ValueError('Start state is not set')
        cur = self.start
        for ch in inp:
            cur = self.step(cur, ch)
        return cur

    def accepts(self, inp):
        try:
            return self.run(inp) in self.final
        except Exception:
            return False

    def transitions(self):
        out = []
        for f in sorted(self.delta.keys()):
            for c, t in sorted(self.delta[f].items()):
                out.append((f, c, t))
        return out

    def __str__(self):
        lines = [f'Sigma: {sorted(self.sigma)}', f'States: {sorted(self.states)}', f'Start: {self.start}', f'Finals: {sorted(self.final)}', 'Transitions:']
        for f, c, t in self.transitions():
            lines.append(f'  {f} --{c}--> {t}')
        return '\n'.join(lines)

    def __repr__(self):
        return f'DFA(start={self.start!r}, states={len(self.states)}, sigma={sorted(self.sigma)})'

