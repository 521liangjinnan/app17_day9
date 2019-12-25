# 读取文件
import yaml

with open("./value1.yaml", "r", encoding="utf-8") as f:
    # 加载yaml文件
    data = yaml.safe_load(f)

    # 打印数据
    print("data:{}".format(data))
    # 打印类型
    # print("类型{}".format(type(data.get("value1"))))
    # print("类型{}".format(type(data.get("value2"))))
    # print("类型{}".format(type(data.get("value3"))))
    # print("类型{}".format(type(data.get("value4"))))
    # print("类型{}".format(type(data.get("value5"))))
    # print("类型{}".format(type(data.get("value6"))))
    # print("类型{}".format(type(data.get("value7"))))
    # print("类型{}".format(type(data.get("value8"))))
    # print("类型{}".format(type(data.get("value9"))))
    # print("类型{}".format(type(data.get("value10"))))
    # print("类型{}".format(type(data.get("value11"))))
    # print("类型{}".format(type(data.get("value12"))))
    # print("类型{}".format(type(data.get)))
