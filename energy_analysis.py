import numpy as np
from generate_trees import generate_barabasi_albert_tree, generate_random_recursive_tree

def compute_energy_time_ratio(iterations: int, node_count: int, weight_function) -> list:
    """
    Runs multiple simulations and computes the energy/time ratio for each.
    
    Returns:
        list: A list of computed energy/time ratios from simulations.
    """
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
    energy_evolution = []

    for t in range(2, node_count + 1):
        adjacency_matrix = generate_barabasi_albert_tree(t, weight_function)
        eigenvalues = np.linalg.eigvals(adjacency_matrix)
        energy = sum(abs(eigenvalues))
        energy_evolution.append(energy)
    
    return energy_evolution

def compute_lower_bound_approximation(nodes=100, nr_iterations=1000):
    """
    Estimates a lower bound approximation for the energy of random recursive trees.
    
    Parameters:
        nodes (int, optional): Number of nodes in the tree. Default is 100.
        nr_iterations (int, optional): Number of Monte Carlo iterations. Default is 1000.

    Returns:
        float: Approximated lower bound for the tree energy.
    """
    bins = [(0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0), (1.0, 1.2), (1.2, 1.4),
        (1.4, 1.6), (1.6, 1.8), (1.8, 2.0), (2.0, 2.2), (2.2, 2.4), (2.4, 2.6),
        (2.6, 2.8), (2.8, 3.0), (3.0, 3.2), (3.2, 3.4), (3.4, 3.6), (3.6, 3.8),
        (3.8, 4.0), (4.0, np.inf)]
    coefficients = [b[0] for b in bins]

    sum_counts = {b: np.zeros(nodes) for b in bins}

    for _ in range(nr_iterations):
        for k in range(2, nodes):
            adjacency_matrix = generate_random_recursive_tree(k)
            eigenvalues = np.linalg.eigvals(adjacency_matrix)
            removed_root_eigenvalues = np.linalg.eigvals(adjacency_matrix[1:, 1:])

            for b in bins:
                sum_counts[b][k] += (
                    np.sum((eigenvalues >= b[0]) & (eigenvalues < b[1])) -
                    np.sum((removed_root_eigenvalues >= b[0]) & (removed_root_eigenvalues < b[1]))
                )

    expectation_counts = {b: sum_counts[b] / nr_iterations for b in bins}

    final_means = {
        b: np.sum([expectation_counts[b][k] / (k * (k + 1)) for k in range(2, nodes)])
        for b in bins
    }

    return 2 * sum(coeff * final_means[b] for coeff, b in zip(coefficients, bins))

