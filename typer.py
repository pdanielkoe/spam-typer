import pyautogui
import time
import datetime

message_interval = int(input("message interval: "))
test_set = int(input("test set: "))
use_image = str(input('use image(y/n):'))

text_image = [
    '0______________==______________0',
    '1____________======____________1',
    '2_________============_________2',
    '3______==================______3',
    '4___========================___4',
    '5___========================___5',
    '6______==================______6',
    '7_________============_________7',
    '8____________======____________8',
    '9______________==______________9',
]

print("Time to start, please place / focus on the input box")

countdown = 10
for i in range(countdown, 0, -1):
    print(i)
    time.sleep(1)

print("SPAM IT!!!")

for i in range(test_set):
    if(use_image == 'y'):
        for img in text_image:
            print(f'{img}') 
            pyautogui.typewrite(f'{img}\r\n')
            
            time.sleep(message_interval)
    else:
        for j in range(0,11):
            print(f'{i:2} {j:2} | {datetime.datetime.now().strftime("%c")}') 
            pyautogui.typewrite(
                f'{i:2} {j:2}  | {datetime.datetime.now().strftime("%c")}\r\n')
            
            time.sleep(message_interval)

    time.sleep(message_interval)
    print(f'==================================')
    pyautogui.typewrite(f'==================================\r\n')

    
