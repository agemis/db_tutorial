# db_tutorial in python - https://github.com/agemis/db_tutorial
# 
import cmd, sys, os

class DBShell(cmd.Cmd):
    intro = 'Welcome to the db shell. Type help or ? to list commands.\n'
    prompt = 'db > '
    file = None

    # ----- commands -----
    def do_someaction(self, arg):
        'Do someaction: SOMEACTION arg1, arg2'
        print(*parse(arg))
        x = DB()
        x.some_action()

    def help_someaction(self):
        print('todo: help for someaction command')
        
    def do_exit(self, arg):
        'Stop recording and exit: EXIT'
        print('Thank you for using db')
        self.close()
        return True

    def do_shell(self, arg):
        'Exec a system shell command: ! cmdline'
        os.system(arg)


    # ----- record and playback -----
    def do_record(self, arg):
        'Save future commands to filename: RECORD file.dbcmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file: PLAYBACK file.dbcmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


class DB:
    """DB main class"""
    i = 12345

    def some_action(self):
        print('SOMEACTION')

    
if __name__ == '__main__':
    DBShell().cmdloop()
