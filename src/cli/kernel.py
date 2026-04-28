class Kernel:
    def __init__(self, Shell, Loader, Executor, Replacer):
        self.Shell = Shell
        self.Loader = Loader
        self.Executor = Executor
        self.Replacer = Replacer

    def startup(self):
        self.Replacer.replace()

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