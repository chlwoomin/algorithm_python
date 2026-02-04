discount = [10,20,30,40]
def solution(users, emoticons):
    answer = []
    users.sort()
    select_emoticon = []
    dfs(select_emoticon, emoticons, users)
    answer = max(results)
    return answer
# [할인율, 할인된 가격]
results = []
def dfs(select_emoticon, emoticons, users):
    if not emoticons:
        user_buy(select_emoticon, users)
        return
    node = emoticons.pop()
    for i in discount:
        select_emoticon.append([i, node*(1-i/100)])
        dfs(select_emoticon, emoticons, users)
        select_emoticon.pop()
    emoticons.append(node)
def user_buy(select_emoticon, users):
    result = [0, 0]
    for user in users:
        sum_price = 0
        for discount, price in select_emoticon:
            if user[0] <= discount:
                sum_price += price
        if user[1] <= sum_price:
            result[0] += 1
        else:
            result[1] += sum_price
    results.append(result)
    