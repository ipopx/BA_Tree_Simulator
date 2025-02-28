# Barabási–Albert Tree Model Simulation 🌳

This project simulates **random trees** using the **Preferential attachment model** and analyzes their properties. It generates trees, computes their energy statistics, and visualizes their structure.

---

## 📌 Features
✅ Generate **Barabási–Albert Trees** using two different methods:
   - Standard preferential attachment (`generate_barabasi_albert_tree`)
   - Optimized bucket-based selection (`roll_barabasi_albert_tree`)

✅ Visualize:
   - **Tree structures** with `networkx`
   - **Energy/time ratio statistics**
   - **Eigenvalue distributions**
   - **Energy evolution over time**

✅ Selectable **modes** to **easily switch between different analyses**.

---

## 🚀 Installation
To install the required dependencies, run:

```bash
pip install -r requirements.txt
```
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

Modify `config.py` to customize the simulation.

### **🔹 Explanation of Parameters:**
- `iterations`: Number of **Monte Carlo simulations** to compute statistics.
- `node_count`: Number of **nodes in the generated tree**.
- `alpha`: Controls **how preferential attachment scales** (for power function).
- `delta`: Offset parameter for **affine weight function**.
- `weight`: Choose the attachment model:
  - `'power'` → Uses **w(d) = d^alpha**
  - `'affine'` → Uses **w(d) = d + delta**
- `mode`: Selects the **type of analysis** to run.
  - `'energy time ratio'`  → Computes and plots the energy/time ratio histogram
  - `'energy evolution'`   → Computes and plots energy evolution over time
  - `'eigenvalues'`        → Computes and plots eigenvalue distribution
  - `'drawing'`            → Plots the generated tree structure

---

## 🎮 Usage

### **Running the Simulation**
Modify `mode` in `config.py`, then run:

```bash
python main.py
```
---

## 📊 Output Examples

### **1️⃣ Energy Evolution Over Time**


### **2️⃣ Tree Visualization**

---
