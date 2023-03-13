import math

for x in range(1, 11):
    print(repr(x).ljust(2), repr(x*x).ljust(3), repr(x*x*x).ljust(4))
    # 注意前一行 'end' 的使用
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
#  !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
