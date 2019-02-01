# 例外処理
'''
　 try 節 には、 発生 する 可能性 の ある エラー が 含ま れ て い ます。 except 節 には、 try 節 の 例外 が 発生 し た 場合 に のみ 実行 さ れる コード が 含ま れ て い ます。
'''
try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")
