#  TODO: 用户输入密码
password = input('请输入新密码：')
#  TODO：判断密码的安全性
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGIT = '0123456789'
PUNC = '`,.<>?:'"\\{}[]()*&^%$#@!/+=-_ |"

have_upper = False
have_lower = False
have_digit = False
have_punc = False
is_secure = False

for char in password:
    if char in UPPER:
        have_upper = True
    if char in LOWER:
        have_lower = True
    if char in DIGIT:
        have_digit = True
    if char in PUNC:
        have_punc = True
    if have_upper and have_lower and have_digit and have_punc:
        is_secure = True
        print('密码安全性合格\n')
        break
if not is_secure:
    print('密码不安全，请重新设置\n')

# TODO：输出
