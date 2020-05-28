# Node_Rank-Lab_assignment
Calculating ranks of nodes of a given graph.

Graph input is given as followed:

	n β
	A01 A02 A03 ... A0k0
	A11 A12 A13 ... A1k3
	A21 A22 A23 ... A2k2
	...
	An−11 An−12 An−13 ... An−1kn
	q
	n1 t1 
	n2 t2 
	n3 t3 
	...
	nq tq
	
 , where n is an integer (number of nodes in graph), β is a float type (probability of following
 the edges of a graph -> (1-β) is the probability of random teleportation from current node to 
 another node).
	After the first line comes n lines which describe edges of a given graph.
 i-th line states all the neighbor nodes of the i-th node.
 One node has a minimum of 1 neighbor and a maximum of 15 neighbors.
	After mentioned n lines comes integer Q which represents number of following queries.
 i-th line after Q input contains integers ni and ti. ni represents the index of the observed node while
 ti represents the wanted iteration of NodeRank algorithm in which we seek the rank of node ni.
 
 
 
 Graph output is wanted as:
 
	r1
	r2
	r3
	...
	rq

 , where ri is the rank of the observed node of the appropriate query.
 ri is rounded to 10 decimal places.

 