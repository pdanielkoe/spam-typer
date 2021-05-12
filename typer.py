import pyautogui
import time
import datetime

message_interval = 0.5

message_count = int(input("spam count: "))

print("Time to start, please place / focus on the input box")

countdown = 10
for i in range(countdown, 0, -1):
    print(i)
    time.sleep(1)

print("SPAM IT!!!")

for i in range(1, message_count+1):
    print(f'{i:5} | {datetime.datetime.now().strftime("%c")}')
    pyautogui.typewrite(
        f'{i:5} | {datetime.datetime.now().strftime("%c")}\r\n')

    if(i % 5 == 0):
        time.sleep(message_interval)
        print(f'==================================')
        pyautogui.typewrite(f'==================================\r\n')

    time.sleep(message_interval)
