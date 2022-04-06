from classes.grid_object import GridObject

#Defines what constitutes as obstacles or "terrain"
class Terrain(GridObject):

    def __init__(self, terrainType):
        self.terrainType = terrainType
        self.cellText = "*"
