# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
from kruskal_min_power import*
import unittest   # The test framework


class Test_MinimalPower(unittest.TestCase):
    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        
        a = kruskal(g)
        self.assertEqual(
            {node: set(a.graph[node]) for node in g.nodes},
            {1:set([(4,4,1)]), 4: set([(3,4,1), (1,4,1)]), 3: set([(4,4,1), (2,4,1)]), 2: set([(3,4,1)]),5:set([]),6:set([]),7:set([]),8:set([]),9:set([]),10:set([])}
        )
    
    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        
        a = kruskal(g)
        self.assertEqual(
            {node: set(a.graph[node]) for node in g.nodes},
            {1:set([(2,4,89)]), 4: set([(3,4,2)]), 3: set([(4,4,2), (2,4,3)]), 2: set([(1,4,89), (3,4,3)]),5:set([]),6:set([]),7:set([]),8:set([]),9:set([]),10:set([])}
        )

    

if __name__ == '__main__':
    unittest.main()