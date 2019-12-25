import pytest, sys, os
sys.path.append(os.getcwd())

from Base.getData import GetData



import yaml

"""定义方法"""


def get_sum_data():
    # 定义存储数据列表
    sum_list = []
    data = GetData().get_yml_data("sum.yml")

    # print("data{}".format(data))
    for i in data.values():
        # 追加数据列表
        sum_list.append(tuple(i.values()))
    return sum_list


# print(get_sum_data())


class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        """
        判断两数之和 a+b==c
        :param a:
        :param b:
        :param c:
        :return:
        """
        print("{}+{}={}".format(a, b, c))
        assert a + b == c
