from colorama import Fore, init


init(autoreset=True)


def info(msg):
    print(Fore.GREEN + msg)


def warn(msg):
    print(Fore.YELLOW + msg)


def error(msg):
    print(Fore.RED + msg)
