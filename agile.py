d = {'NY':0.15,'LA':0.20}
disc = 0.08
d['NY']
count = float(input())
price = float(input())
state = input()
print('total is %s' % (count*price*(1+d[state])))