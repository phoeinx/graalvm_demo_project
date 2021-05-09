import polyglot
import re
import sys
from itertools import combinations
from random import random

def generate_random_sample_graph(num_vertices, prob_edge):
    '''
    # as soon as more R packages are supported graph network generation with standard methods will become easy
    generate_sample_network = polyglot.eval(string="""function() {
        require(igraph)
        graph <- erdos.renyi.game(50, 1/30)
        edge_list <- as.vector(as_edgelist(graph)))
        list(V(graph), edge_list)
    }""", language="R")
    node_list, edge_list = generate_sample_network()
    '''
    
    node_list = list(range(1, num_vertices + 1))
    edge_list = [[edge[0], edge[1]] for edge in combinations(node_list, 2) if random() < prob_edge]
    
    return node_list, edge_list

def parse_graph_from_file(filename):
    graph = []
    with open(filename) as file:
        for line in file.readlines():
            graph.append([weighted_edge.split(",") for weighted_edge in re.findall( r'\d,\d', line)])

    node_list = list(range(1, len(graph) + 1))

    customMap = polyglot.eval(language="js", string="(array) => Array.from(array, (edge, index) => Array.from(edge).map(edge => [index + 1, parseInt(edge[0]) + 1]))")
    edge_list = customMap(graph)
    edge_list = ruby_array(edge_list).flatten(1)

    return node_list, edge_list

ruby_array = polyglot.eval(language="ruby", string=" lambda { |array| Array(array)}")

filename = sys.argv[-1]

if filename == sys.argv[0]:
    print("No filename given, generating random sample graph.")
    node_list, edge_list = generate_random_sample_graph(20, 1/3)
else:
    print("Parsing graph from: " + filename)
    node_list, edge_list = parse_graph_from_file(filename)

edge_list = ruby_array(edge_list).flatten(1)

analyze_network = polyglot.eval(string="""function(nodes, edges) {
    require(network)
    matrix <- matrix(edges, ncol= 2, byrow= TRUE)
    graph.network <- network(matrix)
    print(noquote("================== (PRESET) NETWORK CHARACTERISTICS =================="))
    print(graph.network)
    print(noquote("================== NETWORK DENSITY =================="))
    print(network.density(graph.network))
    print(noquote("================== NETWORK AS MATRIX =================="))
    print(as.matrix(graph.network))
    
    svg(filename="distributionOfEdgecount.svg")
    require(lattice)
    print(bwplot(tabulate(matrix[,1]), xlab="Distribution of Edgecount"))
    grDevices:::dev.off()
}""", language="R")

analyze_network(node_list, edge_list)