#!/usr/bin/env python
import subprocess
import sys
from argparse import ArgumentParser, Namespace
from collections.abc import Iterator


def run_command(command: str) -> bool:
    try: 
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as error:
        print(f"{error}")
        return False


class CommandPipeline:
    def __init__(self) -> None:
        self._commands: list[str] = []
                   
    def add_command(self, command: str) -> "CommandPipeline":
        self._commands.append(command)
        return self

    def __iter__(self) -> Iterator[str]:
        return iter(self._commands)

def main(pipeline: CommandPipeline) -> None:
    for command in pipeline:
        if not run_command(command):
            sys.exit(1)


if __name__ == "__main__":
    
    commands: CommandPipeline = CommandPipeline()
    #default commands
    commands.add_command("mypy .")\
            .add_command("ruff check . --fix")

    parser: ArgumentParser = ArgumentParser()

    parser.add_argument("-m" ,
                        "--run_migrations", 
                        action="store_true", 
                        help="Run command makemigrations and migrate")

    parser.add_argument("-r" ,
                        "--run_server", 
                        action="store_true", 
                        help="run server")

    parser.add_argument("-c" ,
                        "--create_user", 
                        action="store_true", 
                        help="run server")

    args:Namespace = parser.parse_args()


    if args.create_user:
        commands.add_command("python manage.py createsuperuser")

    if args.run_migrations:
        commands.add_command("python manage.py makemigrations")\
        .add_command("python manage.py migrate")
    
    if args.run_server:
        commands.add_command("python manage.py runserver")

    main(commands)