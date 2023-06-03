def main():
    not_exit = True
    while not_exit:
        command = input().split()
        if len(command) == 0:
            not_exit = False
        elif len(command) == 1:
            pass # add
        else:
            pass # get

class Trie:
    def __init__(self):
        self.