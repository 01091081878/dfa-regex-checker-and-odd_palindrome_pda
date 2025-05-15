from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.regex.regex import Regex

class RegexToDFA:
    def __init__(self, regex_str: str):
        self.regex_str = regex_str
        self.dfa = self.regex_to_dfa(regex_str)
        
    def regex_to_dfa(self, regex_str: str) -> DFA:
        regex_obj = Regex(regex_str)
        nfa = regex_obj.to_epsilon_nfa()
        dfa = DFA.from_nfa(nfa)
        return dfa
    
    def accepts(self, string: str) -> bool:
        return self.dfa.accepts_input(string)
