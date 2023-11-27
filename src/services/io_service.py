class IOService:
    def read(self, prompt):
        return input(prompt)

    def write(self, value):
        print(value)

class StubIOService:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)
# pylint: disable=W0613
    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return "4"

    def add_input(self, value):
        self.inputs.append(value)

    def reset_outputs(self):
        self.outputs = []
