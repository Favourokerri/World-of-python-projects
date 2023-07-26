#!/usr/bin/python3
"""console application """
from models.base_model import BaseModel
from models.register import Register
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """console application """
    prompt = "(Imperial Banking) "
    print("*****welcome to imperial Banking system******")
    print()
    print("=>>)type register if you are new")
    print("=>>)for more options type help")
    print("=>>)for explantion of any function type help function_name")
    print("*******************************")

    def do_register(self, line):
        """ command for registration of a person
       <Usage>: register
       """
        person = Register()
        person.get_first_name()
        person.get_last_name()
        person.get_age()
        person.get_sex()
        person.get_phone_number()
        person.get_email()
        person.get_password()
        print(person.id)
        person.confirm_password()
        storage.new(person)
        person.save()
        
    def do_quit(self, line):
        """
        commnad for quit
        <usage>: quit
        """
        return True
    def do_login(self, line):
        """ interface when user logs in """

        class HBNBCommand(cmd.Cmd):
            prompt = "(welcome okerri)"

            def do_quit(self, line):
                """commnad for quit"""
                return True

            def do_EOF(self, line):
                """enable cntrol d"""
                return True

            def emptyline(self):
                """do nothing for emptyline"""
                pass

        if __name__ == '__main__':
            HBNBCommand().cmdloop()

    def do_EOF(self, line):
        """enable contro d"""
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
