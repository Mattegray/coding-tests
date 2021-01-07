def main():
    numbers = [2, 1, 3, 4, 1]
    presult = [2, 3, 4, 5, 6, 7]

    print(solution(numbers))

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            n = numbers[i] + numbers[j]
            if n not in answer:
                answer.append(n)
    answer.sort()
    return answer

if __name__ == '__main__':
    main()
