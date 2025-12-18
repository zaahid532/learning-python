#nilai = input("masukan nilai")
#if nilai == 'A': print("selamat")
#elif nilai == 'B':print("kerja bagus")
#elif nilai == 'C':print("semoga beruntung dilain waktu")
#else:
#     print("nilai mu salah")

# #hari = input("masukan hari")
# #if hari == "ini kamis":
#     print("ini kamis")
# #else:
#     print("tidak hari ini jum'at")

# #cuaca = "ini gelap"
# #if cuaca == "ini gelap":
#     print("ini gelap")
    
# score = 75

# if score > 85 and score <= 100:
#     print('grade A')
# elif score > 70 and score < 85:
#     print('grade B')
# elif score < 70 and score <=100:
#     print('grade C')

# arham = 100.000
# if arham == 100.000 or arham == 'tiket':
#     print('arham dapat mainan godzilla')

# else:
#     print('gak dapat apa apa')

# username = input('masukan username :')
# password = input("masukan password :")

# if username != ''  and password != '':
#     if username == 'bgamer567':
#         if password == '459877':
#             print('masuk lobby')

#         else:
#             print('password salah')
#     else:
#          print('username salah')
# else:
#     print('form belum diisi')
from random import randint

print('Rock-Paper-Scissor Game')
print('=======================')

weapon = ['rock', 'paper', 'scissor']
computer = weapon[randint(0,2)]

print("What weapon do you want to use?")
print("Rock / Paper / Scissor")
player = input().lower()

if player == computer:
  print(f"Player and Computer use {player}")
  print("Nobody wins!")
elif player == 'rock':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'paper':
    print("Computer wins!")
    print("Paper covers Rock")
  elif computer == 'scissor':
    print("Player wins!")
    print("Rock smashes Scissor")
elif player == 'paper':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'rock':
    print("Player wins!")
    print("Paper covers Rock")
  elif computer == 'scissor':
    print("Computer wins!")
    print("Scissor cuts Paper")
elif player == 'scissor':
  print(f"Player uses {player}")
  print(f"Computer uses {computer}")
  if computer == 'rock':
    print("Computer wins!")
    print("Rock smashes Scissor")
  elif computer == 'paper':
    print("Player wins!")
    print("Scissor cuts Paper")
else:
  print("You input an invalid weapon!")  