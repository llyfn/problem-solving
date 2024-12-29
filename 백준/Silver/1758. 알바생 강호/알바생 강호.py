def max_tip(tips):
    tips = sum(map(cal_tip, sorted(tips, reverse=True), range(len(tips))))
    return tips

def cal_tip(tip, order):
    return max(tip - order, 0)

first_tips = [int(input().strip()) for i in range(int(input().strip()))]

print(max_tip(first_tips))
