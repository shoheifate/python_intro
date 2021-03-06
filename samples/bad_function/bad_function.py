"""add1()は、関数外の変数を直接参照している。
このため、
(1) 変数x,yを事前に用意してから実行する必要がある。
　これは、関数add1()が「このモジュールに強く依存している」ことを意味する。
(2) 変数x,y以外のデータを参照して実行することができない。これは不便。
(3) ユニットテスト等、動作確認する際にも必ず変数x,yが必要。
　このため、関数以外のことも考慮して動作確認しなければならない。
　関係する要素が増えるため、読みにくく、バグの温床になりやすい。
"""
def add1():
    return x + y

"""add2()は、材料を引数として受け取ってから調理(処理)している。
このため、
(1) 引数として材料を用意するだけで利用可能。
　これは、関数add2()が「このモジュールへの依存度が低い」ことを意味する。
(2) 引数を用意するだけで動作する（状況再現できる）ため、検証しやすい。
"""
def add2(x, y):
    return x + y

x = 2
y = 3
print(add1())

print(add2(x, y))
print(add2(10, 100))
