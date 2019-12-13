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


# quan x 1.0.3 远程加ID
def edit_remote():
    SUPPORT = "/**\n * @supported 2ABDBE39B3FF 8BCC0A25D731 E3CA0C025E9B\n */\n\n"
    URL_PREFIX = "https://raw.githubusercontent.com/wongdean/Script/master/JS/"
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    FILE_PATH = os.path.join(PROJECT_ROOT, 'JS')
    modify_conf(os.path.join(PROJECT_ROOT, 'QuantumultX/Js.conf'),
                FILE_PATH, URL_PREFIX, SUPPORT)
    modify_file([os.path.join(PROJECT_ROOT, 'JS')], SUPPORT)

# 本地 js 脚本


def edit_local(js_path, local_conf):
    raw = []
    contents = []
    r = requests.get(
        'https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/Js.conf')

    with open(local_conf, 'wb') as f:
        f.write(r.content)

    with open(local_conf, 'r', encoding='utf-8') as f:
        raw += f.readlines()

    for line in raw:
        items = line.split(' ')
        if 'https' in items[-1]:
            url = items[-1].strip('\n')
            r = requests.get(url)

            file = url.split('/')[-1]
            file = file.replace('%20', '_')

            with open(js_path + '/' + file, 'wb') as f:
                f.write(r.content)
            url = file + '\n'
            items[-1] = url
        temp = ' '.join(items)
        contents.append(temp)

    with open(local_conf, 'w', encoding='utf-8') as f:
        for line in contents:
            f.write(line)
    print('remote file updated! Please sync it to Github')

# 由 js_conf 修改配置文件


def edit_conf(js_conf, conf):
    conf_raw, js_raw = [], []
    contents = []
    with open(conf, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            conf_raw.append(line)
    with open(js_conf, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            js_raw.append(line)

    index = 0
    while index < len(conf_raw) and '[rewrite_local]' not in conf_raw[index]:
        contents.append(conf_raw[index])
        index += 1

    contents.append(conf_raw[index])
    contents += js_raw[3:]

    while index < len(conf_raw) and '[mitm]' not in conf_raw[index]:
        index += 1

    while index < len(conf_raw) and 'hostname' not in conf_raw[index]:
        contents.append(conf_raw[index])
        index += 1

    # 直接写入会报错？？？
    temp = 'hostname = ' + js_raw[0].split('=')[-1].strip()
    contents.append(temp)

    with open(conf, 'w', encoding='utf-8') as f:
        for line in contents:
            f.write(line)

    print('overwrite the conf in iCloud')


if __name__ == '__main__':
    edit_remote()
    PROJECT_ROOT = r'/Users/coco/Library/Mobile Documents/iCloud~com~crossutility~quantumult-x/Documents/'
    JS_PATH = os.path.join(PROJECT_ROOT, 'Scripts')
    JS_CONF_PATH = os.path.join(PROJECT_ROOT, 'Profiles/local_js.conf')
    CONF_PATH = os.path.join(
        PROJECT_ROOT, 'Profiles/quantumult.conf')
    edit_local(JS_PATH, JS_CONF_PATH)
    edit_conf(JS_CONF_PATH, CONF_PATH)
