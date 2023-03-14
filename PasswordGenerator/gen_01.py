import string


while True:
    # TODO: 用户输入密码
    password = input('请输入新密码：')
    # TODO：判断密码的安全性

    #  用一个五位二进制码分别表示
    #  是否有大写字母、是否有小写字母、
    #  是否有数字、是否有标点符号和长度是否合格
    password_state = 0b00000

    for char in password:
        if char in string.ascii_uppercase:
            password_state |= 0b10000
        elif char in string.ascii_lowercase:
            password_state |= 0b01000
        elif char in string.digits:
            password_state |= 0b00100
        else:
            password_state |= 0b00010

        if len(password) >= 8:
            password_state |= 0b00001

        # TODO：输出
    if password_state == 0b11111:
        print('密码安全性合格。\n')
        break
    else:
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
