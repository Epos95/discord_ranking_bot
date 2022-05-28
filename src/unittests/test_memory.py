import unittest
# How to import from another folder???? Ahhhhhhh
from ./ import memory

class TestMemory(unittest.TestCase):
    def __init__(self, *args, **kwargs): 
        super(TestMemory, self).__init__(*args, **kwargs)
        self.handle = memory.Stats()

    def test_types(self):
        # This will test that the arguments raises TypeErrors
        for functions in [self.handle.add, self.handle.subtract, self.handle.get_stat]:
            self.assertRaises(TypeError, functions, 3+5j)
            self.assertRaises(TypeError, functions, 5)
            self.assertRaises(TypeError, functions, True)
            self.assertRaises(TypeError, functions, ["he", "dfs", 3])