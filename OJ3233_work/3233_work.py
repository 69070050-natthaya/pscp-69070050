"""[LEARNING LOGS] สลากกินแบ่ง"""

reward_char , reward_number = input().split()
buy_char , buy_number = input().split()

if reward_char == buy_char and reward_number == buy_number:
    print("1000000")
elif reward_char != buy_char and reward_number == buy_number:
    print("100000")
elif reward_char == buy_char and reward_number[2:5] == buy_number[2:5]:
    print("2000")
elif reward_char == buy_char and reward_number[3:5] == buy_number[3:5]:
    print("1000")
elif reward_char != buy_char and reward_number[2:5] == buy_number[2:5]:
    print("200")
elif reward_char != buy_char and reward_number[3:5] == buy_number[3:5]:
    print("100")
elif reward_char == buy_char and reward_number != buy_number:
    print("20")
else:
    print("0")
