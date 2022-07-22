import os

path = 'atom_test.html'
f = open(path, 'w',encoding="utf-8")
f.write('atomのテスト')  # 何も書き込まなくてファイルは作成されました
f.close()