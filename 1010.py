c1,n1,p1 = input().split()
c1,n1,p1 = int(c1),int(n1),float(p1)

c2,n2,p2 = input().split()
c2,n2,p2 = int(c2),int(n2),float(p2)

soma = (n1*p1 + n2*p2)

print('VALOR A PAGAR: R$ %.2f'%soma)