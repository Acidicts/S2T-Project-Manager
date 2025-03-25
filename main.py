import visuals
import proccessing
import Record.record
from Record.record import record_audio


class Main:
    def __init__(self):
        self.objs = []
        self.visuals = visuals.Main(self)
        self.process = proccessing.Main(self)

    def audio(self):
        audio = record_audio()
        print(audio)
        self.process.ev(audio)

main = Main()
main.visuals.run()
