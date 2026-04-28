class Executor:
    def __init__(self, path):
        self.path = path

    def exec(self, module, args):
        try:
            return module.run(args)
        
        except AttributeError:
            return None