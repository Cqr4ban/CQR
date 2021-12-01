#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：蔡秋蓉
日期：2021/11/28
"""
import random
def name_to_number(name):
    if name=='rock':
        return 0
    elif name=='spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    else:
        print("Error:No Correct Name")
def number_to_name(number):
   if number==0:
       return'rock'
   elif number==1:
       return'spock'
   elif number==2:
       return'paper'
   elif number==3:
       return'lizard'
   else:
       return'scissors'
   def rpsls(player_choice):
    print("----------------")
    print("请输入您的选择：")
   player_choice=input()
   player_choice_number=name_to_number(player_choice)
   comp_number=random.randrange(0,4)
   comp_choice=number_to_name(comp_number)
   print("计算机的选择为：")
   diff=(comp_number-player_choice_number)%5
   if diff==0:
      print("您和计算机出的一样呢")
   elif diff==3 or diff==4:
      print("您赢了")
   elif diff==1 or diff==2:
       print("计算机赢了")
   else:
       print("Error:No Correct Name")
   rpsls("rock")
   rpsls("spock")
   rpsls("paper")
   rpsls("lizard")
   rpsls("scissors")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择：")
choice_name=input()
rpsls(choice_name)