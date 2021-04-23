# -*-coding: utf-8 -*-

import os

def html_to_md(file_dir):
    # 获取当前目录下所有的md文件的路径信息
    all_whole_path_files = []
    for root, dirs, files in os.walk(file_dir):
        #print(root, "\n")
        #print("\n", dirs)
        #print("\n", files, "\n")

        for file in files:
            print(file)
            try:
                if file[-5:] == ".html":
                    file_info = [root+'/', file]
                    all_whole_path_files.append(file_info)
            except Exception as e:
                print(e)
    print("==>", all_whole_path_files)

    # 将html依次转换为markdown
    for file_info in all_whole_path_files:
        html = file_info[0] + file_info[1]
        md_name = file_info[1][:-5] + '.md'
        markdown = file_info[0] + md_name
        new_command = 'pandoc ' + html + ' -o ' + markdown

        try:
            result = os.popen(new_command).readlines()
            if len(result) == 0:
                print(html, "已经转换为", markdown)
        except Exception as e:
            print(e)


def main():
    html_to_md('.')

if __name__ == '__main__':
    main()