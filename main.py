import visuals
import proccessing


class Main:
    def __init__(self):
        self.objs = []
        self.visuals = visuals.Main(self)
        self.process = proccessing.Main(self)

main = Main()
main.visuals.run()
