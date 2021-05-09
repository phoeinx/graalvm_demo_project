# GraalVM Demo Project
A simple polyglot graph network analysis application written in Python using the GraalVM provided [Polyglot API](https://www.graalvm.org/reference-manual/python/Interoperability/). The application has been tested to work with GraalVM version `21.1.0`.

## Dependencies

1. [GraalVM](https://www.graalvm.org/docs/getting-started/#install-graalvm) with support for Python, Ruby and R installed.
2. The R network package, which can be installed with 
   ```$GRAALVM_HOME/bin/r -e 'install_packages(network)'```
   where `$GRAALVM_HOME` points to the home directory of your GraalVM installation.

## Usage
```
graalpython --jvm --polyglot polyglot_graph_analysis.py [graph_input_file]
```
Without a specified graph input file a random graph network will be generated for analysis. (Currently based on the `G(n,p)` [Erdős–Rényi](https://en.wikipedia.org/wiki/Erdős–Rényi_model) model.)

For example usage run:

```
# Analyse a randomly generated graph network
graalpython --jvm --polyglot polyglot_graph_analysis.py

# Analyse an example graph network
graalpython --jvm --polyglot polyglot_graph_analysis.py examples/small_graph.txt
```

### Input Format

The application works with this very common adjacency list format, expecting zero-indexed vertices numbers:

```
<vertex1> <connected_vertex, weight> <connected_vertex, weight> ...
<vertex2> <connected_vertex, weight> <connected_vertex, weight> ...
...
```
For an example input file have a look at the [small_graph](https://github.com/phoeinx/graalvm_demo_project/blob/polyglot-graph-analysis/examples/small_graph.txt) example:

```
0 1,3 3,4 
1 2,3 0,1  
2 3,10 0,5
3 1,3
```

