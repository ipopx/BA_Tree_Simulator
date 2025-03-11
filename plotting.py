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
    
    plt.figure(figsize=(9, 6))
    plt.hist(ratio_statistics, bins=50, edgecolor='#17becf', color='#17becf',alpha=0.7, density=True, label="Histogram")
    plt.plot(x_values, gaussian_fit, 'r-', linewidth=3, label="Gaussian Fit", color = '#1f77b4')
    
    plt.xlabel("Energy/Time Ratio", fontsize=18)
    plt.ylabel("Density", fontsize=18)
    plt.title(f"Histogram (Iterations: {iterations}, Nodes: {node_count})", fontsize=20)
    plt.legend(fontsize=16, loc="upper left", frameon=True, edgecolor='black')

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()


def plot_energy_evolution(energy_evolution: list, node_count: int):
    """
    Plots the evolution of tree energy over time.
    """
    time_steps = np.arange(2, node_count + 1)
    star_energy = [2 * math.sqrt(n - 1) for n in time_steps]
    path_energy = [path_graph_energy(n) for n in time_steps]
    linear = time_steps  
    colors = ['#1f77b4', '#17becf', '#2ca02c', '#6baed6', '#76c7c0']  

    plt.figure(figsize=(9, 6))
    plt.plot(time_steps, energy_evolution, label="Tree Energy", color=colors[2], linewidth=2.5)
    plt.plot(time_steps, star_energy, label="Star Graph Energy", color=colors[0], linewidth=2.5)
    plt.plot(time_steps, path_energy, label="Path Graph Energy", color=colors[3], linewidth=2.5)
    plt.plot(time_steps, linear, label="Linear Growth", color=colors[1], linewidth=2.5)

    plt.xlabel("Time (Number of Nodes)", fontsize=18)
    plt.ylabel("Graph Energy", fontsize=18)
    plt.title("Evolution of Tree Energy Over Time", fontsize=20)
    plt.legend(fontsize=16, loc="upper left", frameon=True, edgecolor='black')

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_scaled_energy_evolution(energy_evolution: list, node_count: int):
    """
    Plots the evolution of scaled tree energy over time.
    """
    time_steps = list(range(2, node_count + 1))
    star_energy = [2*np.sqrt(n-1)/n for n in time_steps]
    energy_evolution_scaled = [energy_evolution[n-2]/n for n in time_steps]

    plt.figure(figsize=(9, 6))
    plt.plot(time_steps, energy_evolution_scaled, label="Generated Tree", linewidth=2.5, color='#2ca02c')
    plt.plot(time_steps, star_energy, label="Star Graph", linewidth=2.5, color='#1f77b4')
    
    plt.xlabel("Time (Number of Nodes)",fontsize=18)
    plt.ylabel("Graph Energy/Sqrt(Time)",fontsize=18)
    plt.title("Scaled evolution of Tree Energy Over Time",fontsize=20)
    plt.legend(fontsize=16, loc="upper left", frameon=True, edgecolor='black')

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_eigenvalue_distribution(adjacency_matrix: np.ndarray):
    """
    Plots the eigenvalue distribution of a BA tree.
    """
    eigenvalues = np.linalg.eigvals(adjacency_matrix)
    
    plt.figure(figsize=(8, 5))
    plt.hist(eigenvalues, bins=100, edgecolor='#17becf', color='#17becf', alpha=0.7, density=True)

    plt.xlabel("Eigenvalue", fontsize=18)
    plt.ylabel("Density", fontsize=18)
    plt.title("Eigenvalue Distribution of BA Tree", fontsize=20)

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

def plot_averaged_eigenvalue_distribution(total_eigenvalues):
    """
    Plots the averaged eigenvalue distribution of multiple simulations of BA trees.
    """
    
    plt.figure(figsize=(8, 5))
    plt.hist(total_eigenvalues, bins=100, edgecolor='#17becf', color='#17becf', alpha=0.7, density=True)
    plt.xlabel("Eigenvalue", fontsize=18)
    plt.ylabel("Density", fontsize=18)
    plt.title("Eigenvalue Distribution of BA Tree", fontsize=20)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()


def plot_tree_from_adjacency_matrix(adjacency_matrix: np.ndarray, title: str = "Barabási–Albert Tree"):
    """
    Plots a tree from its adjacency matrix using networkx.
    """
    G = nx.from_numpy_array(adjacency_matrix)
    pos = nx.spring_layout(G, seed=42)  
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, node_size=50, with_labels=0, alpha=0.6, node_color='#2ca02c', edge_color='#2ca02c')

    plt.title(title)
    plt.show()

