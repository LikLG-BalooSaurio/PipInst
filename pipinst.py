from os import system 
from colorama import Fore


print(Fore.YELLOW + """
████████████████████████████████████████████████
█▄─▄▄─█▄─▄█▄─▄▄─█▀▀▀▀▀██▄─▄█▄─▀█▄─▄█─▄▄▄▄█─▄─▄─█
██─▄▄▄██─███─▄▄▄█████████─███─█▄▀─██▄▄▄▄─███─███
▀▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀
""")

print(Fore.RED + """
                                ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                                ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                                ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█
                                
                                
""")

lib = input(Fore.YELLOW + "Nombre de la librería que deseas instalar: ")

system('pip install ' + lib)
exit()