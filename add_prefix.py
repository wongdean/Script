import os
import requests


def add_prefix(file, prefix):
    contents = []
    with open(file, 'r', encoding='utf-8') as f:
        contents += f.readlines()

    if '/**' in contents[0] and ' */' in contents[2]:
        contents = contents[3:]

    with open(file, 'w', encoding='utf-8') as f:
        f.write(prefix)
        for line in contents:
            f.write(line)
    # print(contents)


def modify_file(paths, prefix):
    for path in paths:
        files = os.listdir(path)
        for file in files:
            if file.startswith('.'):
                continue
            if not os.path.isdir(file):
                print(path, file)
                add_prefix(path + '/' + file, prefix)


def modify_conf(conf, file_path, url_perfix, support):
    raw = []
    contents = []
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

    if '/**' in contents[0] and ' */' in contents[2]:
        contents = contents[3:]

    with open(conf, 'w', encoding='utf-8') as f:
        for line in contents:
            f.write(line)


if __name__ == '__main__':
    SUPPORT = "/**\n * @supported 2ABDBE39B3FF 8BCC0A25D731\n */\n\n"
    URL_PREFIX = "https://raw.githubusercontent.com/wongdean/Script/master/JS/"
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    FILE_PATH = os.path.join(PROJECT_ROOT, 'JS')
    modify_conf(os.path.join(PROJECT_ROOT, 'QuantumultX/Js.conf'),
                FILE_PATH, URL_PREFIX, SUPPORT)
    modify_file([os.path.join(PROJECT_ROOT, 'JS')], SUPPORT)
