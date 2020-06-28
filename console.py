#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        Summary: class that define the command interpreter:
    """
    # a custom prompt: (hbnb)
    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User"]

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    # quit and EOF to exit the program
    def do_EOF(self, line):
        "Exit the program with Ctrl+D"
        return True

    def do_quit(slef, line):
        "Quit command to exit the program"
        return True

    # an empty line + ENTER shouldn’t execute anything
    def emptyline(self):
        """ If the line is empty, emptyline() is called,
            the method was modified because the default
            implementation runs the previous command again
            and we want it to pass not executing anything.
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        args_list = arg.split(" ") # this to parse the string
        if not args_list[0]:
            print("** class name missing **")
        elif args_list[0] == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        args_list = arg.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to create
            id_object with the form Classname.id that is the key that we
            will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        args_list = arg.split(" ") # this to parse the string
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to create
            id_object with the form Classname.id that is the key that we
            will ask if is in Storge and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """deletes an instance for the dictionary
                """
                storage.all().pop(id_object)
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not
            on the class name
        """
        element_list = []
        args_list = arg.split(" ") # this to parse the string
        if args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if value.__class__.__name__ == args_list[0]:
                    element_list.append(str(value))
            print(element_list)


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
           updating attribute  (save the change into the JSON file).
        """

        args_list = shlex.split(arg) # this to parse the string

        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            "if the instance of the class name doesn’t exist for the id"
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                id_object = "{}.{}".format(args_list[0], args_list[1])
                args_list[2] = args_list[2].strip('\"')
                args_list[3] = args_list[3].strip('\"')
                setattr(storage.all()[id_object], args_list[2], args_list[3])
                storage.save()

if __name__ == "__main__":
    # Your code should not be executed when imported
    """ cmdloop() is the main processing loop of the interpreter. """
    HBNBCommand().cmdloop()
