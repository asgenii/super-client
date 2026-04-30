import os, yaml

class Command:
    def __init__(self, path: str):
        self.path = path

    def build(self, data: dict):
        """
        str "catalog"        : command's catalog name
        str "general"        : main name of command
        list "additional"    : additional names for command
        str "description"    : command's description
        """
        current_dir = os.getcwd()

        os.chdir(self.path)
        os.mkdir(data["catalog"])
        os.chdir(data["catalog"])

        config = {
            "command": {
                "name": {
                    "general": data["general"],
                    "additional": data["additional"]
                },
                "description": data["description"]
            },
        }
        
        with open("config.yml", "w", encoding="utf-8") as file:
            yaml.dump(config, file, sort_keys=False, allow_unicode=True)

        os.mkdir("src")
        os.chdir("src")
        
        with open("exec.py", "w", encoding="utf-8") as file:
            file.write("def run(args):\n    return \"Hello World!\"")

        os.chdir(current_dir)