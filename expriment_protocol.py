import time
import numpy as np
#------------------------------

def I_gen(n):
    return np.identity(n)

def A1_gen(n,k,q):
    A1_prime = np.random.randint(1, q, (n, k-n))  # 4以上10未満のn行 x (k-n)列の配列の乱数
    In = I_gen(n)
    A1 = np.concatenate([In, A1_prime], 1)
    return A1

def A2_gen(n,k,m,q):
    Zero = np.random.randint(0, 1, (m-n, n))  # 0以上1未満の(m-n)行 x n列の配列の行列
    Imn = I_gen(m-n)
    A2_prime = np.random.randint(1, q, (m-n, k-m))  # 1以上q未満の(m-n)行 x (k-m)列の配列の乱数
    A2 = np.concatenate([Zero,Imn, A2_prime], 1)
    return A2

def sender_commitment(n,k,m,q,beta):
    r = np.random.randint(1,beta,k) # 1以上beta未満のk列の配列の乱数
    x = np.random.randint(1,beta,m) # 1以上beta未満のk列の配列の乱数
    A1 = A1_gen(n,k,q)
    A2 = A2_gen(n,k,m,q)
    A = np.concatenate([A1, A2])
    # print('A',A)
    # print('r',r)
    # print('x',x)
    com = A.dot(r)+x
    return com
def sender_commitment_bdlop(n,k,m,q,beta):
    r = np.random.randint(1,beta,k) # 1以上beta未満のk列の配列の乱数
    x = np.random.randint(1,q,m-n) # 1以上beta未満のm-n列の配列の乱数
    zero = np.random.randint(0,1,n) # 0以上1未満のn列の配列の乱数
    x_ = np.concatenate([zero, x]) # m列の配列
    A1 = A1_gen(n,k,q)
    A2 = A2_gen(n,k,m,q)
    A = np.concatenate([A1, A2])
    # print('A',A)
    # print('r',r)
    # print('x',x)
    com = A.dot(r)+x_
    return com


# a = np.random.randint(0,4,6)
# A = np.random.randint(0, 4, (3, 6))

# print('A',A)
# print('a',a)
# print('A*a',A.dot(a))

n = 140
k = 220
m = 200
q = 2**31
beta = 5

time_sta = time.perf_counter() # Start time measurement
for i in range(10000):
    sender_commitment(n,k,m,q,beta)
time_end = time.perf_counter() # End of time measurement
# Elapsed time in seconds
tim_all = time_end - time_sta
tim_average = tim_all/10000
print('all time of our proposal:',tim_all)
print('average time of our proposal:',tim_average)

# BDLOP18
time_sta = time.perf_counter() # Start time measurement
for i in range(10000):
    sender_commitment_bdlop(n,k,m,q,beta)
time_end = time.perf_counter() # End of time measurement
# Elapsed time in seconds
tim_all = time_end - time_sta
tim_average = tim_all/10000
print('all time of BDLOP protocol:',tim_all,tim_average)
print('average time of BDLOP protocol:',tim_average)

# z = zero = np.random.randint(0,1,5)
# print(z)


# Write the process (in this case, stop for 1 second)
# time.sleep(1)

# print(I_gen(3))
# a = I_gen(3)
# b = np.random.randint(0,30,6)
# print(b)
# print(b+b)
# print(np.concatenate([a, a,a]))
# print(np.random.randint(0, 1, (3, 6)))
