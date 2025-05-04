RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
LIGHTBLUE = "\033[94m"
BOLD_WHITE = "\033[1;37m"


class Logger():
    def log(message):
        print(f"[{LIGHTBLUE}+{RESET}] {BOLD_WHITE}{message}{RESET}")

    def error(message):
        print(f"[{RED}*{RESET}] {BOLD_WHITE}{message}{RESET}")

    def success(message):
        print(f"[{GREEN}-{RESET}] {BOLD_WHITE}{message}{RESET}")
