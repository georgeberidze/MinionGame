"""
Name: George Beridze
Last Modified: March 7, 2021
Description: Assignment 4
"""
### CLASSES & INHERITANCE

class Character:
  '''represents characters in the game'''
  def __init__(self, name, lvl = 1, hp = 100, at = 10, df = 1, exp = 1):
    self.name = name
    self.lvl = lvl
    self.hp = hp
    self.at = at
    self.df = df
    self.exp = exp
    self.maxhp = hp

  def rename(self, name):
    '''changes character's name'''
    self.name = name

  def setlvl(self, lvl):
    '''sets character level'''
    self.lvl = lvl  

  def sethp(self, hp):
    ''' sets the character's hp to a new value or 0 (if hp is below 0)'''
    if hp <= 0:
        'health is less than or equal to 0'
        self.hp = 0
    else:
        'health is more than 0'
        try:
            self.hp = int(hp)
        except:
            self.hp = hp

  def setat(self, at):
    '''sets character attack level'''
    self.at = at    

  def setdf(self, df):
    '''sets character defense level'''
    self.df = df

  def setexp(self, exp):
    '''sets character experience'''
    self.exp = exp   

  def getname(self):
    '''returns character's name'''
    return self.name 

  def getlvl(self):
    '''returns character's level'''
    return self.lvl   

  def gethp(self):
    '''returns character's health level'''
    return self.hp   

  def getat(self):
    '''returns character's attack'''
    return self.at   

  def getdf(self):
    '''returns character's defence'''
    return self.df  

  def getexp(self):
    '''returns character's experience level'''
    return self.exp        

  def attack(self, other):
    '''attacks another character'''
    if self.at > other.df:
      'damage is dealt'
      other.sethp(other.hp - (self.at - other.df))
    else:
      'damage is not dealt'
      print(self.name, 'is too weak.')

    print(self.name, " attacked ", other.name, ".", sep = "", end= " ")
    print(self.name, "'s HP is ", self.hp, "/", self.maxhp, ".", sep = "", end= " ")
    print(other.name, "'s HP is ", other.hp, "/", other.maxhp, ".", sep = "", end= "\n")

    if other.gethp() <= 0:
      'other player dies'
      print(self.name, 'defeated', other.name, end ='!\n')

class MajorCharacter(Character):
  '''represents the playable characters in the game'''
  def __init__(self, name, lvl=1, hp=100, at=10, df=1, exp=1):
        Character.__init__(self, name, lvl, hp, at, df, exp)

        self.charged = False        
        self.shields = 0           

  def recover(self, recoverypts):
      ''' recover the current character's HP by recoverypts UP TO the max'''
      self.hp += recoverypts
      if self.hp > self.maxhp:
          'recovered health is above the maximum allowed'
          self.hp = self.maxhp
      print(self.name, "'s HP has been restored to ", self.hp, "/", self.maxhp, ".", sep = "", end= "\n")

  def fullheal(self):
      '''fully restores the player's health'''
      self.hp = self.maxhp
      print(self.name, "'s HP has been fully restored (", self.hp, "/", self.maxhp, ").", sep = "", end= "\n")

  def shield(self):
      '''creates the shield that protects from all attacks for the next 3 turns'''
      print(self.name, "is safe from the next 3 attacks.", sep = " ", end= "\n")
      self.shields = 3       

  def sethp(self, hp):
    ''' sets the character's hp to a new value or 0 (if hp is below 0)'''
    if self.shields > 0:
          'shield is activated and will not deplete health'
          self.hp = self.hp
          self.shields -= 1
    elif hp <= 0:
        'health amount is negative, so 0 will be set'
        self.hp = 0
    else:
        'health amount is positive and will increase the health'
        try:
            self.hp = int(hp)
        except:
            self.hp = hp

  def decr_shield(self):
      '''decreases shield amount'''
      self.shields -= 1

  def charge(self):
      '''increases player damage'''
      self.charged = True
      print(self.getname(), "charged.")

  def attack(self, other):
      '''attack the enemy minions and boss'''
      if self.charged:
        'charge is activated'
        if (2.5 * self.at) > other.df:
          'damage is dealt'
          other.sethp(other.hp - (2.5 * self.at - other.df))
        else:
          'damage is not dealt'
          print(self.name, 'is too weak.')
        self.charged = False
      else:
        'charge is not activated'
        if self.at > other.df:
          'damage is dealt'
          other.sethp(other.hp - (self.at - other.df))
        else:
          'damage is not dealt'
          print(self.name, 'is too weak.')

      print(self.name, " attacked ", other.name, ".", sep = "", end= " ")
      print(self.name, "'s HP is ", self.hp, "/", self.maxhp, ".", sep = "", end= " ")
      print(other.name, "'s HP is ", other.hp, "/", other.maxhp, ".", sep = "", end= "\n")

      if other.gethp() <= 0:
        'other player dies'
        print(self.name, 'defeated', other.name, end ='!\n')

