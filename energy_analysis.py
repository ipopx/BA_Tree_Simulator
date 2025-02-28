import numpy as np

def compute_energy_time_ratio(iterations: int, node_count: int, weight_function) -> list:
    """
    Runs multiple simulations and computes the energy/time ratio for each.
    
    Returns:
        list: A list of computed energy/time ratios from simulations.
    """
    from generate_trees import generate_barabasi_albert_tree  # Import tree generator
    ratio_statistics = []

    for _ in range(iterations):
        adjacency_matrix = generate_barabasi_albert_tree(node_count, weight_function)
        eigenvalues = np.linalg.eigvals(adjacency_matrix)
        energy = sum(abs(eigenvalues))
        ratio_statistics.append(energy / node_count)
    
    return ratio_statistics

def compute_energy_time_evolution(node_count: int, weight_function) -> list:
    """
    Computes the evolution of tree energy over time.
    
    Returns:
        list: Energy of the tree at each time step from 1 to node_count.
    """
    from generate_trees import generate_barabasi_albert_tree
    energy_evolution = []

    for t in range(2, node_count + 1):
        adjacency_matrix = generate_barabasi_albert_tree(t, weight_function)
        eigenvalues = np.linalg.eigvals(adjacency_matrix)
        energy = sum(abs(eigenvalues))
        energy_evolution.append(energy)
    
    return energy_evolution
