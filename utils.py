import math

def power_weight_function(degree: int, alpha: float) -> float:
    """Returns the weight of a given degree using a power function w(d) = d^alpha."""
    return math.pow(degree, alpha) if degree > 0 else 1.0

def affine_weight_function(degree: int, delta: float) -> float:
    """Returns the weight of a given degree using an affine function w(d) = d + delta."""
    return degree + delta

def path_graph_energy(n: int) -> float:
    """
    Computes the energy of a path graph P_n.
    
    """
    if n % 2 == 0:
        return (2 / math.sin(math.pi / (2 * (n + 1)))) - 2
    else:
        return (2 * math.cos(math.pi / (2 * (n + 1))) / math.sin(math.pi / (2 * (n + 1)))) - 2

