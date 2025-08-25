import pyautogui
import time
import random

time.sleep(5)

completion_count = 2000
current_count = 0

try:
    while current_count < completion_count:
        time.sleep(2)   
        
        # 输入触发字符
        pyautogui.write('print', interval=0.05)
        
        # 等待补全弹出
        time.sleep(2)      
        
        # 使用Tab选择第一个建议
        pyautogui.press('tab')
        
        # 换行
        pyautogui.press('enter')
        pyautogui.hotkey('shift', 'home')
        
        current_count += 1
        
        if current_count % 100 == 0:
            print(f"进度: {current_count}/{completion_count}")
            
        time.sleep(random.uniform(0.1, 0.2))

except KeyboardInterrupt:
    print("任务中断")

print("任务完成！")