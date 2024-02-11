#!/usr/bin/python3
""" Console module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNB command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Exit program at End of File (EOF) """
        print("")
        return True

    def emptyline(self):
        """ Do nothing on empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
