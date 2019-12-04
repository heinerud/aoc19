import collections
import sys


def valid_password_1(x: str) -> bool:
    if not x == "".join(sorted(x)):
        return False

    if len(set(x)) < len(x):
        return True

    return False


def valid_password_2(x: str) -> bool:
    if not valid_password_1(x):
        return False

    if [item for item, count in collections.Counter(x).items() if count == 2]:
        return True

    return False


start = int(sys.argv[1])
stop = int(sys.argv[2])
task = sys.argv[3]

password_candidates = range(start, stop + 1)
validate = valid_password_1 if task == "1" else valid_password_2

for x in password_candidates:
    if validate(str(x)):
        print(x)
