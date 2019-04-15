initial = ['A', 'D', 'C', 'B']
initialhn = [-3, -2, -1, 0]
final = ['A', 'B', 'C', 'D']
finalhn = [0, 1, 2, 3]
ground = []
goal = []
goalhn = []
i = 0
j = 0
s = 0
while len(initial) > 0:
    ground.append(initial[i])
    print("ground  ", ground[j])
    s = s + initialhn[i]
    print(" h(n)", s, "blocks ", initial)
    initial.pop(i)
    initialhn.pop(i)
    j = j + 1

print("Building up the blocks  ")
print("Take from ground and add to goal")
k = 0
m = 0
for i in final:
    if i in ground:
        goal.append(i)
        goalhn.append(finalhn[k])
        m = m + goalhn[k]
        print("goal at present ", goal, "sum of goal huristic vale ", m)
        k = k + 1
