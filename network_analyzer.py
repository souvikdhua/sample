import networkx as nx

def calculate_modularity(file_path):
    G = nx.read_edgelist(file_path)
    # Using the Louvain algorithm for community detection as it's a common choice
    # and was present in the original user snippet.
    communities = nx.community.louvain_communities(G)
    # Ensure communities are non-overlapping for nx.community.modularity
    # The Louvain algorithm in networkx by default returns non-overlapping communities.
    # If a different algorithm were used, this might need adjustment.
    Q = nx.community.modularity(G, communities)
    return Q

# Example usage:
# These lines will be commented out for now to prevent errors when running tests,
# as the data files don't exist yet. They can be uncommented for manual runs
# once data files are in place.
# bio_Q = calculate_modularity("data/biological_network.txt")
# cosmic_Q = calculate_modularity("data/cosmic_network.txt")
# print(f"Biological Modularity: {bio_Q:.3f}")
# print(f"Cosmic Modularity: {cosmic_Q:.3f}")

if __name__ == '__main__':
    # Example of how to run, assuming data files are present
    # To make this runnable, create 'data/biological_network.txt'
    # and 'data/cosmic_network.txt' with some edgelist data.
    # For example, 'data/biological_network.txt' could contain:
    # 0 1
    # 1 2
    # 2 0
    print("To run the modularity calculation, ensure 'data/biological_network.txt' and 'data/cosmic_network.txt' exist.")
    print("Example: bio_Q = calculate_modularity('data/biological_network.txt')")
    print("Example: print(f'Biological Modularity: {bio_Q:.3f}')")

    # Small test case that can be run without external files:
    # Create a simple graph
    G_test = nx.Graph()
    G_test.add_edges_from([(0,1), (1,2), (2,0), (3,4), (4,5), (5,3)])
    # Define communities for this test graph
    # Expected communities: {0,1,2} and {3,4,5}
    test_communities = [ {0,1,2}, {3,4,5} ]
    # Calculate modularity
    Q_test = nx.community.modularity(G_test, test_communities)
    print(f"Test graph modularity with predefined communities: {Q_test:.3f}")

    # Example using Louvain communities on the test graph
    louvain_comms_test = nx.community.louvain_communities(G_test)
    Q_louvain_test = nx.community.modularity(G_test, louvain_comms_test)
    print(f"Test graph modularity with Louvain communities: {Q_louvain_test:.3f}")
