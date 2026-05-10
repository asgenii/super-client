import importlib, yaml, os

class Loader:
    def __init__(self, path):
        self.path = path

    def load_module(self, command):
        found = False
        for paths in ["commands/system", "commands/user"]:
            if found:
                break

            for subdir in os.listdir(paths):
                with open(f"{paths}/{subdir}/config.yml", "r", encoding="utf-8") as file:
                    config = yaml.safe_load(file)
                    config_general = config["command"]["name"]["general"]
                    config_additional = config["command"]["name"]["additional"]

                if command == config_general or command == config_additional:
                    module_path = f"{paths}/{config_general}/src/exec.py"
                    found = True
                    break

        if not found:
            return "command wasnt found"
        
        try:
            spec = importlib.util.spec_from_file_location("exec.py", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
            
        except FileNotFoundError:
            return "exec wasnt found"