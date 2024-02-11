#!/usr/bin/env python3
"""
Console module for HBNB command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with Ctrl+D (EOF).
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line does not execute anything.
        """
        pass

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help message for the EOF command.
        """
        print("Exit the program with Ctrl+D (EOF)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
