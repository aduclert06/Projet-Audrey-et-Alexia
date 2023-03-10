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
        print('Hello')
        print(m)
        self.assertEqual(main.kruskal(g),{1:[(4,4)], 4: [(3,4), (1,4)], 3: [(4,4), (2,4)], 2: (3,4)})

    

if __name__ == '__main__':
    unittest.main()