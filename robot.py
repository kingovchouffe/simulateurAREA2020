#Creation de la classe robot
class Robot:
    def __init__(self, position_x, position_y, objectif_x, objectif_y, couleur):
        self.position_x = position_x
        self.position_y = position_y
        self.objectif_x = objectif_x
        self.objectif_y = objectif_y
        self.couleur = couleur

    def nouvelle_position(self,pos_x, pos_y):
        self.position_x = pos_x
        self.position_y = pos_y

    def nouvel_objectif(self,posobj_x, posobj_y):
        self.objectif_x = posobj_x
        self.objectif_y = posobj_y
    def position_x(self):
        return self.position_x
    def position_y(self):
        return self.position_y

