import os, yaml

class Plugin:
    def __init__(self, path: str):
        self.path = path

    def build(self, data: dict):
        """
        str "catalog"        : plugin's catalog name
        str "general"        : main name of plugin
        str "description"    : plugin's description
        """
        current_dir = os.getcwd()

        os.chdir(self.path)
        os.mkdir(data["catalog"])
        os.chdir(data["catalog"])
        os.mkdir("new")

        config = {
            "plugin": {
                "general": data["general"],
                "description": data["description"]
            }
        }

        with open("config.yml", "w", encoding="utf-8") as file:
            yaml.dump(config, file, sort_keys=False, allow_unicode=True)

        with open("replace.yml", "w", encoding="utf-8") as file:
            yaml.dump({}, file, sort_keys=False, allow_unicode=True)

        os.chdir(current_dir)