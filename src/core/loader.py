import importlib, json, os

class Loader:
    def __init__(self):
        ...

    def load_module(self, command):
        for subdir in os.listdir("commands/"):
            with open(f"commands/{subdir}/metadata.json", "r", encoding="utf-8") as file:
                metadata = json.load(file)
                if command in metadata["aliases"]:
                    module_path = f"commands/{subdir}/{metadata['entry']}"
                    break
        
        try:
            spec = importlib.util.spec_from_file_location(f"{metadata['entry'].split('/')[-1]}", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
            
        except FileNotFoundError:
            return "exec wasnt found"