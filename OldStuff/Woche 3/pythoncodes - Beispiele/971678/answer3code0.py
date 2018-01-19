import itertools
for cell in itertools.chain(*self.cells):
    cell.drawCell(surface, posx, posy)
