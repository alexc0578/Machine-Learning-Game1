class GridCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cellObject = None

    def coordString(self):
        return str(self.x) + "," + str(self.y)

    def setCellObject(self, cellObject):
        if  cellObject is not None:
            cellObject.gridCell = self
            
        self.cellObject = cellObject