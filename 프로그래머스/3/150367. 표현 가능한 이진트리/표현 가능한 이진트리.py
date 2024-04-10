def solution(numbers):
    def get_expon(num):
        expon = 1
        while(num > 1):
            num //= 2
            expon += 1
        return expon
    for n in numbers:
        expon1 = get_expon(n)
        expon2 = get_expon(expon1)
        print(expon1, expon2)
    answer = []
    return answer