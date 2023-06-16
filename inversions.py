from arcobundle import Arcobundle


class Inversion:
    def __init__(self, input_bundle: Arcobundle, output_bundle: Arcobundle):
        self.input = input_bundle
        self.output = output_bundle
        self.inversion_pairs = zip(self.input.symbols, self.output.symbols)

    def is_applicable(self, bundle: Arcobundle) -> bool:
        for symbol, quantity in self.input.quantities.items():
            if quantity > bundle.quantities[symbol]:
                return False

        return True

    def apply(self, bundle: Arcobundle) -> Arcobundle:
        inversed_bundle = bundle
        for symbol_from, symbol_to in self.inversion_pairs:
            inversed_bundle = inversed_bundle.replace(symbol_from, symbol_to)

        return inversed_bundle
