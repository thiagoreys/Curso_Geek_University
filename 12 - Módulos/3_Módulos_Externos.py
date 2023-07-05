# Para usarmos módulos externos, utilizamos o pip (Python Installer Package).
# Digite 'pip' no terminal para ver como usá-lo.
# Pacotes externos disponíveis: https://pypi.org/
# Aqui instalamos o colorama.

from colorama import init, Fore

init()

print(Fore.RED + 'Texto Colorido!')
print(Fore.CYAN + 'Texto Colorido!')
print(Fore.BLACK + 'Texto Colorido!')
print(Fore.GREEN + 'Texto Colorido!')
print(Fore.YELLOW + 'Texto Colorido!')
