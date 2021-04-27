import matplotlib.pyplot as plt
import numpy as np

N, M = 5, 5
print('Size of matrix: {}'.format(N), '{}'.format(M))

P_nm = [[0.3, 0.1, 0.1, 0.3, 0.2],
        [1.0, 0.0, 0.0, 0.0, 0.0],
        [0.9, 0.0, 0.1, 0.0, 0.0],
        [0.1, 0.0, 0.0, 0.1, 0.8],
        [0.0, 0.0, 0.0, 0.1, 0.9]]
P_nm = np.array(P_nm)
print('Matrix of probability:\n {}'.format(P_nm))

mu = [1/32, 1/64, 1/128, 1/256, 1/512]
mu = np.array(mu)
print('Maintenance:', *mu)

e1 = mu[0]
print('e1: {}'.format(e1))

time = 1/mu
print('Waiting time:',*time)

plt.plot(range(1,6), time, 'o-')
plt.title('Waiting time:')
plt.savefig('time.png')
plt.close()

x_i = []
x_i.append(e1/mu[0])
for i in range(N-1):
  x_i.append(P_nm[0][i+1]*e1/mu[i+1])
x_i = np.array(x_i)
print('x_i coefficients:', *x_i)

G = []
for i in range(N+1):
  G.append([x_i[1]**i])
for j in range(1, M):
  G[0].append(1)
for i in range(1, N+1):
  for j in range(1, M):
    G[i].append(G[i][j-1]+x_i[j]*G[i-1][j])
G = np.array(G)
print('Normalizing constant:\n {}'.format(G))

Probability = []
for i in range(1, N+1):
  Probability.append(x_i[0]*G[i-1][M-1]/G[i][M-1])
Probability = np.array(Probability)
print('Probability of condition:', *Probability)

plt.plot(range(1,6), Probability, 'o-')
plt.title('Probability of condition:')
plt.savefig('Probability.png')
plt.close()

Length = 0
for i in range(N):
  Length += G[i][M-1]
Length /= G[N][M-1]
print('Queue length: {}'.format(Length))