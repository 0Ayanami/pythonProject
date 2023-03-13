#  TODO: 用户输入密码
password = input('请输入新密码：')
#  TODO：判断密码的安全性
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGIT = '0123456789'

have_upper = False
have_lower = False
have_digit = False
have_punc = False

for char in password:
    if char in UPPER:
        have_upper = True
    elif char in LOWER:
        have_lower = True
    elif char in DIGIT:
        have_digit = True
    else:
        have_punc = True

    have_enough = len(password) == 8
    is_secure = (have_enough and have_upper
             and have_lower and have_digit
             and have_punc)
# TODO：输出
    if is_secure:
        print('密码安全性合格。\n')
        break
    else:
        prompt = '密码不符合，'
        if not have_enough:
            prompt += '长度不符，'
        if not have_upper:
            prompt += '不包含大写字符，'
        if not have_lower:
            prompt += '不包含小写字符，'
        if not have_digit:
            prompt += '不包含数字，'
        if not have_punc:
            prompt += '不包含特殊符号，'
prompt = prompt[:-1]
print(prompt)
