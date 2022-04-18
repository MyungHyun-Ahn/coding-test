from collections import defaultdict


def solution(id_list, report, k):

    answer = [0] * len(id_list)
    report = set(report)

    dict1 = defaultdict(set)
    reported_user_count = defaultdict(int)
    user = []

    for r in report:
        report_user, report_result = r.split()
        reported_user_count[report_result] += 1
        dict1[report_user].add(report_result)

        if reported_user_count[report_result] == k:
            user.append(report_result)

    for s in user:
        for i in range(len(id_list)):
            if s in dict1[id_list[i]]:
                answer[i] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))