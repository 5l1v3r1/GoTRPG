import random
import sys
#House classes that contains game parameters
class Lannister():
   def __init__(self, name, starting_health=100, starting_gold=200, damage=25, gold_won=75):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Tywin Lannister"
      self.slogan="Hear Me Roar!!"

class Stark():
   def __init__(self, name, starting_health=160, starting_gold=100, damage=40, gold_won=65):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Eddard Stark"
      self.slogan = "Winter is Coming!!"

class Targaryen():
   def __init__(self, name, starting_health=135, starting_gold=135, damage=40, gold_won=60):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Daenerys Targaryen"
      self.slogan = "Fire and Blood!!"


class Arryn():
   def __init__(self,name,starting_health=145,starting_gold=145,damage=35, gold_won=60):
      self.name=name
      self.starting_gold=starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage=damage
      self.gold_won=gold_won
      self.hero = "Robert Arryn"
      self.slogan = "As High As Honor!!"

class Baratheon():
   def __init__(self, name, starting_health=125, starting_gold=125, damage=50, gold_won=50):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Stannis Baratheon"
      self.slogan = "Ours is the Fury!!"

class Bolton():
   def __init__(self, name, starting_health=120, starting_gold=130, damage=45, gold_won=60):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Roose Bolton"
      self.slogan = "Our Blades are Sharp!!"

class Greyjoy():
   def __init__(self, name, starting_health=160, starting_gold=140, damage=25, gold_won=75):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Theon Greyjoy"
      self.slogan = "We Don't Sow!!"

class Martell():
   def __init__(self, name, starting_health=120, starting_gold=150, damage=45, gold_won=50):
      


      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Prince Doran"
      self.slogan = "Unbowed,Unbent,Unbroken!!"

class Tarly():
   def __init__(self, name, starting_health=150, starting_gold=150, damage=25, gold_won=75):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Randyll Tarly"
      self.slogan = "First in Battle!!"

class Tully():
   def __init__(self, name, starting_health=140, starting_gold=140, damage=35, gold_won=65):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Edmure Tully"
      self.slogan = "Family,Duty,Honor!!"

class Tyrell():
   def __init__(self, name, starting_health=105, starting_gold=175, damage=40, gold_won=55):
      self.name = name
      self.starting_gold = starting_gold
      self.total_gold = starting_gold
      self.starting_health = starting_health
      self.total_health = starting_health
      self.damage = damage
      self.gold_won = gold_won
      self.hero = "Loras Tyrell"
      self.slogan = "Growing Strong!!"

#Dynamically inheritance house class to Player class
def select_house(house):

   class Player(house):
      #Who first attack to each other
      def who_first(self):
         return random.randint(0, 4)



      #Exit from game when user want to quit.
      def exit_game(self):
         print('See you later...')
         sys.exit()

      #Increases damage to enemy or you
      def do_damage(self, enemy, you):
         enemy.total_health -= you.damage

      #Display user statues

      def display_status(self):
         print('damage: ', self.damage)

         if self.total_health < 0:
            print('health: ',0)
         else:
            print('health: ', self.total_health)

      def select_damage(self, enemy):
         #Selects who first attack and make damage.
         result = self.who_first()

         if result == 0:
            print('\nResult: You damaged by your enemy' '\n')
            self.do_damage(you, enemy)

         if result == 1 or result == 2 or result == 3 or result == 4:
            print('\nResult: Enemy damaged by you' '\n')
            self.do_damage(enemy, you)
         #If enemy lose

         if enemy.total_health < 1:
            print ('This round is over!')
            print(you.name + ' is winner of this round')
            print()
            print("† " + you.slogan + " †")
            print()

            you.total_gold = you.total_gold + you.gold_won
            if you.total_gold >= you.starting_gold:
               you.total_gold = you.starting_gold
            else:
               pass
            print('Total gold:' + str(you.total_gold))
            print("Health of your Hero:" + str(you.total_health))
            print()
            #buy health point
            print("Do you wanna buy some health point? (1 health point = 1 gold)")
            try:
               amount = int(input('\n> '))
               print()
               if not (0 <= amount <= you.total_gold and 0 <= amount <= you.starting_health - you.total_health):
                  raise ValueError()
            except ValueError:
               print ("Invalid value, amount isn't bigger than you gold and negative. Or your Total health exceed your starting health.")
               print ()

            else:
               you.total_gold -= amount
               you.total_health += amount
               print("Total Gold:" + str(you.total_gold))


               print("Total Health:" + str(you.total_health))
         #If you lose
         elif you.total_health < 1:
            print ('This round is over!')
            print(enemy.hero + ' is winner of this round')
   return Player


