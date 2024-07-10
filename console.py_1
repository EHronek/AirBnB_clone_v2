#!/usr/bin/env python3
""" Defines a class that contains the entry point of the command
    of the command interpreter"""
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City

import shlex
from models import storage

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'Amenity': Amenity,
    'Review': Review,
    'City': City
}


class HBNBCommand(Cmd):
    """ entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ EOF to Exit the program"""
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it to JSON
            and prints the `id` """
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print('** class name missing **')
            return
        class_name = parsed_args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id """
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print('** class name missing **')
            return
        class_name = parsed_args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print('** instance id missing **')
            return
        instance_id = parsed_args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance:
            print(instance)
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            save the changes in the json file"""
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print('** class name missing **')
            return
        class_name = parsed_args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print('** instance id missing **')
            return
        instance_id = parsed_args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances based
            on class name"""
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print([str(obj) for obj in storage.all().values()])
            return
        class_name = parsed_args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        instances = [str(obj) for key, obj in storage.all().items()
                     if key.startswith(class_name)]
        print(instances)

    def do_update(self, arg):
        """updates an instance based on the class name and id by
        adding or updating attributes, saves changes into the JSON file"""
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print('** class name missing **')
            return
        class_name = parsed_args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print('** instance id missing **')
            return
        instance_id = parsed_args[1]
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print('** no instance found **')
            return
        if len(parsed_args) < 3:
            print('** attribute name missing **')
            return
        if len(parsed_args) < 4:
            print('** value missing **')
            return
        attribute_name = parsed_args[2]
        attribute_value = parsed_args[3]
        if hasattr(instance, attribute_name):
            attr_type = type(getattr(instance, attribute_name))
            setattr(instance, attribute_name, attr_type(attribute_value))
        else:
            setattr(instance, attribute_name, attribute_value)
        instance.save()

    '''def default(self, line):
        """Handle unrecognized commands"""
        args = line.split('.')
        if len(args) == 2 and args[1] == 'all()':
            class_name = args[0]
            if class_name in classes:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))'''

    def default(self, line):
        """Handle unrecognized commands"""
        command_parts = line.split('.')
        if len(command_parts) != 2:
            print(f"*** Unknown syntax: {line}")
            return

        class_name, command = command_parts
        if class_name not in classes:
            print(f"*** Unknown syntax: {line}")
            return

        if command == 'all()':
            self.do_all(class_name)
        elif command == 'count()':
            self.do_count(class_name)
        else:
            print(f"*** Unknown syntax: {line}")


    def do_count(self, class_name):
        """Retrieve the number of instances of a class"""
        count = sum(1 for key in storage.all() if key.startswith(class_name))
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
