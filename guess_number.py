#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
猜數字遊戲 (Number Guessing Game)

規則：
1. 程式隨機產生一個 1 到 100 的整數
2. 玩家輸入猜測的數字
3. 程式提示「大了」或「小了」
4. 猜對時顯示「恭喜通過！」並結束遊戲
5. 記錄並顯示猜測次數
"""

import random


def play_game():
    """主遊戲函數"""
    # 隨機產生 1 到 100 的整數答案
    answer = random.randint(1, 100)
    attempts = 0
    
    print("=" * 50)
    print("歡迎來到猜數字遊戲！")
    print("我已經想好一個 1 到 100 之間的數字")
    print("請開始猜測吧！")
    print("=" * 50)
    
    while True:
        try:
            # 獲取玩家輸入
            guess = int(input("\n請輸入你猜測的數字 (1-100): "))
            
            # 驗證輸入範圍
            if guess < 1 or guess > 100:
                print("請輸入 1 到 100 之間的數字！")
                continue
            
            # 增加猜測次數
            attempts += 1
            
            # 判斷猜測結果
            if guess > answer:
                print(f"大了！這是你的第 {attempts} 次猜測。")
            elif guess < answer:
                print(f"小了！這是你的第 {attempts} 次猜測。")
            else:
                print("\n" + "=" * 50)
                print(f"🎉 恭喜通過！🎉")
                print(f"答案就是 {answer}！")
                print(f"你總共猜了 {attempts} 次。")
                print("=" * 50)
                break
                
        except ValueError:
            print("請輸入有效的數字！")
        except KeyboardInterrupt:
            print("\n\n遊戲已結束。")
            break


if __name__ == "__main__":
    play_game()
