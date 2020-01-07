# 去除目录中的重复文件
import hashlib
import os


def delete_repeat_files():
    pass


# 按照文件类型归类到目标文件夹
def move_file_to_typed_direct():
    pass


# 删除目录下的空目录
def delete_empty_direct(file_path):
    for v in os.listdir(file_path):
        if os.path.isdir(v) and os.listdir(v).__len__() == 0:
            os.remove(v)


# 获取文件MD5
def get_file_md5(file_path):
    with open(file_path, 'rb') as f:
        md5 = hashlib.md5()
        md5.update(f.read())
        _hash = md5.hexdigest()
    return str(_hash).upper()
