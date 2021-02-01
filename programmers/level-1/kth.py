# https://programmers.co.kr/learn/courses/30/lessons/42748

def main():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    presult = [5, 6, 3]

    print(solution(array, commands))

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer


if __name__ == '__main__':
    main()
