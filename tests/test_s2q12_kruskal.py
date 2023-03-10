# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework






class Test_MinimalPower(unittest.TestCase):
    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        import main
        m= main.kruskal(g)
        a = main.kruskal(g)
        #print(m)
        self.assertEqual(
            {node: set(a.graph[node]) for node in g.nodes},
            {1:set([(4,4,1)]), 4: set([(3,4,1), (1,4,1)]), 3: set([(4,4,1), (2,4,1)]), 2: set([(3,4,1)]),5:set([]),6:set([]),7:set([]),8:set([]),9:set([]),10:set([])}
        )

    

if __name__ == '__main__':
    unittest.main()