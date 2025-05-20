# Network Modularity Calculator

This script calculates the modularity of networks using the Louvain community detection algorithm. 
Modularity is a measure of the structure of networks or graphs. It was designed to measure the 
strength of division of a network into modules (also called groups, clusters or communities).

## Setup

1.  **Clone the repository (if applicable) or download the files.**
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The main script is `network_analyzer.py`. It can calculate modularity for network data provided in edgelist format.

To run the example calculations for the provided sample data:

1.  **Uncomment the example usage lines in `network_analyzer.py`:**

    Open `network_analyzer.py` and uncomment these lines at the end of the script:

    ```python
    # bio_Q = calculate_modularity("data/biological_network.txt")
    # cosmic_Q = calculate_modularity("data/cosmic_network.txt")
    # print(f"Biological Modularity: {bio_Q:.3f}")
    # print(f"Cosmic Modularity: {cosmic_Q:.3f}")
    ```
    to
    ```python
    bio_Q = calculate_modularity("data/biological_network.txt")
    cosmic_Q = calculate_modularity("data/cosmic_network.txt")
    print(f"Biological Modularity: {bio_Q:.3f}")
    print(f"Cosmic Modularity: {cosmic_Q:.3f}")
    ```

2.  **Run the script:**
    ```bash
    python network_analyzer.py
    ```

    This will output the modularity for the `biological_network.txt` and `cosmic_network.txt` files located in the `data` directory.

    The script also contains a self-contained example within the `if __name__ == '__main__':` block that demonstrates modularity calculation on a small, programmatically created graph, which runs even if the example usage lines for file-based data are commented out.

## Data Files

*   Network data should be in an edgelist text file format. Each line should represent an edge, with two node identifiers separated by a space. For example:
    ```
    0 1
    1 2
    ```
*   Sample data files (`biological_network.txt` and `cosmic_network.txt`) are provided in the `data/` directory.

## Function `calculate_modularity(file_path)`

This function reads a graph from an edgelist file, detects communities using the Louvain algorithm, and then calculates and returns the modularity of the graph based on these communities.
