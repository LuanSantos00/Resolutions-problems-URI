dias = int(input())

anos = dias//360
dias%=365
mes = dias // 30
dias%=30
print("{} ano(s)".format(anos))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dias))