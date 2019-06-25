# _*_ coding=utf-8 _*_


# 带参数的装饰器:在最外层天加一层函数，用来接收装饰器函数的参数
def login(auth_type):   # 参数从这里传进来

    def auth(func):     # 要执行的函数从这里传入

        def inner():    # 再定义一层函数,主要认证逻辑
            if auth_type == "QQ":
                # 认证逻辑：
                return func()
            if auth_type == "WeChat":
                # 认证逻辑：
                return func()

        return inner

    return auth


@login('QQ')
def europe_america():
    print("——————Europe And America——————")


@login('WeChat')
def japan_korea():
    print("——————Japan And Korea——————")


if __name__ == "__main__":
    europe_america()
    japan_korea()
