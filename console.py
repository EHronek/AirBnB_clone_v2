#!/usr/bin/python3
""" The Airbnb Console """

from cmd import Cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City

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
    """Entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to
        JSON and prints the `id`
        """
        parsed_args = shlex.split(arg)
        try:
            if not parsed_args:
                print('** class name missing **')
                return
            elif parsed_args[0] not in classes:
                print("** class doesn't exist **")
                return

            params = parsed_args[1:]
            attributes = {}

            for param in params:
                if "=" not in param:
                    continue

                key, value = param.split("=", 1)
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                    value = value.replace("_", " ")
                    value.replace('\\"', '"')

                elif "." in value:
                    try:
                        value = float(value)
                    except ValueError:
                        continue

                else:
                    try:
                        value = int(value)
                    except ValueError:
                        continue

                attributes[key] = value

            new_obj = classes[parsed_args[0]](**attributes)
            new_obj.save()
            print(new_obj.id)

        except Exception as e:
            print(e)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print('** class name missing **')
            return False
        if parsed_args[0] in classes:
            if len(parsed_args) > 1:
                key = parsed_args[0] + '.' + parsed_args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id,
        save the changes in the JSON file"""
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
        key = class_name + '.' + parsed_args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of
        all instances based on class name"""
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print([str(obj) for obj in storage.all().values()])
            return
        class_name = parsed_args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        instances = [str(obj) for key, obj in storage.all().items() if key.startswith(class_name)]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attributes, saves
        changes into the JSON file
        """
        p_args = shlex.split(arg)
        if len(p_args) == 0:
            print('** class name missing **')
        if p_args[0] in classes:
            if len(p_args) > 1:
                key = p_args[0] + '.' + p_args[1]
                if key in storage.all():
                    instance = storage.all()[key]
                    if len(p_args) > 2:
                        if len(p_args) > 3:
                            setattr(instance, p_args[2], p_args[3])
                            instance.save()
                        else:
                            print('** value missing **')
                    else:
                        print('** attribute name missing **')
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print('** class doesn\'t exist **')

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
        elif command.startswith('destroy(') and command.endswith(')'):
            instance_id = command[len('destroy('):-1].strip('"')
            self.do_destroy(f"{class_name} {instance_id}")
        elif command.startswith('show(') and command.endswith(')'):
            instance_id = command[len('show('):-1].strip('"')
            self.do_show(f"{class_name} {instance_id}")
        else:
            print(f"*** Unknown syntax: {line}")

    def do_count(self, class_name):
        """Retrieve the number of instances of a class"""
        count = sum(1 for key in storage.all() if key.startswith(class_name))
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
