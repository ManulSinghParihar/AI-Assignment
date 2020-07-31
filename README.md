# AI-Assignment

## UCS :

UCS is different from BFS and DFS because here the costs come into play. The goal is to find a path where the cumulative sum of costs is least. 
The ucs.cpp is a C++ program to solve the n-queens problem. It takes input as n.
UCS contains the following :<br />
* A problem graph - here, the graph is n x n matrix.<br />
* A strategy - the graph will be travered such that no 2 queens are under attack by any of the other queen.<br />
* A fringe - this is the data structure used to store possible states.<br />
* A tree - This is the result while traversing the goal node.<br />
* Solution - it gives output as the sequence of the nodes.<br />

## A Star :

A* is used in path-finding and graph traversals.<br />
Apart from the UCS algorithm, it uses a heuristic function to solve the problem.<br />
A* also needs the input value n to solve the n-queens problem.<br />
A* also contains the problem graph, strategy, fringe and tree along with additional heuristic function. It gives out a solution comprising of all possible solutions each of which is an n-length array, consisting of values upto n.<br />

## Genetic Algorithm : 

Genetic algorithms provide computers with a method of problem-solving which is based upon implementations of evolutionary processes. 
The computer program begins with a set of variables which internally resemble the chromosomes which store the genetic information in humans. 
Each genome of these digital chromosomes represents a trait of whatever the data structure is supposed to represent; this information can be stored either in bitfield form, in which each genome is classified as being on or off (0 or 1, respectively). 
Alternatively, they can be stored in a character string in which each character represents an integer value which describes the magnitude of a trait.

Here, we have taken input size as 25 and the weight is randomly distributed between 40 to 80. After assigning the parent chromosome with the values, the two parents are made to cross-over to produce two children.

## NimGame : 

The nimgame is a python program which lets user play with the AI or lets him decide which AI to choose for the AI vs AI game for the sticks game, where every player can pick sticks ranging from 1 to 3. 
If the player plays against the AI, the user has to choose sticks for every round. If the player decides to play AI vs AI then the user is displayed which one of the AI wins.
