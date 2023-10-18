#!/usr/bin/python3
"""The console for the Airbnb project."""
import cmd

class HBNBCommand(cmd.Cmd):
    

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Exit the command interpreter.'''
        return True

    def do_EOF(self, line):
        '''Exit the command interpreter.'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

