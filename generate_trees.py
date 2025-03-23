import numpy as np
import random
from collections import deque

from plotting import plot_tree_from_adjacency_matrix

def generate_barabasi_albert_tree(node_count: int, weight_function) -> np.ndarray:
    """
    Generates a tree using the Barabási–Albert model with
    a custom weight function for preferential attachment.
 
    Parameters:
        node_count (int): Number of nodes in the tree.
        weight_function (function): A function defining the attachment probability.

    Returns:
        np.ndarray: Adjacency matrix of the generated tree.
    """
    vertices = [0, 1]
    degrees = [1, 1]
    adjacency_matrix = np.zeros((node_count, node_count), dtype=int)
    adjacency_matrix[0, 1] = adjacency_matrix[1, 0] = 1
    attachment_probabilities = [weight_function(deg) for deg in degrees]

    for t in range(2, node_count):
        selected_vertex = random.choices(vertices, weights=attachment_probabilities)[0]
        
        vertices.append(t)
        degrees.append(1)
        degrees[selected_vertex] += 1
        
        attachment_probabilities[selected_vertex] = weight_function(degrees[selected_vertex])
        attachment_probabilities.append(weight_function(degrees[-1]))
        
        adjacency_matrix[t, selected_vertex] = adjacency_matrix[selected_vertex, t] = 1
    
    return adjacency_matrix

def generate_tree_and_compute_energy(node_count: int, weight_function) -> list:
    """
    Generates a Barabási–Albert tree and computes its energy at each step.
    
    Parameters:
        node_count (int): Total number of nodes in the tree.
        weight_function (function): Function defining the attachment probability.

    Returns:
        list: Energy of the tree at each time step from 2 to node_count.
    """
    vertices = [0, 1]
    degrees = [1, 1]
    adjacency_matrix = np.zeros((node_count, node_count), dtype=int)
    adjacency_matrix[0, 1] = adjacency_matrix[1, 0] = 1
    attachment_probabilities = [weight_function(deg) for deg in degrees]
    energy_evolution = []
    eigenvalues = np.linalg.eigvals(adjacency_matrix[:2, :2])
    energy_evolution.append(sum(abs(eigenvalues)))

    for t in range(2, node_count):
        selected_vertex = random.choices(vertices, weights=attachment_probabilities)[0]
        vertices.append(t)
        degrees.append(1)
        degrees[selected_vertex] += 1
        
        attachment_probabilities[selected_vertex] = weight_function(degrees[selected_vertex])
        attachment_probabilities.append(weight_function(degrees[-1]))
        adjacency_matrix[t, selected_vertex] = adjacency_matrix[selected_vertex, t] = 1

        eigenvalues = np.linalg.eigvals(adjacency_matrix[:t+1, :t+1])
        energy_evolution.append(sum(abs(eigenvalues)))

    plot_tree_from_adjacency_matrix(adjacency_matrix)
    return energy_evolution

def generate_random_recursive_tree(node_count: int) -> np.ndarray:
    """
    Generates a random recursive tree (Barabási–Albert model with α = 0).
    
    Parameters:
        node_count (int): Number of nodes in the tree.

    Returns:
        np.ndarray: Adjacency matrix of the generated tree.
    """
    adjacency_matrix = np.zeros((node_count, node_count), dtype=int)
    
    for t in range(1, node_count):
        selected_vertex = random.randint(0, t - 1)  # Pick a random existing node
        
        adjacency_matrix[t, selected_vertex] = adjacency_matrix[selected_vertex, t] = 1

    return adjacency_matrix

def generate_multiple_trees(nr_iterations, node_count, weight_function):
    """
    Generates multiple Barabási–Albert (BA) trees and returns the accumulated list of eigenvalues.
    
    Parameters:
        nr_iterations (int): Number of trees to generate.
        node_count (int): Number of nodes in each tree.
        weight_function (function): A function defining the attachment kernel for preferential attachment.

    Returns:
        list: A list containing all eigenvalues from the generated trees.
    """
    
    total_eigenvalues = np.array([])
    for _ in range(nr_iterations):
        adjacency_matrix = generate_barabasi_albert_tree(node_count, weight_function)
        eigenvalues = np.linalg.eigvals(adjacency_matrix)
        total_eigenvalues = np.concatenate((total_eigenvalues, eigenvalues))
    return total_eigenvalues