from tkinter import *
from robot import *
import math

# Construction de la fenêtre principale «root»
fenetre = Tk()
fenetre.title('Simulation')

# Personalisation fenetre
fenetre.geometry("1080x720")
fenetre.config(background="#3366CC")
frametable = Frame(fenetre)

# Placement table dans la fenetre
hauteur = 520
largeur = 778
table = PhotoImage(file="table2020.png")
canvas_table = Canvas(fenetre, width=largeur*1.5, height=hauteur,bg="#3366CC",bd = "0", highlightthickness="0")
canvas_table.create_image(largeur/2, hauteur/2, image=table)
canvas_table.pack(side="top")

###################################################################
robot1 = Robot(40,170,60,460,0,90,0,0)
robot2 = Robot(40,240,311,442,0,90,1,0)
RCVA = Robot(700,190,160,210,0,0,2,0)
#Fonction de correspondance simulateur/réalité
def correspondance_x(posx_reel):
    posx_simu = posx_reel*(778/3000)-15/2
    return posx_simu
def correspondance_y(posy_reel):
    posy_simu = posy_reel*(778/3000)-15/2
    return posy_simu

#Fonction de placement de robot

def place_robot(robot):
    if robot.couleur == 0:
        robot1_cercle = canvas_table.create_oval(robot.position_x-30, robot.position_y-30, robot.position_x + 30, robot.position_y + 30, fill="blue",tags="robot1")
        robot1_angle = canvas_table.create_line(robot.position_x,robot.position_y,robot.position_x+30*(math.cos(math.radians(robot.orientation_depart))),robot.position_y+30*(math.sin(math.radians(robot.orientation_depart))),tags="angle_robot1")

    if robot.couleur == 1:
        robot2_cercle =canvas_table.create_oval(robot.position_x-30, robot.position_y-30, robot.position_x + 30, robot.position_y + 30, fill="blue",tags="robot2")
        robot2_angle =canvas_table.create_line(robot.position_x,robot.position_y,robot.position_x+30*(math.cos(math.radians(robot.orientation_depart))),robot.position_y+30*(math.sin(math.radians(robot.orientation_depart))),tags="angle_robot2")


    if robot.couleur == 2:
        RCVA_cercle = canvas_table.create_oval(robot.position_x-30, robot.position_y-30, robot.position_x + 30, robot.position_y + 30,fill="yellow",tags="RCVA")

#Fonction pour déplacer le robot adverse à la souris
def deplacer(event):
    cercle = canvas_table.find_withtag("RCVA")
    canvas_table.coords(cercle, event.x - 30,event.y - 30, event.x+30,event.y+30)
    RCVA.nouvelle_position(event.x,event.y)

    #print("posx robot RCVA=", RCVA.position_x)
    #print("posy robot RCVA=", RCVA.position_y)

