# https://programmers.co.kr/learn/courses/30/lessons/42576

def main():
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    presult = "mislav"

    print(solution(participant, completion))


def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[i+1]

if __name__ == '__main__':
    main()
