def solution(jobs):
    answer = 0
    n = len(jobs)
    for i in range(n):
        jobs[i].append(i)
    jobs.sort()
    # jobs = [요청시각, 소요시간, 번호]
    current_time = 0
    request_queue = []
    wait_time = 0
    task = [0,0,0]
    task_flag = False
    while jobs or request_queue:
        for job in jobs:
            if job[0] <= current_time:
                request_queue.append(jobs.pop(0))
            else:
                break
        if request_queue:
            request_queue.sort(key=lambda x:(x[1],x[0],x[2]))
        if wait_time == 0:
            answer += current_time - task[0]
            task_flag = False
        if request_queue and task_flag == False:
            task = request_queue.pop(0)
            wait_time = task[1]
            task_flag = True
        current_time += 1
        wait_time -= 1
    answer+= current_time+wait_time - task[0]
    return answer // n