#Importing neccessary libraries
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Function for generating the random graph
def gen_random_graph(number_of_nodes, average_degree):
    probability = average_degree / (number_of_nodes - 1)
    G = nx.fast_gnp_random_graph(number_of_nodes, probability)
    return G

#Function for generating small world graph
def gen_smallworld_graph(number_of_nodes, average_degree, re_probability):
    G = nx.watts_strogatz_graph(number_of_nodes, average_degree, re_probability)
    return G

#Function for generating Preferential attachment graph
def gen_preferential_attach_graph(number_of_nodes, average_degree):
    G = nx.barabasi_albert_graph(number_of_nodes, average_degree // 2)
    return G

#Function for calculating the metrics
def calculate_metrics(G):
    if nx.is_connected(G):
        average_path_length = nx.average_shortest_path_length(G)
        clustering_coefficient = nx.average_clustering(G)
        return average_path_length, clustering_coefficient
    else:
        print("Graph is not connected. Unable to calculate the result.")
        return None, None

#Function for plotting a graph
def plot_graph(G, title):
    plt.figure()  # Creating a new figure
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.title(title)
    plt.show()

# Parameters that are being used for calculations
number_of_nodes = 282
average_degree = 14
re_probability = 0.28


print("Implementing Simulating Models for C.ELEGANS")
print("-----------------------------------------")

# Generating Random Graph
random_graph = gen_random_graph(number_of_nodes, average_degree)
random_average_path_length, random_clustering_coefficient = calculate_metrics(random_graph)
print("RANDOM GRAPH:")
print("-------------")
print("Average Path Length:", random_average_path_length)
print("Clustering Coefficient:", random_clustering_coefficient)
plot_graph(random_graph, "Random Graph View")

# Generating Small World Graph
smallworld_graph = gen_smallworld_graph(number_of_nodes, int(average_degree), re_probability)
small_average_path_length, small_clustering_coefficient = calculate_metrics(smallworld_graph)
print("SMALL WORLD GRAPH")
print("-----------------")
print("Average Path Length:", small_average_path_length)
print("Clustering Coefficient:", small_clustering_coefficient)
plot_graph(smallworld_graph, "Small World Graph View")

# Generating Preferential Attachment Graph
preferential_attachment_graph = gen_preferential_attach_graph(number_of_nodes, int(average_degree))
pref_average_path_length, pref_clustering_coefficient = calculate_metrics(preferential_attachment_graph)
print("PREFERENTIAL ATTACHMENT GRAPH")
print("-----------------------------")
print("Average Path Length:", pref_average_path_length)
print("Clustering Coefficient:", pref_clustering_coefficient)
plot_graph(preferential_attachment_graph, "Preferential Attachment Graph View")
