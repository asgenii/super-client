import importlib, yaml, os

class Loader:
    def __init__(self, path):
        self.path = path

    def load_module(self, command):
        found = False
        for paths in [self.path, "src/cli/internal/commands"]:
            for path in os.listdir(paths):
                with open(f"{paths}/{path}/config.yml", "r", encoding="utf-8") as file:
                    config = yaml.safe_load(file)
                    config_general = config["command"]["name"]["general"]
                    config_additional = config["command"]["name"]["additional"]

                if command == config_general or command == config_additional:
                    return config_general, True

                if found == False:
                    return "command wasnt found" # create log i guess?
        
        try:
            spec = importlib.util.spec_from_file_location("exec.py", f"{self.path}/{config_general}/src/exec.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
            
        except FileNotFoundError:
            return "exec wasnt found"