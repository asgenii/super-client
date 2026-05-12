class Executor:
    def __init__(self):
        ...

    def exec(self, module, args):
        try:
            return module.run(args)
        
        except Exception as e:
            return e