import re

class DFA:
    def __init__(self, pattern):
        self.pattern = re.compile(f"^{pattern}$")

    def accepts(self, string):
        return bool(self.pattern.match(string))

def regex_to_dfa(regex: str) -> DFA:
    return DFA(regex)

assert regex_to_dfa("(a|b)*abb").accepts("aabb") == True
assert regex_to_dfa("(a|b)*abb").accepts("ababa") == False
