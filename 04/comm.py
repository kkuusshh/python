import sys

def communication(first):

    if first == '010':
        RET = 'UNKNOWN'
    elif first == '011':
        RET = 'SKT'
    elif first == '019':
        RET = 'KT'
    elif first == '017':
        RET = 'LGT'
    else:
        sys.exit('[ FAIL ] unknown communication company.')

    return RET

phone_number = input("휴대전화번호 입력: ")
first = phone_number.split('-')[0]
comm = communication(first)

if   comm == 'SKT'   : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'KT'    : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'LGT'   : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'UNKNOWN': print('당신의 통신사는 알수 없습니다.')
else: sys.exit(1)