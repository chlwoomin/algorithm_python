def solution(players, m, k):
    servers = [0] * 24
    answer = 0
    for i in range(24):
        if i-k>=0:
            servers[i-k] = 0
        servers[i] += add_server(players, m, k, i, servers)
        answer+= servers[i]
    return answer

def add_server(players, m, k, i, servers):
    amount = (sum(servers) + 1) * m
    if amount - players[i] > 0:
        return 0
    else:
        return (players[i] - amount) // m + 1
        