logo = """\
                                                                    
                               '...............................,    
   @   @                          @                            `    
  @        '   #      +:'         @ @   @ @,@   +;'` @   .. @;@ # # 
 +`        @   @   '` ;    .` .`  @ @   @ @  ; @ ; ' @@     @   +   
 #        #.   +@  :+ ;`, @` .:   @ @;;;@ @   `` ;  :@ @    @`' ';  
 +,    @  +'@  ',`; @ ;   #` ;:   @ @   @ @,@ `. ;  '@  @   @ `  :' 
  @    @ .  @  . @: @ ;    ., ;   @ @   @ @  + @ ; . @  `+  @     @ 
  ;@   @ @  .@`; `  @.##;         @ @`  @ @. .+ #';  @`  `  @:@ ';  
    #@@,                         ';;             		

                       
"""       
print(logo)
#Ask new player when you lose
while True:
   name = input('Player Name:')
   gender = input('Gender (Male or Female):')

   print('Select House:',
        '1. Lannister ',
        '2. Stark ',
        '3. Targaryen',
        '4. Arryn',
        '5. Baratheon',
        '6. Bolton',
        '7. Greyjoy',
        '8. Martell',
        '9. Tarly',
        '10. Tully',
        '11. Tyrell',
         sep='\n')
   #Select your house
   house = input('Which house you are belong to? :')
#Generate enemy list randomly and choose your house.
   house_list = [Lannister,Stark,Targaryen,Arryn,Baratheon,Bolton,Greyjoy,Martell,Tarly,Tully,Tyrell]
   random.shuffle(house_list)

   if house == "1":
      you = select_house(Lannister)(name[0].upper()+name[1:] + " Lannister")
      del house_list[0]
   elif house == "2":
      you = select_house(Stark)(name[0].upper()+name[1:] + " Stark")
      del house_list[1]
   elif house == "3":
      you = select_house(Targaryen)(name[0].upper()+name[1:] + " Targaryen")
      del house_list[2]
   elif house == "4":
      you = select_house(Arryn)(name[0].upper()+name[1:] + " Arryn")
      del house_list[3]
   elif house == "5":
      you = select_house(Baratheon)(name[0].upper()+name[1:] + " Baratheon")
      del house_list[4]



   elif house == "6":
      you = select_house(Bolton)(name[0].upper()+name[1:] + " Bolton")
      del house_list[5]
   elif house == "7":
      you = select_house(Greyjoy)(name[0].upper()+name[1:] + " Greyjoy")
      del house_list[6]
   elif house == "8":
      you = select_house(Martell)(name[0].upper()+name[1:] + " Martell")
      del house_list[7]
   elif house == "9":
      you = select_house(Tarly)(name[0].upper()+name[1:] + " Tarly")
      del house_list[8]
   elif house == "10":
      you = select_house(Tully)(name[0].upper()+name[1:] + " Tully")
      del house_list[9]
   elif house == "11":
      you = select_house(Tyrell)(name[0].upper()+name[1:] + " Tyrell")
      del house_list[10]

   #Choose enemies and fight with them
   x=1
   while x<=10:
      enemy = select_house(house_list[x-1])(" ")
      print(x)
      x+=1
      print('Enemy Name: ' + enemy.hero)
      print('Name: ' + (you.name))
      print('Gender:' + (gender[0].upper()+gender[1:]))
      print()
      print('Your starting gold:'+str(you.total_gold))
      print("Enemy's starting gold:" + str(enemy.starting_gold))
      print()
      while you.total_health>0 and enemy.total_health>0:
         print('Your total health:' + str(you.total_health))
         print('Enemy total health:'+ str(enemy.total_health))
         print()

         print('You are facing with your enemy right now.' '\n',
              'What is your move?: ',
              'Fight:  s',
              'Quit:   q', sep='\n')

         move = input('\n> ')

         if move == 's':
            you.select_damage(enemy)

            print('Status of  enemy:')
            enemy.display_status()
            print()
            print('Your status:')
            you.display_status()
            print()

         if move == 'q':
            you.exit_game()



      #If you beat 10 enemies, you win the game and ascend Iron Throne. (And starts new game.)

      if x == 11:
         if you.total_health > 0:
            print( "† "+ "You win the game.You reach the Iron Throne" + " † " )
