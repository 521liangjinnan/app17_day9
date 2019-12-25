import os

import yaml


class GetData:
    """解析数据"""
    def get_yml_data(self,yml_name):
        """
        返回yaml文件数据
        :param yml_name:yaml数据文件名字
        :return:
        """
        with open("./Data" + os.sep + yml_name, "r", encoding="utf-8") as f:
            # 解析
            return yaml.safe_load(f)

    def get_json_data(self):
        pass