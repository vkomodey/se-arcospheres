from enum import IntEnum, auto


class Arcosymbol(IntEnum):
    LAMBDA = auto()
    ZETA = auto()
    EPSILON = auto()
    GAMMA = auto()
    KSI = auto()
    THETA = auto()
    PHI = auto()
    OMEGA = auto()


def clean_symbols_map():
    result = {}
    for symbol in Arcosymbol:
        result[symbol] = 0
    return result


def to_symbol(s: str) -> Arcosymbol:
    match s:
        case "lambda":
            return Arcosymbol.LAMBDA
        case "zeta":
            return Arcosymbol.ZETA
        case "epsilon":
            return Arcosymbol.EPSILON
        case "gamma":
            return Arcosymbol.GAMMA
        case "ksi":
            return Arcosymbol.KSI
        case "theta":
            return Arcosymbol.THETA
        case "phi":
            return Arcosymbol.PHI
        case "omega":
            return Arcosymbol.OMEGA
    raise ValueError(f"Arcosymbol {s} is unknown")