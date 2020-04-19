from tkinter import *
from robot import *
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
robot1 = Robot(40,150,60,480,0)
robot2 = Robot(40,210,311,442,0)
RCVA = Robot(712,210,160,210,1)
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
        canvas_table.create_oval(robot.position_x, robot.position_y, robot.position_x + 60, robot.position_y + 60, fill="blue")
    else:
        RCVA_cercle = canvas_table.create_oval(robot.position_x, robot.position_y, robot.position_x + 60, robot.position_y + 60,fill="yellow")
#Fonction pour déplacer le robot adverse à la souris
def deplacer(event):
    cercle =  canvas_table.find_withtag("current")[0]
    souris = canvas_table.find_closest(event.x, event.y)
    canvas_table.move(cercle, event.x-canvas_table.coords(souris[0])[0] ,event.y-canvas_table.coords(souris[0])[1])

#Fonction de placement de gobelet
def place_gobelet():
    canvas_table.create_oval(correspondance_x(300), correspondance_y(400), correspondance_x(300) + 15, correspondance_y(400) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(450), correspondance_y(1080), correspondance_x(450) + 15, correspondance_y(1080) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(1100), correspondance_y(800), correspondance_x(1100) + 15, correspondance_y(800) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(1730), correspondance_y(1200), correspondance_x(1730) + 15, correspondance_y(1200) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(2050), correspondance_y(400), correspondance_x(2050) + 15, correspondance_y(400) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(2550), correspondance_y(510), correspondance_x(2550) + 15, correspondance_y(510) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(2700), correspondance_y(1200), correspondance_x(2700) + 15, correspondance_y(1200) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(1005), correspondance_y(1955), correspondance_x(1005) + 15, correspondance_y(1955) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(1335), correspondance_y(1650), correspondance_x(1335) + 15, correspondance_y(1650) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(1605), correspondance_y(1955), correspondance_x(1605) + 15, correspondance_y(1955) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(1935), correspondance_y(1650), correspondance_x(1935) + 15, correspondance_y(1650) + 15, fill="red")
    canvas_table.create_oval(correspondance_x(670), correspondance_y(100), correspondance_x(670) + 15,correspondance_y(100) + 15, fill="red")

    canvas_table.create_oval(correspondance_x(300), correspondance_y(1200), correspondance_x(300) + 15, correspondance_y(1200) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(450), correspondance_y(510), correspondance_x(450) + 15, correspondance_y(510) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(950), correspondance_y(400), correspondance_x(950) + 15, correspondance_y(400) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(1270), correspondance_y(1200), correspondance_x(1270) + 15, correspondance_y(1200) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(1900), correspondance_y(800), correspondance_x(1900) + 15, correspondance_y(800) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(2330), correspondance_y(100), correspondance_x(2330) + 15, correspondance_y(100) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(1395), correspondance_y(1955), correspondance_x(1395) + 15, correspondance_y(1955) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(1065), correspondance_y(1650), correspondance_x(1065) + 15, correspondance_y(1650) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(1665), correspondance_y(1650), correspondance_x(1665) + 15, correspondance_y(1650) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(1995), correspondance_y(1955), correspondance_x(1995) + 15, correspondance_y(1955) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(2700), correspondance_y(400), correspondance_x(2700) + 15, correspondance_y(400) + 15, fill="green")
    canvas_table.create_oval(correspondance_x(2550), correspondance_y(1080), correspondance_x(2550) + 15, correspondance_y(1080) + 15, fill="green")




place_robot(robot1)
place_robot(robot2)
place_robot(RCVA)
place_gobelet()
fenetre.bind("<B1-Motion>",deplacer)
# Lancement de la «boucle principale»
fenetre.mainloop()





