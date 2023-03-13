def main():
    f = None
    try:
        f = open('test.txt', 'a', encoding='utf-8')
        f.write(input())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

# 最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，
# 由于finally块的代码不论程序正常还是异常都会执行到
# （甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），
# 因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作


if __name__ == '__main__':
    main()
