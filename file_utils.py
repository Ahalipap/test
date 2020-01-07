import hashlib
import os
import shutil

from filetype import filetype

file_path_set = set()


# 获取所有的文件列表
def get_all_files(source_file):
    file_path_set = set(os.listdir(source_file))
    res_list = []
    dir = os.path.dirname(source_file)
    for v in file_path_set:
        full_path = os.path.join(dir, v)
        if os.path.isfile(full_path):
            res_list.append(full_path)
    return res_list


# 去除目录中的重复文件
def delete_repeat_files(source_file):
    file_list = get_all_files(source_file)
    md5_set = set()
    for v in file_list:
        md5 = get_file_md5(v)
        if md5 in md5_set:
            os.remove(v)
        else:
            md5_set.add(md5)


# 按照文件类型归类到目标文件夹
def move_file_to_typed_direct(source_file, target_file, file_type):
    if os.path.isfile(target_file) or os.path.isfile(source_file):
        return
    filepath_set = set(os.listdir(source_file))
    dir = os.path.dirname(source_file)
    for v in filepath_set:
        full_path = os.path.join(dir, v)
        if os.path.isfile(full_path):
            kind = filetype.guess(full_path)
            if kind and kind.EXTENSION == file_type:
                shutil.move(full_path, target_file)


# 删除目录下的空目录
def delete_empty_direct(file_path):
    if not os.path.isfile(file_path):
        return None
    for v in os.listdir(file_path):
        if os.path.isdir(v) and os.listdir(v).__len__() == 0:
            os.remove(v)


# 获取文件MD5
def get_file_md5(file_path):
    if not os.path.isfile(file_path):
        return None
    with open(file_path, 'rb') as f:
        md5 = hashlib.md5()
        md5.update(f.read())
        _hash = md5.hexdigest()
    return str(_hash).upper()


if __name__ == '__main__':
    pass
# move_file_to_typed_direct('/Users/ltb/Desktop/微信图片/', '/Users/ltb/Desktop/', 'jpg')
# print(get_all_files('/Users/ltb/Desktop/微信图片/'))
