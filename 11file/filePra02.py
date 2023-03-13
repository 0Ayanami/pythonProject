import time

# 除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中


def main():
    # 一次性读取整个文件内容
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('test.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('test.txt') as f:
        lines = f.readlines()
    print(lines)

# 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源


if __name__ == '__main__':
    main()
