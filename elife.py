HP=80
PO=76
Speed=85
G=0
myvar = 9
HPG=50
POG=85
SpeedG=10
GG=500

#def die():
#   global HP
 #  if HP<=0:
  #     print("You lost because you have no HP anymore! Good luck when you choose the next choice .)

def choice():
   global PO
   global G
   c1=input("Right or Left?")
   if c1=="left":
       print("Cool! You got 200 gold and a magic bracelet which will increase your strenth by 10")
       PO = PO+10
       G=G+200
       print("Your life is",HP,"Your strength is",PO,"Your speed is ",Speed,"Your money is" ,G)
       print("Now you have to go to the right.")
       choice2()
   elif c1=="right":
       print("You are attacked by a Gorgan")
       choice2()
       
def choice2():
   #die()
   c2=input("Fight or Flee")
   if c2=="fight":
       fight()
   elif c2=="flee":
       flee()
       
def fight():
   global HP
   global PO
   global HPG
   global POG
   global G
   global GG
   if HP>HPG and PO>POG:
       G=G+GG
       print("Because you are so talant, you don't even lose one blood. Your life is now ",HP,"You win")
       print("Your rewards are 500 gold!!!","Your gold become",G,"now. Keep moving")
   elif HP>HPG and PO<POG:
       HP=HP-20
       print("You lose, make the choice again","Your life is now ",HP)
       choice2()
   elif HP<HPG and PO>POG:
       HP=HP-20,
       print("You lose, make the choice again","Your life is now ",HP)
       choice2()
   elif HP<HPG and PO<POG:
       HP=HP-50
       print("Gorgan beat you down, make the choice again","Your life is now ",HP)
       choice2()

def flee():
   Speed=85
   SpeedG=10
   if Speed>SpeedG:
       print("You fall back! Make the choice again!")
       choice2()
   elif Speed<SpeedG:
       HP=HP-50
       print("You were caught and got beated, make the choice again","Your life is now ",HP)
       choice2()
   
choice()
       


#Choice1= input("You r in a dungeon and come to a fork. Right or Left?")
#if Choice1=="left":
#    print("Lucky! You got 200 gold and a magic bracelet which will increase your strenth by 10")
#    PO=PO+10
#    G=G+200
#    print(HP,PO,Speed,G)
   
       
#elif Choice1=="right":
#    print("WOO! You attacked by a Gorgan")
#    Choice2= input("Fight or Flee")
#   if Choice2=="fight":
#       fight(HP)