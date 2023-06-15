from typing import List
from arcosymbol import Arcosymbol, clean_symbols_map


class Arcobundle:
    """
    This is a list of arcospheres which is used in recipies
    List might contain duplicates
    """
    def __init__(self, symbols: List[Arcosymbol]):
        self.symbols = sorted(symbols)
        self.quantities = clean_symbols_map()
        for symbol in self.symbols:
            self.quantities[symbol] += 1

    def __eq__(self, other):
        if len(self.symbols) != len(other.symbols):
            return False

        for i, symbol in enumerate(self.symbols):
            if symbol != other.symbols[i]:
                return False

        return True