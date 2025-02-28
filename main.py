import time
from config import iterations, node_count, alpha, delta, weight, mode
from generate_trees import generate_barabasi_albert_tree
from utils import power_weight_function, affine_weight_function
from energy_analysis import *
from plotting import *

def main():
    """Main function to run the simulation and plot results."""
    
    if weight == 'power':
        weight_function = lambda d: power_weight_function(d, alpha)
    else:
        weight_function = lambda d: affine_weight_function(d, delta)
    
    if mode == 'energy time ratio':
        start_time = time.time()
        ratio_statistics = compute_energy_time_ratio(iterations, node_count, weight_function)
        elapsed_time = time.time() - start_time
        
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
        plot_ratios_histogram(ratio_statistics, iterations, node_count)

    elif mode == 'energy evolution':
        energy_evolution = compute_energy_time_evolution(node_count, weight_function)
        plot_energy_evolution(energy_evolution, node_count)

    elif mode == 'eigenvalues':
        adjacency_matrix = generate_barabasi_albert_tree(node_count, weight_function)
        plot_eigenvalue_distribution(adjacency_matrix)

    elif mode == 'drawing':
        adjacency_matrix = generate_barabasi_albert_tree(node_count, weight_function)
        plot_tree_from_adjacency_matrix(adjacency_matrix)

if __name__ == "__main__":
    main()
