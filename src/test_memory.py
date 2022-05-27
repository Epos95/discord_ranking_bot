import unittest
import memory

class TestMemory(unittest.TestCase):
    def __init__(self, *args, **kwargs): 
        super(TestMemory, self).__init__(*args, **kwargs)
        self.handle = memory.Stats()

    def test_types(self):
        self.assertRaise(TypeError, self.handle.add, 5)
        for functions in [self.handle.add, self.handle.subtract]:
            self.assertRaise(TypeError, functions, 3+5j)
            self.assertRaise(TypeError, functions, 5)
            self.assertRaise(TypeError, functions, True)
            self.assertRaise(TypeError, functions, ["he", "dfs", 3])