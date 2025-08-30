import heapq
import math
import copy
from copy import deepcopy
import numpy as np

## Name:Yousif Alani
## PID: 18562674

#######################################################
##############       QUESTION 1 HERE   ################
#######################################################

def myFloyd(M):

  '''
    Todo:

    Write an algorithm that runs Floyd-Warshall's algorithm on a graph

    Input:
        M: The adjacency matrix representing the graph

    return:
        shortest_paths: an array of the n distance matrices on each of the n phases
            of the algorithm, where the distance matrix is an n×n matrix whose i-th row, j-th 
            column entry denotes the shortest distance from vertex i to vertex j (at that phase 
            of the algorithm).

  '''


#########################################################
##############       QUESTION 2 HERE   ##################
#########################################################
def myDijkstra(vertices, edges):
  '''
    TODO:

    Write an algorithm that runs Dijkstra's Algorithm on a Directed Graph to solve the Single Source Shortest Path Problem.
    The source vertex is always vertex 0.

    Input:
        vertices: Vector of the first n non-negative integers representing the n vertices of G.
        edges: A vector containing edges in G in the form of tuples where each tuple is of the form [i, j, c(i, j)],
            corresponding to the directed edge from vertex i to vertex j with weight c(i, j).


    return:
        sol: A tuple of the following elements in the exact order:
            0:  shortestPath: List of lists containing the shortest path from source vertex to vertex i at index i.
            1:  shortestPathLength: A vector that contains the shortest distance from source vertex to vertex i at index i.

    Some Helper functions that might help you modularize the code:
        - myInitialize(n, s) : calculates Initialize (as explained in class) from a given source node (s) given the number of nodes (n).

        - myRelax(distance, edges, u) : Gives an updated distance vector after `Relax`-ing (as explained in class) all edges
          going out from u.

    Note: These functions are recommended however we won't be grading your implementations of the
          above stated functions

  '''

#########################################################
##############       QUESTION 3 HERE   ##################
#########################################################
def myMSTTSP(distance_matrix):
  '''
    TODO:
    
    Write an algorithm that solves the Traveling Salesman Problem using the MST-based approximation algorithm.
    
    Input:
        distance_matrix: A 2D list where distance_matrix[i][j] represents the distance from vertex i to vertex j.
        
    return:
        tuple: A tuple containing:
            0: tour: A list of integers representing the order in which vertices are visited in the TSP tour
            1: total_distance: An integer representing the total distance of the tour
                    
    Note: The tour should start and end at vertex 0, but you only need to return the visiting order,
          not a complete cycle.
  '''