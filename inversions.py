import json
from copy import copy
from arcobundle import Arcobundle
from arcosymbol import clean_symbols_map

raw_inversions = json.load(open("./inversions.json"))


class Inversion:
    def __init__(self, input_bundle: Arcobundle, output_bundle: Arcobundle):
        self.input = input_bundle
        self.output = output_bundle
        self.symbols_map = clean_symbols_map()
        for symbol in self.input.symbols:
            self.symbols_map[symbol] += 1


    def is_applicable(self, bundle: Arcobundle) -> bool:
        symbols = bundle.symbols
        symbols_map = copy(self.symbols_map)
        for