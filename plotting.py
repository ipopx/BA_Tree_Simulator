import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
from utils import path_graph_energy
import networkx as nx

def plot_ratios_histogram(ratio_statistics: list, iterations: int, node_count: int):
    """
    Plots a histogram of the energy/time ratio with a Gaussian fit.
    """
    mean_ratio = np.mean(ratio_statistics)
    std_dev_ratio = np.std(ratio_statistics)
    x_values = np.linspace(min(ratio_statistics), max(ratio_statistics), 100)
    gaussian_fit = stats.norm.pdf(x_values, mean_ratio, std_dev_ratio)
    
    plt.figure(figsize=(8, 5))
    plt.hist(ratio_statistics, bins=50, edgecolor='black', alpha=0.7, density=True, label="Histogram")
    plt.plot(x_values, gaussian_fit, 'r-', linewidth=2, label="Gaussian Fit")
    
    plt.xlabel("Energy/Time Ratio")
    plt.ylabel("Density")
    plt.title(f"Histogram (Iterations: {iterations}, Nodes: {node_count})")
    plt.legend()
    plt.show()

def plot_energy_evolution(energy_evolution: list, node_count: int):
    """
    Plots the evolution of tree energy over time.
    """
    time_steps = list(range(2, node_count + 1))
    star_energy = [2 * math.sqrt(n - 1) for n in time_steps]
    path_energy = [path_graph_energy(n) for n in time_steps]
    linear = [n for n in time_steps]

    plt.figure(figsize=(8, 5))
    plt.plot(time_steps, energy_evolution, label="Tree Energy", linewidth=2)
    plt.plot(time_steps, star_energy, linestyle='dashed', label="Star Graph Energy", linewidth=2)
    plt.plot(time_steps, path_energy, linestyle='dotted', label="Path Graph Energy", linewidth=2)
    plt.plot(time_steps, linear, linestyle='dotted', label="Linear", linewidth=2)
    
    plt.xlabel("Time (Number of Nodes)")
    plt.ylabel("Graph Energy")
    plt.title("Evolution of Tree Energy Over Time")
    plt.legend()
    plt.show()

def plot_eigenvalue_distribution(adjacency_matrix: np.ndarray):
    """
    Plots the eigenvalue distribution of a BA tree.
    """
    eigenvalues = np.linalg.eigvals(adjacency_matrix)
    
    plt.figure(figsize=(8, 5))
    plt.hist(eigenvalues, bins=50, edgecolor='black', alpha=0.7, density=True)
    plt.xlabel("Eigenvalue")
    plt.ylabel("Density")
    plt.title("Eigenvalue Distribution of BA Tree")
    plt.show()


def plot_tree_from_adjacency_matrix(adjacency_matrix: np.ndarray, title: str = "Barabási–Albert Tree"):
    """
    Plots a tree from its adjacency matrix using networkx.

    Parameters:
        adjacency_matrix (np.ndarray): The adjacency matrix of the tree.
        title (str): The title of the plot (default: "Barabási–Albert Tree").

    Returns:
        None
    """
    # Create a graph from the adjacency matrix
    G = nx.from_numpy_array(adjacency_matrix)

    # Use the spring layout for better visualization of tree structure
    pos = nx.spring_layout(G, seed=42)  # Fixed seed for consistent layout

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, node_size=50, with_labels=0, alpha=0.6, node_color="#40a6d1", edge_color="#52bced")

    # Add title
    plt.title(title)
    plt.show()

