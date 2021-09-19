x = int(input())

N = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(N)):
  N[i] = x
  x = x * 2
  print('N[{}] = {}'.format(i, N[i]))