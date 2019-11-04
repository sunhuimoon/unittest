import unittest

from unittest01.fk_math import *


class TestFkMath(unittest.TestCase):
    print("开始")

    # # 测试一元一次方程的求解
    # def test_one_equation(self):
    #     print("第一个断言")
    #     # 断言该方程求解应该为1.8
    #     self.assertEqual(one_equation(5, 9), 1.8)
    #     # 断言该方程求解应该为2.5
    #     print("第二个断言")
    #     # .00001是干甚的?，，这是msg，错误后传出，Nome传出空
    #     self.assertTrue(one_equation(4, 10) == 2.5, msg=None)
    # #     # 断言该方程求解应该为27/4
    #     print("第三个断言")
    #     self.assertTrue(one_equation(4, 27) == 27 / 4)
    # #     # 断言当a == 0时的情况，断言引发ValueError
    #     print("第四个断言")
    #     with self.assertRaises(ValueError):
    #         one_equation(0, 9)
    #
    # 测试一元二次方程的求解
    def test_two_equation(self):
        print("第2.1个断言")
        r1, r2 = two_equation(1, -3, 2)
        # assertCountEqual(a, b) 	a、b 两个序列包含的元素相同，不管元素出现的顺序如何
        self.assertCountEqual((r1, r2), (2.0, 1.0), '第一个求解出错')
        r1, r2 = two_equation(2, -7, 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
        # 断言只有一个解的情形
        r = two_equation(1, -4, 4)
        self.assertEqual(r, 2.0, '求解出错')
        # 断言当a == 0时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(0, 9, 3)
        # 断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(4, 2, 3)
