import os
import requests


# 给每个 js 文件开头加注释
def add_prefix(file, prefix):
    contents = []
    with open(file, 'r', encoding='utf-8') as f:
        contents += f.readlines()

    i = 0
    # 删除前面的空行
    while i < len(contents):
        if contents[i] == '\n':
            i += 1
        else:
            break

    if '/**' in contents[i]:
        # 如果存在注释，则删除前面注释的内容
        while i < len(contents):
            if ' */' in contents[i]:
                break
            i += 1

        # 删除注释后一段的空行
        while i < len(contents):
            if contents[i] == '\n':
                i += 1
            else:
                break

    contents = contents[i:]

    with open(file, 'w', encoding='utf-8') as f:
        f.write(prefix)
        for line in contents:
            f.write(line)


# 批量修改 paths 里面的文件
def modify_file(paths, prefix):
    for path in paths:
        files = os.listdir(path)
        for file in files:
            if file.startswith('.'):
                continue
            if not os.path.isdir(file):
                print(path, file)
                add_prefix(path + '/' + file, prefix)


# 读取订阅的 conf 文件，修改本地的 conf 文件
def modify_conf(conf, file_path, url_perfix, support):
    raw = []
    contents = []
    r = requests.get(
        'https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/Js.conf')

    with open(conf, 'wb') as f:
        f.write(r.content)

    with open(conf, 'r', encoding='utf-8') as f:
        raw += f.readlines()

    for line in raw:
        items = line.split(' ')
        if 'https' in items[-1]:
            url = items[-1].strip('\n')
            r = requests.get(url)

            file = url.split('/')[-1]
            file = file.replace('%20', '_')

            with open(file_path + '/' + file, 'wb') as f:
                f.write(r.content)
            url = url_perfix + file + '\n'
            print(items[-1], url)
            items[-1] = url
        temp = ' '.join(items)
        contents.append(temp)

    with open(conf, 'w', encoding='utf-8') as f:
        for line in contents:
            f.write(line)


if __name__ == '__main__':
    SUPPORT = "/**\n * @supported 2ABDBE39B3FF 8BCC0A25D731 E3CA0C025E9B\n */\n\n"
    URL_PREFIX = "https://raw.githubusercontent.com/wongdean/Script/master/JS/"
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    FILE_PATH = os.path.join(PROJECT_ROOT, 'JS')
    modify_conf(os.path.join(PROJECT_ROOT, 'QuantumultX/Js.conf'),
                FILE_PATH, URL_PREFIX, SUPPORT)
    modify_file([os.path.join(PROJECT_ROOT, 'JS')], SUPPORT)
