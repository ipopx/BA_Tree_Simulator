import time
from config import iterations, node_count, alpha, delta, weight, mode
from generate_trees import *
from utils import *
from energy_analysis import *
from plotting import *

def main():
    """Main function to run the simulation and plot results."""
    
    # Select the appropriate weight function
    if weight == 'power':
        weight_function = lambda d: power_weight_function(d, alpha)
    else:
        weight_function = lambda d: affine_weight_function(d, delta)

    mode_actions = {
        Mode.ENERGY_TIME_RATIO: lambda: run_energy_time_ratio(weight_function),
        Mode.ENERGY_EVOLUTION: lambda: run_energy_evolution(weight_function),
        Mode.SCALED_ENERGY_EVOLUTION: lambda: run_scaled_energy_evolution(weight_function),
        Mode.EIGENVALUES: lambda: run_eigenvalues(weight_function),
        Mode.AVERAGED_EIGENVALUES: lambda: run_averaged_eigenvalues(weight_function),
        Mode.DRAWING: lambda: run_tree_drawing(weight_function),
        Mode.ENERGY_RANDOM_RECURSIVE_TREES: lambda: run_energy_random_recursive_trees()
    }

    # Run the selected mode or show an error message
    if mode in mode_actions:
        mode_actions[mode]()
    else:
        print(f"Error: Invalid mode '{mode}'. Please choose from: {', '.join(mode_actions.keys())}")

def run_energy_time_ratio(weight_function):
    """Computes and plots the energy-time ratio."""
    start_time = time.time()
    ratio_statistics = compute_energy_time_ratio(iterations, node_count, weight_function)
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    plot_ratios_histogram(ratio_statistics, iterations, node_count)

def run_energy_evolution(weight_function):
    """Generates tree energy evolution and plots it."""
    energy_evolution = generate_tree_and_compute_energy(node_count, weight_function)
    plot_energy_evolution(energy_evolution, node_count)

def run_scaled_energy_evolution(weight_function):
    """Generates and plots scaled energy evolution."""
    energy_evolution = generate_tree_and_compute_energy(node_count, weight_function)
    plot_scaled_energy_evolution(energy_evolution, node_count)

def run_eigenvalues(weight_function):
    """Generates a tree and plots its eigenvalue distribution."""
    adjacency_matrix = generate_barabasi_albert_tree(node_count, weight_function)
    plot_eigenvalue_distribution(adjacency_matrix)

def run_averaged_eigenvalues(weight_function):
    """Generates multiple trees and plots the averaged eigenvalue distribution."""
    eigenvalues = generate_multiple_trees(iterations, node_count, weight_function)
    plot_averaged_eigenvalue_distribution(eigenvalues)

def run_tree_drawing(weight_function):
    """Generates a tree and plots its structure."""
    adjacency_matrix = generate_barabasi_albert_tree(node_count, weight_function)
    plot_tree_from_adjacency_matrix(adjacency_matrix)

def run_energy_random_recursive_trees():
    """Computes and prints the energy expectation for random recursive trees."""
    energy_expectation = compute_lower_bound_approximation()
    print(energy_expectation)

if __name__ == "__main__":
    main()
