#
# import numpy as np

# ar = np.array([0,1,2,3,4,5,6,7,8,9])
# print(ar)
# print(type(ar))

# data = [0,1,2,3,4,5,6,7,8,9]
# answer = []
# for di in data:
#     answer.append(2*di)
    
# print(answer)
# print(type(answer))

# x = np.array(data)
# print(x)
# x = 2 * x
# print(x)
# print(type(x))

# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])

# print(2 * a + b)
# print(type(2 * a + b))

# c = np.array([[0, 1, 2], [3, 4, 5]])
# print(c)
# print(len(c))
# print(len(c[0]))

# d = np.array([[[1, 2, 3, 4],
#                [5, 6, 7, 8],
#                [9, 10, 11, 12]],
#               [[11, 12, 13, 14],
#                [15, 16, 17, 18],
#                [19, 20, 21, 22]]])
# print(d)
# print(len(d)), print(len(d[0])), print(len(d[0][0]))


# print(a.ndim)
# print(a.shape)

# print(c.ndim)
# print(c.shape)

# print(d.ndim)
# print(d.shape)
# 

# import numpy as np
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = np.reshape(a,(2,4))
# #세로로 2 가로로 4인 넘파이 배열로 변환
# c = np.reshape(a,(4,2))
# #세로로 4 가로로 2인 넘파이 배열로 변환

# print(a)
# print()
# print(b)
# print()
# print(c)

# import numpy as np
# a = np.arange(1,9)
# b = a.reshape(2,2,2)
# print(b)
# print()
# print(b[0])

import numpy as np

x = np.arange(12)
x = x.reshape(3,4)
print(x)

# print(x.reshape(-1,1))

# print(x.reshape(-1,1))

x.reshape(-1,1)