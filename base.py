dog_age = float(input('请输入够的年龄'))

like_person_age = 0
# 检查用户输入的是否是负数
if dog_age < 0:
    print('你的输入不合法')
elif dog_age <= 2:
    like_person_age = dog_age * 10.5
else:
    like_person_age = 2 * 10.5
    like_person_age += (dog_age - 2) * 4

if dog_age > 0:
    print(dog_age,'岁的狗,年纪相当于',like_person_age,'岁的人')