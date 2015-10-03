# A* (A Star) Search Algorithm
Implementation (in python language) of search algorithm A* (A Star).

Implementation based in the explanation of video: https://www.youtube.com/watch?v=b9fH-j_yNHU

A* or "A star" is the combination of Uniform-cost and Greedy. Uniform-cost orders by path cost or backward cost - g(n). Greedy orders by goal proximity or forward cost - h(n). A* Search orders by the sum: f(n) = g(n) + h(n)

For the graph below, the total cost is 4 and the path is S -> A -> G

![alt tag](https://github.com/marcoscastro/a_star_search_algorithm/blob/master/images/graph1.png)

For the graph below, the total cost is 6 and the path is S -> A -> D -> G

![alt tag](https://github.com/marcoscastro/a_star_search_algorithm/blob/master/images/graph2.png)

Contains a unique file called "a_star.py" that contains three classes: PriorityQueue, Node and Graph.

Output for the graphs shown previously:

![alt tag](https://github.com/marcoscastro/a_star_search_algorithm/blob/master/images/output.png)

Post about A* (in portuguese): http://www.geeksbr.com/2015/03/python-algoritmo-de-busca-a.html

Tested with Python 2.7 and 3.4.
