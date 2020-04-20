import math
#Creation de la classe robot:
class Robot:

    def __init__(self, position_x, position_y, objectif_x, objectif_y, orientation_depart,orientation_arrive, couleur, gobelet):
        self.position_x = position_x #position courante en x (converti par une fonction de conversion)
        self.position_y = position_y #position courante en y (converti par une fonction de conversion)
        self.objectif_x = objectif_x #position objectif en x (converti par une fonction de conversion)
        self.objectif_y = objectif_y #position objectif en y (converti par une fonction de conversion)
        self.orientation_depart = orientation_depart #orientation du robot entre 0 (vertical haut) et 359
        self.orientation_arrive =  orientation_arrive
        self.couleur = couleur
        self.gobelet = gobelet # Nombre de gobelet dans le robot

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

    def deplacement_robot(self, canvas):
        posx= self.position_x
        posy = self.position_y
        posx_fin = self.objectif_x
        posy_fin = self.objectif_y
        if self.couleur==0:

            while posx != posx_fin or posy != posy_fin:
                canvas.coords(canvas.find_withtag("robot1"), posx-30, posy-30, posx+30, posy+30)
                canvas.coords(canvas.find_withtag("angle_robot1"), posx, posy, posx+30*(math.cos(math.radians(self.orientation_arrive))), posy+30*(math.sin(math.radians(self.orientation_arrive))))

                #canvas.move(canvas.find_withtag("robot1"), posx, posy)

                if posx == posx_fin and posy != posy_fin:
                    posy += 1

                elif posy==posy_fin and posx!=posx_fin:
                    posx += 1
                else:
                    posx+=1
                    posy+=1
                self.position_x=posx
                self.position_y=posy

            print("posx=",self.position_x)
            print("posy=",self.position_y)
        if self.couleur==1:
            while posx != posx_fin or posy != posy_fin:
                canvas.coords(canvas.find_withtag("robot2"), posx - 30, posy - 30, posx + 30, posy + 30)
                canvas.coords(canvas.find_withtag("angle_robot2"), posx, posy,
                              posx + +30 * (math.cos(math.radians(self.orientation_arrive))),
                              posy + +30 * (math.sin(math.radians(self.orientation_arrive))))

                # canvas.move(canvas.find_withtag("robot1"), posx, posy)

                if posx == posx_fin and posy != posy_fin:
                    posy += 1

                elif posy == posy_fin and posx != posx_fin:
                    posx += 1
                else:
                    posx += 1
                    posy += 1
                self.position_x = posx
                self.position_y = posy

            print("posx=", self.position_x)
            print("posy=", self.position_y)
