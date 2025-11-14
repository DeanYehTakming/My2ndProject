# 猜數字遊戲
import random
def guess_number_game():
# 產生一個1到100之間的隨機整數  
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("歡迎來到猜數字遊戲！請猜一個1到100之間的數字。")
    
    while True:
        user_input = input("請輸入你的猜測（或輸入 'exit' 離開遊戲）：")
        if user_input.lower() == 'exit':
            print("遊戲結束，謝謝參與！")
            break
        try:
            guess = int(user_input)
            attempts += 1
            if guess < number_to_guess:
                print("太低了！請再試一次。")
            elif guess > number_to_guess:
                print("太高了！請再試一次。")
            else:
                print(f"恭喜你！猜對了，答案就是 {number_to_guess}。你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入有效的數字。")