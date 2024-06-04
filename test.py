import unittest
from main import cube_volume_calc
from main import sphere_volume_calc
from main import cone_cylinder_volume_calc


class TestVolumeCalculator(unittest.TestCase):

    def test_1_cube(self):
        self.assertEqual(cube_volume_calc(5, 2), 125.00)
    def test_2_cube_none(self):
        self.assertEqual(cube_volume_calc(None, 2), "error")
    def test_3_cube_char(self):
        self.assertEqual(cube_volume_calc(5, 'ghj'), "error")
    def test_4_sphere(self):
        self.assertEqual(sphere_volume_calc(5, 3), 523.599)
    def test_5_sphere_none(self):
        self.assertEqual(sphere_volume_calc(5, None), "error")
    def test_6_cone(self):
        self.assertEqual(cone_cylinder_volume_calc('cone', 5, 5, 4), 130.8997)
    def test_7_cone_none(self):
        self.assertEqual(cone_cylinder_volume_calc(None, 5, 5, 4), "error")
    def test_8_cylinder(self):
        self.assertEqual(cone_cylinder_volume_calc('cylinder', 3, 4, 1), 113.1)
    def test_9_cylinder_char(self):
        self.assertEqual(cone_cylinder_volume_calc('cylinder', '-', 4, 1), "error")


if __name__ == '__main__':
    unittest.main()
