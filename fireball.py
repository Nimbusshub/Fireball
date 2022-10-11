#!/usr/bin/python3
"""An interactive shell for fireball tool"""

import cmd
from models.portScanner import Scanner
from models.banner import printBanner
from models.scanUsage import usageScan, usageListener
from models.listener import Listener


class FireballPrompt(cmd.Cmd):
    """Interactive command for Fireball project"""

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
        pass

    def do_exit(self, line):
        """Exits the console"""
        print("\nThank you for using fireball")
        return True

    def do_man(self, line):
        """Shows the man page"""
        if line == 'fireball':
            import os
            os.system("bash -c 'man ./man_3_fireball'")
        elif line == '':
            print("Type 'man fireball' to see the usage")
        else:
            print("No manual entry for {}".format(line))

    def do_clear(self, line):
        """Clear all the outputs on the console"""
        import subprocess
        subprocess.call('clear', shell=True)

    def do_scan(self, args):
        """Scans for open ports"""
        if len(args) == 0:
            usageScan()
            return
        args_split = args.split()
        if len(args_split) == 1:
            if args_split[0] == '-h':
                usageScan()
                return
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
                        try:
                            start, end = 0, 0
                            plist = arg2.split('-')
                            start = int(plist[0])
                            end = int(plist[1])
                            Scanner(args_split[0], start, end)
                        except ValueError as err:
                            print(err)
                            print()
                            usageScan()
                    else:
                        plist.append(arg2)
                        Scanner(args_split[0], plist)
                except IndexError:
                    usageScan()
            else:
                usageScan()

    def do_listen(self, args):
        """Listens for connection"""
        if len(args) == 0:
            usageListener()
            return
        args_split = args.split()
        Listener(args_split)


if __name__ == '__main__':
    try:
        FireballPrompt().cmdloop()
    except KeyboardInterrupt:
        print("\nThank you for using fireball")
        exit()
