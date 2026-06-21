def a(a):
    return a

if __name__ == '__main__':
    print(a('true'))   # 字符串
    print(a(True))     # 布尔值
    print(a(0))        # 整数

    for y in range(1, 10):
        for x in range(1, 10):
            if x > y:
                break
            print(f'{y}*{x}={y*x}', end=' ')
        print()