#Fonction de placement de gobelet
def place_gobelet():
    canvas_table.create_oval(correspondance_x(300), correspondance_y(400), correspondance_x(300) + 15, correspondance_y(400) + 15, fill="red",tags="gob1")
    canvas_table.create_oval(correspondance_x(450), correspondance_y(1080), correspondance_x(450) + 15, correspondance_y(1080) + 15, fill="red",tags="gob2")
    canvas_table.create_oval(correspondance_x(1100), correspondance_y(800), correspondance_x(1100) + 15, correspondance_y(800) + 15, fill="red",tags="gob3")
    canvas_table.create_oval(correspondance_x(1730), correspondance_y(1200), correspondance_x(1730) + 15, correspondance_y(1200) + 15, fill="red",tags="gob4")
    canvas_table.create_oval(correspondance_x(2050), correspondance_y(400), correspondance_x(2050) + 15, correspondance_y(400) + 15, fill="red",tags="gob5")
    canvas_table.create_oval(correspondance_x(2550), correspondance_y(510), correspondance_x(2550) + 15, correspondance_y(510) + 15, fill="red",tags="gob6")
    canvas_table.create_oval(correspondance_x(2700), correspondance_y(1200), correspondance_x(2700) + 15, correspondance_y(1200) + 15, fill="red",tags="gob7")
    canvas_table.create_oval(correspondance_x(1005), correspondance_y(1955), correspondance_x(1005) + 15, correspondance_y(1955) + 15, fill="red",tags="gob8")
    canvas_table.create_oval(correspondance_x(1335), correspondance_y(1650), correspondance_x(1335) + 15, correspondance_y(1650) + 15, fill="red",tags="gob9")
    canvas_table.create_oval(correspondance_x(1605), correspondance_y(1955), correspondance_x(1605) + 15, correspondance_y(1955) + 15, fill="red",tags="gob10")
    canvas_table.create_oval(correspondance_x(1935), correspondance_y(1650), correspondance_x(1935) + 15, correspondance_y(1650) + 15, fill="red",tags="gob11")
    canvas_table.create_oval(correspondance_x(670), correspondance_y(100), correspondance_x(670) + 15,correspondance_y(100) + 15, fill="red",tags="gob12")

    canvas_table.create_oval(correspondance_x(300), correspondance_y(1200), correspondance_x(300) + 15, correspondance_y(1200) + 15, fill="green",tags="gob13")
    canvas_table.create_oval(correspondance_x(450), correspondance_y(510), correspondance_x(450) + 15, correspondance_y(510) + 15, fill="green",tags="gob14")
    canvas_table.create_oval(correspondance_x(950), correspondance_y(400), correspondance_x(950) + 15, correspondance_y(400) + 15, fill="green",tags="gob15")
    canvas_table.create_oval(correspondance_x(1270), correspondance_y(1200), correspondance_x(1270) + 15, correspondance_y(1200) + 15, fill="green",tags="gob16")
    canvas_table.create_oval(correspondance_x(1900), correspondance_y(800), correspondance_x(1900) + 15, correspondance_y(800) + 15, fill="green",tags="gob17")
    canvas_table.create_oval(correspondance_x(2330), correspondance_y(100), correspondance_x(2330) + 15, correspondance_y(100) + 15, fill="green",tags="gob18")
    canvas_table.create_oval(correspondance_x(1395), correspondance_y(1955), correspondance_x(1395) + 15, correspondance_y(1955) + 15, fill="green",tags="gob19")
    canvas_table.create_oval(correspondance_x(1065), correspondance_y(1650), correspondance_x(1065) + 15, correspondance_y(1650) + 15, fill="green",tags="gob20")
    canvas_table.create_oval(correspondance_x(1665), correspondance_y(1650), correspondance_x(1665) + 15, correspondance_y(1650) + 15, fill="green",tags="gob21")
    canvas_table.create_oval(correspondance_x(1995), correspondance_y(1955), correspondance_x(1995) + 15, correspondance_y(1955) + 15, fill="green",tags="gob22")
    canvas_table.create_oval(correspondance_x(2700), correspondance_y(400), correspondance_x(2700) + 15, correspondance_y(400) + 15, fill="green",tags="gob23")
    canvas_table.create_oval(correspondance_x(2550), correspondance_y(1080), correspondance_x(2550) + 15, correspondance_y(1080) + 15, fill="green",tags="gob24")

def detection():
    detectionrobot1 = 0
    detectionrobot2 = 0
    tuplerobot1 = canvas_table.find_overlapping(robot1.position_x-30, robot1.position_y-30, robot1.position_x + 30, robot1.position_y + 30)
    tuplerobot2 = canvas_table.find_overlapping(robot2.position_x - 30, robot2.position_y - 30, robot2.position_x + 30,
                                        robot2.position_y + 30)
    for i in range(0, len(tuplerobot1)):
        if tuplerobot1[i] == 6:
            detectionrobot1 = 1
    for i in range(0, len(tuplerobot2)):
        if tuplerobot2[i] == 6:
            detectionrobot2 = 1

    #print(canvas_table.find_overlapping(robot1.position_x - 30, robot1.position_y - 30, robot1.position_x + 30,
                                       # robot1.position_y + 30))
    #print(detectionrobot1)
    #print(detectionrobot2)
    fenetre.after(100, lambda : detection())

def collision_gobelet():
    tuplerobot1 = canvas_table.find_overlapping(RCVA.position_x - 30, RCVA.position_y - 30, RCVA.position_x + 30,
                                                RCVA.position_y + 30)
    tuplerobot2 = canvas_table.find_overlapping(robot2.position_x - 30, robot2.position_y - 30, robot2.position_x + 30,
                                                robot2.position_y + 30)
    for i in  range(0,len(tuplerobot1)):
        for j in range(7,32):
            if tuplerobot1[i] == j:
                canvas_table.delete(j)
                robot1.gobelet += 1
    for i in range(0, len(tuplerobot2)):
        for j in range(7, 32):
            if tuplerobot2[i] == j:
                canvas_table.delete(j)
                robot2.gobelet += 1
    print("Nombre gobelet= ", robot1.gobelet)



    fenetre.after(500, lambda: collision_gobelet())


place_robot(robot1)
place_robot(robot2)
place_robot(RCVA)
place_gobelet()

#fenetre.bind("<Button-2>",deplacement_robot1(40,170,150,280))
Lancementrobot1 = Button(fenetre, text="Lancer le premier robot !", command = lambda : robot1.deplacement_robot(canvas_table))
Lancementrobot2 = Button(fenetre, text="Lancer le deuxième robot !", command = lambda : robot2.deplacement_robot(canvas_table))

Lancementrobot1.pack()
Lancementrobot2.pack()
fenetre.bind("<B1-Motion>",deplacer)
# Lancement de la «boucle principale»
fenetre.after(100, lambda : detection())
fenetre.after(500, lambda: collision_gobelet())

#fenetre.after(100, lambda : collision(robot2))

fenetre.mainloop()





