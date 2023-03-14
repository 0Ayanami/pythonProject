import string
import random


def generate_password():
    pass_word = string.digits + string.ascii_letters + string.punctuation
    pass_word *= 9
    seq = ''
    return seq.join(random.sample(pass_word, 9))


def evaluate_password(password, show_info=True):
    # TODO：验证密码的安全性
    result = False
    #  用一个五位二进制码分别表示
    #  是否有大写字母、是否有小写字母、
    #  是否有数字、是否有标点符号和长度是否合格
    password_state = 0b00000

    if len(password) >= 8:
        password_state |= 0b00001

    for char in password:
        if char.isupper():
            password_state |= 0b10000
        elif char.islower():
            password_state |= 0b01000
        elif char.isdigit():
            password_state |= 0b00100
        else:
            password_state |= 0b00010

    # TODO：输出
    if password_state == 0b11111:
        if show_info:
            print('密码安全性合格。\n')
        result = True
    else:
        if show_info:
            prompt = '密码不符合，'
            if password_state & 0b00001 == 0:
                prompt += '长度不符，'
            if password_state & 0b10000 == 0:
                prompt += '不包含大写字符，'
            if password_state & 0b01000 == 0:
                prompt += '不包含小写字符，'
            if password_state & 0b00100 == 0:
                prompt += '不包含数字，'
            if password_state & 0b00010 == 0:
                prompt += '不包含特殊符号，'
            prompt = prompt[:-1]
            print(prompt)
    return result


def user_input():
    while True:
        user_password = input('请输入新密码：')
        if evaluate_password(user_password):
            break


def auto_generate(show_info=True):
    while True:
        user_password = generate_password()
        if evaluate_password(user_password, show_info):
            print(f"生成密码为：{user_password}")
            break


def main():
    # TODO：输入密码
    auto_generate(False)


if __name__ == "__main__":
    main()
