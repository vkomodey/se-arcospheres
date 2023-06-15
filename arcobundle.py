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

    def replace(self, symbol_from: Arcosymbol, symbol_to: Arcosymbol):
        idx = self.symbols.index(symbol_from)
        new_list = self.symbols[:idx]
        new_list.append(symbol_to)
        new_list.extend(self.symbols[idx+1:])

        return Arcobundle(new_list)

    def __repr__(self):
        return str(self.symbols)

