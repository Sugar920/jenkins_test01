import os
import yaml


def analyze_file(file_name, key):
    with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r", encoding="utf-8") as f:
        case_data = yaml.load(f)[key]
        data_list = list()
        for i in case_data.values():
            data_list.append(i)
        return data_list


if __name__ == '__main__':
    print(analyze_file("test_contacts_data.yaml", "test_contacts"))
