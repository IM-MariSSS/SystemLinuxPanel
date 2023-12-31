import os
import time
os.system('clear')
ascii="""  


  ______  __      __   ______  ________  ________  __       __ 
 /      \|  \    /  \ /      \|        \|        \|  \     /  \
|  $$$$$$\\$$\  /  $$|  $$$$$$\\$$$$$$$$| $$$$$$$$| $$\   /  $$
| $$___\$$ \$$\/  $$ | $$___\$$  | $$   | $$__    | $$$\ /  $$$
 \$$    \   \$$  $$   \$$    \   | $$   | $$  \   | $$$$\  $$$$
 _\$$$$$$\   \$$$$    _\$$$$$$\  | $$   | $$$$$   | $$\$$ $$ $$
|  \__| $$   | $$    |  \__| $$  | $$   | $$_____ | $$ \$$$| $$
 \$$    $$   | $$     \$$    $$  | $$   | $$     \| $$  \$ | $$
  \$$$$$$     \$$      \$$$$$$    \$$    \$$$$$$$$ \$$      \$$
                                                               
                                                               
                                                               
       _______    ______   __    __  ________  __              
      |       \  /      \ |  \  |  \|        \|  \             
      | $$$$$$$\|  $$$$$$\| $$\ | $$| $$$$$$$$| $$             
      | $$__/ $$| $$__| $$| $$$\| $$| $$__    | $$             
      | $$    $$| $$    $$| $$$$\ $$| $$  \   | $$             
      | $$$$$$$ | $$$$$$$$| $$\$$ $$| $$$$$   | $$             
      | $$      | $$  | $$| $$ \$$$$| $$_____ | $$_____        
      | $$      | $$  | $$| $$  \$$$| $$     \| $$     \       
       \$$       \$$   \$$ \$$   \$$ \$$$$$$$$ \$$$$$$$$       
#############################################################################
#                                                                           #
#                                                                           #
# 1) information(all):                                                      #
#                                                                           #
# 2) CPU°:                                                                  #
#                                                                           #
# 3) live cpu°:                                                             #
#                                                                           #
#############################################################################     
 """
print(ascii)
secim=input("~>")
if secim=="1":
    os.system("clear")
    os.system('figlet STORAGE:')
    os.system(' df -lh ')
    os.system('figlet CPU:')
    os.system('cat /proc/cpuinfo ')
    os.system('figlet cores CPU:')
    os.system('cat /proc/cpuinfo | grep cores')
    os.system('figlet RAM:')
    os.system('free -m ')
    os.system('figlet GREP CPU1:')
    os.system('lspci | grep VGA ')
elif secim=="2":
    os.system('clear')
    os.system('figlet CPU :')
    os.system('sensors')
elif secim=="3":
    LIVE=input('live 1 or 2:')
    if LIVE=="1":
        
      os.system('clear')
      os.system('figlet LIVE CPU:')
      os.system('watch sensors')
    elif LIVE=="2":
        os.system('clear')
        os.system('figlet LIVE CPU2:')
        os.system('bash cpu2.sh')
