#Creation de la classe robot:
class Robot:
    def __init__(self, position_x, position_y, objectif_x, objectif_y, orientation, couleur):
        self.position_x = position_x #position courante en x (converti par une fonction de conversion)
        self.position_y = position_y #position courante en y (converti par une fonction de conversion)
        self.objectif_x = objectif_x #position objectif en x (converti par une fonction de conversion)
        self.objectif_y = objectif_y #position objectif en y (converti par une fonction de conversion)
        self.orientation = orientation #orientation du robot entre 0 (vertical haut) et 359
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


