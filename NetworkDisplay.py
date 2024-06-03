import networkx as nx
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def networkxDisplay(sentiment_matrix,characters_freq):
    # get the characters list and their frequency value
    characters = list(zip(*characters_freq))[0]
    frequency =  list(zip(*characters_freq))[1]
    node_size = [ freq*100 for freq in frequency]
    # extract edge info from matrix
    shape = sentiment_matrix.shape[0]
    sentiment_edge = list()
    edge_value = list()
    # Handeling edge color
    normalized_matrix = sentiment_matrix / np.max(np.abs(sentiment_matrix))
    edge_weight = np.log(np.abs(1000 * normalized_matrix) + 1) * 0.7
    edge_color = 2000 * normalized_matrix
    # get all lower triangle values' index
    lower_tri_loc = list(zip(*np.where(np.triu(np.ones([shape, shape])) == 0)))
    for indx in lower_tri_loc:
        edge_value.append(sentiment_matrix[indx])
        sentiment_edge.append((characters[indx[0]],characters[indx[1]],
                               {'weight': edge_weight[indx], 'color': edge_color[indx]}))
    # add nodes and edges to graph object
    sentiment_G.add_nodes_from(characters)
    sentiment_G.add_edges_from(sentiment_edge)
    # Use spring algorithm : give axis position to nodes
    pos = nx.circular_layout(sentiment_G)
    # define colormap
    colormap = plt.cm.ScalarMappable(cmap=plt.cm.plasma)
    colormap.set_clim(0,1)
    # map edges with colors
    edges = sentiment_G.edges()
    edge_weights = [sentiment_G[u][v]['weight'] for u, v in edges]
    edge_colors = [sentiment_G[u][v]['color'] for u, v in edges]
    # Draw the graphs
    nx.draw_networkx_nodes(sentiment_G,pos,node_size=node_size)
    nx.draw_networkx_edges(sentiment_G,pos,edge_color=edge_colors,
                                   width=edge_weights)
    nx.draw_networkx_labels(sentiment_G,pos, font_size=12, 
                                     font_color="black", font_family="sans-serif")
    plt.show()

sentiment_G = nx.Graph()

"""
# Example Data
sentiment_matrix = np.array([
    [0, 0.1, 0.2, 0.3, 0.4, 0.5],
    [0.1, 0, 0.6, 0.7, 0.8, 0.9],
    [0.2, 0.6, 0, 1.0, 1.1, 1.2],
    [0.3, 0.7, 1.0, 0, 1.3, 1.4],
    [0.4, 0.8, 1.1, 1.3, 0, 1.5],
    [0.5, 0.9, 1.2, 1.4, 1.5, 0]
])
characters_freq = [('A', 5), ('B', 3), ('C', 2), ('D', 4), ('E', 1), ('F', 2)]
# Run the function with example data
networkxDisplay(sentiment_matrix, characters_freq)
"""