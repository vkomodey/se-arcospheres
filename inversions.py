import json
from arcobundle import Arcobundle

raw_inversions = json.load(open("./inversions.json"))


class Inversion:
    def __init__(self, input_bundle: Arcobundle, output_bundle: Arcobundle):
        self.input = input_bundle
        self.output = output_bundle

    def is_applicable(self, bundle: Arcobundle) -> bool:
        for symbol, quantity in self.input.quantities.items():
            if quantity > bundle.quantities[symbol]:
                return False

        return True
