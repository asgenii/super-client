import os, yaml, json

class Replacer:
    def __init__(self, path: str):
        self.path = path

    def replace(self):
        if not os.path.exists(f"{self.path}/.original.index.json"):
            with open(f"{self.path}/.original/index.json", "w", encoding="utf-8") as file:
                file.write("{}")

        for plugin in os.listdir(self.path):
            if not plugin.startswith("."):
                with open(f"{self.path}/{plugin}/replace.yml", "r", encoding="utf-8") as file:
                    data = yaml.safe_load(file)

                for n in data:
                    with open(data[n], "r", encoding="utf-8") as old_file:
                        with open(f"{self.path}/.original/{data[n].split('/')[-1]}", "w", encoding="utf-8") as snapshot_of_old_file:
                            snapshot_of_old_file.write(old_file.read())

                        with open(f"{self.path}/.original/index.json", "r", encoding="utf-8") as file:
                            index = json.load(file)
                            index[data[n].split("/")[-1]] = data[n]

                    with open(f"{self.path}/.original/index.json", "w", encoding="utf-8") as file:
                        json.dump(index, file, indent=4, ensure_ascii=True)

                    with open(f"{self.path}/{plugin}/new/{n}", "r", encoding="utf-8") as new_file:
                        with open(data[n], "w", encoding="utf-8") as replace_new_file:
                            replace_new_file.write(new_file.read())