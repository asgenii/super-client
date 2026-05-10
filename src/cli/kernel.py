class Kernel:
    def __init__(self, Shell, Loader, Executor):
        self.Shell = Shell
        self.Loader = Loader
        self.Executor = Executor

    def startup(self):
        print("[OK]")

    def run(self):
        self.startup()
        while True:
            data = self.Shell.input()
            command = data.split(" ")[0] # will replace to parser
            args = data.split(" ")[1:]
            
            module = self.Loader.load_module(command)
            result = self.Executor.exec(module, args)

            if result != None:
                print(result)