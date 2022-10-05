import unittest
import memory  # How to import from another folder???? Ahhhhhhh


class TestMemory(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMemory, self).__init__(*args, **kwargs)
        self.handle = memory.Memory()

    def test_types(self):
        # This will test that the arguments raises TypeErrors
        for functions in [
            self.handle.add,
            self.handle.subtract,
            self.handle.get_rating,
        ]:
            self.assertRaises(TypeError, functions, 3 + 5j)
            self.assertRaises(TypeError, functions, 5)
            self.assertRaises(TypeError, functions, True)
            self.assertRaises(TypeError, functions, ["he", "dfs", 3])
