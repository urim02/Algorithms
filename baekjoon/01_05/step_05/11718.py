# 입력값이 몇 번 주어지는 모르지만 입력값 그대로 출력해야 한다

while True:
    # 입력값이 들어오면 그대로 출력
    try:
        print(input())

    # 입력값이 안들어온다면 End of File -> break
    except EOFError:
        break