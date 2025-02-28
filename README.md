# Barabási–Albert Tree Model Simulation 🌳

This project simulates **random trees** using the **Barabási–Albert preferential attachment model** and analyzes their properties. It generates trees, computes their energy statistics, and visualizes their structure.

---

## 📌 Features
✅ Generate **Barabási–Albert Trees** using two different methods:
   - Standard preferential attachment (`generate_barabasi_albert_tree`)
   - Optimized bucket-based selection (`roll_barabasi_albert_tree`)

✅ Compute and analyze:
   - **Graph energy** and its evolution
   - **Eigenvalue distributions**
   - **Energy/time ratio statistics**

✅ Visualize:
   - **Tree structures** with `networkx`
   - **Histograms of energy ratios**
   - **Eigenvalue distributions**
   - **Energy evolution over time**

---

## 🚀 Installation
To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

This installs:
- `numpy`
- `matplotlib`
- `networkx`
- `scipy`
- `sortedcontainers`

---

## 📂 Project Structure
```
📂 BA_Tree_Simulation/
│── main.py                  # Runs the full simulation
│── generate_trees.py         # Contains tree generation functions
│── energy_analysis.py        # Computes energy and eigenvalues
│── plotting.py               # All visualization functions
│── utils.py                  # Utility functions (weight functions)
│── config.py                 # Configuration parameters
│── requirements.txt          # Required Python packages
│── README.md                 # Project documentation
```

---

## ⚙️ Configuration Parameters (`config.py`)

Modify `config.py` to customize the simulation:

```python
# Number of iterations for statistics
iterations = 50  

# Number of nodes in the generated tree
node_count = 500  

# Parameters for weight functions
alpha = 0        # Exponent for power weight function
delta = -0.9     # Offset for affine weight function

# Weight function type ('power' or 'affine')
weight = 'power'
```

**Description of Parameters:**
- `iterations`: Number of **Monte Carlo simulations** to compute statistics.
- `node_count`: Number of **nodes in the generated tree**.
- `alpha`: Controls **how preferential attachment scales** (for power function).
- `delta`: Offset parameter for **affine weight function**.
- `weight`: Choose the attachment model:
  - `'power'` → Uses **w(d) = d^alpha**
  - `'affine'` → Uses **w(d) = d + delta**

---

## 🎮 Usage

### **1️⃣ Running the Simulation**
Execute the main script:

```bash
python main.py
```

### **2️⃣ Plot Tree from Adjacency Matrix**
```python
from generate_trees import generate_barabasi_albert_tree
from plotting import plot_tree_from_adjacency_matrix
from utils import power_weight_function

N = 20  # Example tree size
alpha = 0
weight_function = lambda d: power_weight_function(d, alpha)

# Generate tree
adj_matrix = generate_barabasi_albert_tree(N, weight_function)

# Plot it
plot_tree_from_adjacency_matrix(adj_matrix, title="BA Tree Visualization")
```

---

## 📊 Output Examples

### **1️⃣ Energy Evolution Over Time**
![Energy Evolution](https://upload.wikimedia.org/wikipedia/commons/9/9d/Barab%C3%A1si%E2%80%93Albert_model.svg)

### **2️⃣ Tree Visualization**
Generated tree plotted using `networkx`.

```
(Example plot will be displayed)
```

---

## 🤝 Contributing
If you'd like to contribute, feel free to **fork the repository** and submit a **pull request**! 😊

---

## 📜 License
This project is **open-source** under the **MIT License**.

---

## 🔗 References
- [Barabási–Albert Model (Wikipedia)](https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model)
- [Graph Energy (Wikipedia)](https://en.wikipedia.org/wiki/Energy_of_a_graph)
- [NetworkX Documentation](https://networkx.github.io/)
```

---

### **🚀 Why This README is Awesome?**
✅ **Structured & Easy to Read**  
✅ **Explains Features, Installation, and Usage**  
✅ **Includes Configuration Details**  
✅ **Provides Examples & Images**  
✅ **Encourages Contribution**  

Now, your project is **well-documented and user-friendly!** 🎉 Let me know if you need any tweaks! 😊
