from quote import quote
from git.repo import Repo
import pyautogui
import time
import datetime
import random
import subprocess

message_interval = int(input("message interval: "))
test_set = 999999
# test_set = int(input("test set: "))
# use_image = str(input('use image(y/n):'))
use_image = 'n'

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

res = quote('family', limit=1)
print(res[0]['quote'])

subprocess.call(
    'powershell.exe git commit -a -m "lalalla"', shell=True)

subprocess.call(
    'powershell.exe git push', shell=True)
countdown = 10
for i in range(countdown, 0, -1):
    print(i)
    time.sleep(1)

print("SPAM IT!!!")

duration = random.randint(3600, 5*3600)

start_time = time.time()


# for i in range(test_set):

#     print(time.time())
#     print(start_time)
#     print(duration)

#     if (time.time() > start_time + duration):
#         break

#     if (use_image == 'y'):
#         for img in text_image:
#             print(img)
#             pyautogui.typewrite(img)
#             pyautogui.typewrite('\r\n')

#             time.sleep(message_interval)
#     else:
#         for j in range(0, 11):
#             print(str(i) + ' : ' + str(j) + ' | ' +
#                   datetime.datetime.now().strftime("%c"))
#             pyautogui.typewrite(str(i) + ' : ' + str(j) + ' | ' +
#                                 datetime.datetime.now().strftime("%c")+'\r\n')

#             time.sleep(message_interval)

#     time.sleep(message_interval)
#     print('==================================')
#     pyautogui.typewrite('==================================\r\n')