class Minion(Character):
  '''represents Minions in the game'''
  def __init__(self, name, lvl=1, hp=100, at=10, df=1, exp=1):
    Character.__init__(self, name, lvl, hp, at, df, exp)

    self.hp = boss.gethp() // 4
    self.at = boss.getat() // 4
    self.lvl = boss.getlvl()
    self.exp = 0
    self.df = 0
    self.maxhp = self.hp

# this list stores all alive minions
minions_list = []

class Boss(Character):
  '''represents the Boss enemy in the game'''
  def __init__(self, name, lvl=3, hp=100, at=12, df=1, exp=1):
    Character.__init__(self, name, lvl, hp, at, df, exp)

  def spawn(self):
     '''Boss can spawn a Minion'''
     monster = Minion("Minion")
     print("Boss spawned Minion (HP ", monster.gethp(), ", AT ", monster.getat(), ", DF ", monster.getdf(), ")", sep='')
     minions_list.append(monster)  
     return monster

### MAIN GAME START
invalid = True
while invalid:
      'runs this loop until valid entries are provided'
      try:
        players_num = int(input("How many players? "))
        if players_num >= 1 and players_num <= 8:                                            
          'Number is valid and loop ends'                       
          invalid = False
        else:
          'Number is not valid. Loop restarts'
          print("Error. Enter an integer between 1-8.")
      except:
        'Number is not valid. Loop restarts'
        print("Error. Enter an integer between 1-8.")

# the following lists hold all the playes, their healths and the minimums of the healths
players_list = []
players_HP_list = []
players_HP_list_min = []

for i in range(1, players_num+1):
  'put the players into the list'
  print("Player", i, "Name: ", end="")
  players_new = input()
  players_new = MajorCharacter(players_new,1, 100,10,5,0 )
  players_list.append(players_new)

# creates the instance of the boss and sets its health based on number of players
boss = Boss("Boss", lvl = 1, at = 100, df = 0, exp = 0) 
if players_num == 3:
  'There are 3 players'
  boss.sethp(60)
  boss.maxhp = boss.hp
else :
  'There are not 3 players'
  hp = players_num * 20
  boss.sethp(hp)
  boss.maxhp = boss.hp

def Players_Low_HP():
  '''finds the players with lowest health amount'''
  players_HP_list.clear()

  for i in players_list:
    'returns the alive player with the lowest health'
    players_HP_list.append(i.gethp())

  lowestHP = min(players_HP_list)

  if players_HP_list.count(lowestHP) == 1:
    'there is 1 player with lowest health'
    for i in players_list:
      'checks if each health amount is the minimum one'
      if i.gethp() == lowestHP:
        return i
  else:
    'there are more than 1 players with lowest health'
    for i in players_list:
      'if the players health is the minimum, it is returned'
      if i.gethp() == lowestHP:
        players_HP_list_min.append(i)
    return players_HP_list_min[-1]

def Players_Status():
  '''removes dead players from the list '''
  for i in players_list:
    if i.gethp() == 0:
      'player is dead'
      players_list.remove(i)

def Minions_Status():
  'removes dead minions from the list'
  if not minions_list:
    'all minions are dead'
    minions_list.append(boss)
    print("There are no Minions to attack.")
  else:
    'some minions are still alive. The show goes on'
    pass
  for x in minions_list:
    if x.gethp() == 0:
      'minion is dead'
      minions_list.remove(x)

game_loop = True
options = '''1. Attack \n2. Charge \n3. Shield'''
minion = boss.spawn() 
lowest_HP = players_list

### GAME LOOP
while game_loop:
  'run the game loop until the boss is killed or the player dies'
  for i in players_list:
    'ask players about attack, charge, shield options'
    Minions_Status()
    error = True
    while error:
      'runs loop until valid entries are provided'
      try:
       print(options)
       print(i.getname(), ", what would you like to do? ", sep="", end="")
       players_choice = int(input())
       if players_choice >= 1 and players_choice <= 3:
         'Number is valid'
         error = False
       else:
         'Invalid Nmber. Loop restarts'
         print("Invalid input.")
      except:
        'Number is not valid. Loop restarts'
        print("Invalid input.")
        
    if players_choice == 1:
      'Attack'
      for x in minions_list:
        'give a list of enemies to attack'
        for y in minions_list:
          'prints out the name of each minion'
          print(minions_list.index(y)+1,". ", y.getname(), " (HP ", y.gethp(), ")", sep="")
        print(i.getname(), ", who would you like to attack? ", sep="", end="")
        players_choice_at = int(input())
        i.attack(minions_list[players_choice_at-1])
        break
    elif players_choice == 2:
      'Charge'
      i.charge()
      for x in minions_list:
        if Players_Low_HP().gethp() == 0:
          pass
        else:
          x.attack(Players_Low_HP())
      minion = boss.spawn()
    elif players_choice == 3:
      'Shield'
      i.shield()
      for x in minions_list:
        if Players_Low_HP().gethp() == 0:
          pass
        else:
          x.attack(Players_Low_HP()) 
      minion = boss.spawn() 

    Players_Status()
    Minions_Status()

    if not players_list:
      'all players are dead'
      print("You lose.")
      game_loop = False
      break
    elif boss.gethp() == 0:
      'boss is killed'
      print('''Boss has been defeated.\nYou win!''')
      game_loop = False
      break