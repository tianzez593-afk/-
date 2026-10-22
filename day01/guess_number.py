import random#引入随机数

answer = random.randint(1, 100)#在 1-100 中随机生成一个整数闭区间
tries = 0#计数

print("我想了一个 1-100 的数字。")

while True:#开始游戏
    try:
        guess = int(input("猜一个数字："))
    except ValueError:
        print("请输入一个有效的数字。")
        continue

    tries += 1

    # 在这里补全：
    if  answer>guess : # 1. 猜小了 → 打印"小了"
        print("小了")
    elif answer<guess:  # 2. 猜大了 → 打印"大了"
        print("大了")
    else :
        print("猜对了，你用了 " + str(tries) + " 次") # 3. 猜对了 → 打印"猜对了，你用了 X 次"，然后 break
        break
   
  
   