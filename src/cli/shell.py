class Shell:
    def __init__(self, prompt):
        self.prompt = prompt

    def input(self):
        data: str = input(self.prompt)
        return data