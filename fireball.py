#!/usr/bin/python3
"""An interactive shell for fireball tool"""

from ast import Index
import cmd
from models.portScanner import Scanner
from models.banner import printBanner
from models.scanUsage import usageScan


class FireballPrompt(cmd.Cmd):
    """Interactive command for HBNB project"""

    __commands = ["EOF", "exit", "man", "clear", "scan"]

    intro = printBanner()
    intro = '\n' + "Welcome to fireball shell. Type 'man fireball' to see the usage\n"
    prompt = "<FireB>  "

    # def precmd(self, args):
    #     if args == '':
    #         return args
    #     args_split = args.split()
    #     plist = []
    #     if args_split[1] == '-p':
    #         if ',' in args.split[2]:
    #             plist = args_split[2].split(',')
    #             args = list(args_split[0] + plist

    #     return args

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        exit()

    def do_exit(self, line):
        print("\nThank you for using fireball")
        exit()

    def do_man(self, line):
        if line == 'fireball':
            import os
            os.system("bash -c 'man ./manii'")
        elif line == '':
            print("Type 'man fireball' to see the usage")
        else:
            print("No manual entry for {}".format(line))

    def do_clear(self, line):
        import subprocess
        subprocess.call('clear', shell=True)

    def do_scan(self, args):
        """Port Scanner"""
        if len(args) == 0:
            usageScan()
            return
        args_split = args.split()
        if len(args_split) == 1:
            Scanner(args_split[0])
        else:
            plist = []
            if args_split[1] == '-p':
                try:
                    arg2 = args_split[2]
                    if ',' in arg2:
                        plist = arg2.split(',')
                        Scanner(args_split[0], plist)
                    elif '-' in arg2:
                        start, end = 0, 0
                        plist = arg2.split('-')
                        start = int(plist[0])
                        end = int(plist[1])
                        Scanner(args_split[0], start, end)
                    else:
                        plist = args_split[2]
                        Scanner(args_split[0], plist)
                except IndexError:
                    usageScan()
            else:
                usageScan()


if __name__ == '__main__':
    try:
        FireballPrompt().cmdloop()
    except KeyboardInterrupt:
        print("\nThank you for using fireball")
        exit()
