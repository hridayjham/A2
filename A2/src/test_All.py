## @file test_All.py
#  @author Hriday Jham
#  @brief A pytest file containing tests for all functions in
#  the classes CircleT, ShapeT, TriangleT, BodyT and Scene.
#  @date 02/16/2021
#  @details Written to test code.

from Scene import Scene
from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT


class TestCircleT:

    def setup_method(self):
        self.test_circle = CircleT(1, 2, 3, 4)

    def teardown_method(self):
        self.test_circle = None

    def test_init(self):
        try:
            self.test_circle2 = CircleT(1, 2, 0, 2)
            raise ValueError("r is <= 0 and shouldve thrown an error")
        except ValueError:
            pass
        try:
            self.test_circle2 = CircleT(1, 2, 2, -2)
            raise ValueError("m is <= 0 and shouldve thrown an error")
        except ValueError:
            pass

    def test_cm_x(self):
        assert self.test_circle.cm_x() == 1

    def test_cm_y(self):
        assert self.test_circle.cm_y() == 2

    def test_mass(self):
        assert self.test_circle.mass() == 4

    def test_m_inert(self):
        assert self.test_circle.m_inert() == 18


class TestTriangleT:

    def setup_method(self):
        self.test_triangle = TriangleT(1, 2, 3, 4)

    def teardown_method(self):
        self.test_triangle = None

    def test_init(self):
        try:
            self.test_triangle2 = CircleT(1, 2, 0, 2)
            raise ValueError("s is <= 0 and shouldve thrown an error")
        except ValueError:
            pass
        try:
            self.test_triangle3 = CircleT(1, 2, 2, -2)
            raise ValueError("m is <= 0 and shouldve thrown an error")
        except ValueError:
            pass

    def test_cm_x(self):
        assert self.test_triangle.cm_x() == 1

    def test_cm_y(self):
        assert self.test_triangle.cm_y() == 2

    def test_mass(self):
        assert self.test_triangle.mass() == 4

    def test_m_inert(self):
        assert self.test_triangle.m_inert() == 3


class TestBodyT:

    def setup_method(self):
        self.test_body = BodyT([1, 1, 1], [2, 2, 2], [3, 3, 3])

    def teardown_method(self):
        self.test_body = None

    def test_init(self):
        try:
            self.test_body2 = BodyT([1, 2, 3], [4, 5, 6], [8, 9])
            raise ValueError("x, y, m cannot have variable lengths")
        except ValueError:
            pass
        try:
            self.test_body3 = BodyT([1, 2, 3], [4, 5, 6], [-7, 8, 9])
            raise ValueError("m having a value <= 0 should throw an error")
        except ValueError:
            pass

    def test_cm_x(self):
        assert self.test_body.cm_x() == 1

    def test_cm_y(self):
        assert self.test_body.cm_y() == 2

    def test_mass(self):
        assert self.test_body.mass() == 9

    def test_m_inert(self):
        assert self.test_body.m_inert() == 0


class TestScene:

    def setup_method(self):
        self.body = BodyT([1, 1, 1], [2, 2, 2], [1, 1, 1])
        self.test_scene = Scene(self.body, self.Fx, self.Fy, 0, 0)
        self.g = 9.81
        self.m = 1
        self.circle = CircleT(1, 2, 1, 1)

    def Fx(self, t):
        return 5 if t < 5 else 0

    def Fy(self, t):
        return -self.g * self.m if t < 3 else self.g * self.m

    def teardown_method(self):
        self.test_scene = None
        self.body = None
        self.m = None
        self.g = None

    def test_get_shape(self):
        assert self.test_scene.get_shape() == self.body

    def test_get_init_velo(self):
        x, y = self.test_scene.get_init_velo()
        assert x == 0 and y == 0

    def test_set_shape(self):
        self.test_scene.set_shape(self.circle)
        assert self.test_scene.get_shape() == self.circle

    def test_set_init_velo(self):
        self.test_scene.set_init_velo(0, 1)
        x, y = self.test_scene.get_init_velo()
        assert x == 0 and y == 1

    def test_sim(self):
        x, y = self.test_scene.sim(2, 2)
        a = [0.0, 2.0]
        b = [[1.0, 2., 0.0, 0.0], [4.333333335602872, -4.540000004452837, 3.333333333333334,
                                   -6.54]]
        temp1 = x
        temp2 = y
        for i in range(len(x)):
            temp1[i] -= a[i]
        assert abs(max(temp1)) / abs(max(a)) < 0.0001

        for i in range(len(y)):
            for j in range(len(y[i])):
                temp2[i][j] -= b[i][j]

        for i in range(len(y)):
            assert abs(max(temp2[i])) / abs(max(b[i])) < 0.0001
