import numpy as np
import random
from collections import deque

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


def roll_bucket(
    buckets: dict[int, list[int]], 
    total_edges: int, 
    total_sum: int, 
    weight_function
):
    """
    Selects a node from `buckets` based on degree-based preferential attachment.

    Uses a random integer to determine selection and updates `buckets` accordingly.

    Parameters:
        buckets (dict[int, list[int]]): Dictionary where keys are degrees and values are lists of node IDs.
        total_edges (int): Total number of edges in the current tree.
        total_sum (int): Sum of all weighted degrees in the tree.
        weight_function (function): Function defining how attachment probability scales with degree.

    Returns:
        tuple[int | None, int]: Selected node ID and updated total sum. 
                                Returns (None, total_sum) if no node is selected.
    """
    S_n = total_sum  
    sigma = 0  
    r = random.randint(1, S_n)

    for degree, node_list in buckets.items():
        deg_Bi = weight_function(degree) * len(node_list)  

        if sigma + deg_Bi >= r:
            r_prime = random.randint(0, len(node_list) - 1)  
            v_k = node_list.pop(r_prime)  # Remove selected node
            
            # Move the node to the next degree bucket
            if degree + 1 in buckets:
                buckets[degree + 1].append(v_k)
            else:
                buckets[degree + 1] = [v_k]

            # Update total sum
            new_total_sum = S_n - weight_function(degree) + weight_function(degree + 1) + weight_function(1)
            
            return v_k, new_total_sum
        
        sigma += deg_Bi


def roll_barabasi_albert_tree(node_count: int, weight_function) -> np.ndarray:
    """
    Generates a tree using the "rolling bucket" preferential attachment method.

    This implementation maintains a dictionary (`buckets`) of nodes grouped by degree,
    ensuring efficient selection.

    Parameters:
        node_count (int): Number of nodes in the tree.
        weight_function (function): Function defining the attachment probability.

    Returns:
        np.ndarray: Adjacency matrix of the generated tree.
    """
    adjacency_matrix = np.zeros((node_count, node_count), dtype=int)
    buckets = {1: [0]}  # Initial bucket with one node (node 0)
    total_edges = 1
    total_sum = weight_function(1)
    
    for new_node in range(1, node_count):
        selected_node, total_sum = roll_bucket(buckets, total_edges, total_sum, weight_function)
        
        if selected_node is not None:
            # Add edge in adjacency matrix
            adjacency_matrix[new_node][selected_node] = 1
            adjacency_matrix[selected_node][new_node] = 1
            
            # Add new node to the degree-1 bucket
            if 1 in buckets:
                buckets[1].append(new_node)
            else:
                buckets[1] = [new_node]
            
            total_edges += 1
    
    return adjacency_matrix
