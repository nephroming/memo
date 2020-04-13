print('Hello')


def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False


def allsum(mylist):   # allsum이라는 이름의 함수를 정의하고, mylist를 변수로 받습니다.
    sum = 0           # sum이라는 변수에 0을 넣습니다.
    for i in mylist:  # mylist의 원소들을 처음부터 돌면서, i에 넣어 아래 식을 수행합니다.
        sum = sum + i # sum에다 직전 sum에다 원소를 더한 값을 넣는 거죠.
    return sum        # 최종 sum을 반환합니다.
mylist = [1,2,3]
print(allsum(mylist))

a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def check_mail(s):
	## 여기에 코딩을 해주세요
    if '@' in s:
        return True
    return False

#결과값
print(check_mail(a))

#아래와 같이 출력됩니다
True

def check_mail(s2):
    c2 = '@'
    if c2 in s2:
        print('참')
    else:
        print('거짓')
s2 = 'qwert@naver.com'
check_mail(s2)
