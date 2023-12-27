class CommonSmallEntity:
    black: str = "#000000"
    white: str = "#FFFFFF"

    def __init__(self, options):
        self.black=options["black"]
        self.white=options["white"]