import os

class Command:
    def __init__(self):
        ...

    def build(self, name: str):
        if not os.path.exists(f"commands/{name}"):
            current_dir = os.getcwd()
            
            os.chdir("commands/")
            os.mkdir(name)
            os.chdir(name)
            os.mkdir("src")

            metadata = {
                "enabled": True,

                "name": f"{name}",
                "version": "0.0",
                "author": f"{os.getlogin()}",
                "description": "",

                "usage": "",
                "aliases": [],
                "entry": "src/run.py",
                "requirements": [],
                "invisible": False,
                "supered": False,

                "index": ""
            }

            # yeah i know its complicated
            with open("metadata.json", "a", encoding="utf-8") as file:
                file.write('{\n')
                file.write('    "enabled": true,\n')
                file.write('\n')
                file.write(f'    "name": "{name}",\n')
                file.write(f'    "type": null,\n')
                file.write('    "version": 0.1,\n')
                file.write(f'    "author": "{os.getlogin()}",\n')
                file.write('    "usage": "",\n')
                file.write('    "description": "",\n')
                file.write('\n')
                file.write('    "aliases": [],\n')
                file.write('    "entry": "src/run.py",\n')
                file.write('    "requirements": [],\n')
                file.write('    "invisible": false,\n')
                file.write('    "supered": false,\n')
                file.write('\n')
                file.write('    "index": null\n')
                file.write('}')

            with open("config.yml", "a", encoding="utf-8") as file:
                file.write("# this file can be configured by user\n")
                file.write("# by using \"[command] configurate\" user can change command preferences\n")

            with open("src/run.py", "w", encoding="utf-8") as file:
                file.write("def run(args):\n")
                file.write("    return \"Hello, World!\"")

            with open("src/__init__.py", "w", encoding="utf-8") as file:
                file.write("")

            os.chdir(current_dir)

            return None
            
        return "it exists"