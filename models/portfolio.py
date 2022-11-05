class Portfolio:
    def __init__(self):
        self.tokens = list()

    def get_tokens(self):
        return sorted(self.tokens, key=lambda x: x.name, reverse=False)
