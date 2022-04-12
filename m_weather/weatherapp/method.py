def gbk_trans_utf8(file_path):
    with open(file_path, 'r', encoding='gbk') as f:
        content = f.read()
    print(content)
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(content)
