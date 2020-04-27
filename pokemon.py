#Codecademy Pokemon Project
class Pokemon:
  def __init__(self, name, level, type1, max_health, current_health, base_attack,exp, dead=False):
    self.name = name.title()
    self.level = level
    self.type1 = type1
    self.exp = exp
    self.dead = dead
    self.max_health = max_health
    self.current_health = current_health
    self.base_attack = base_attack
    
    return print(" Name: {p1} \n Level: {l1} \n Type: {t1} \n Max Health: {m1} \n Current Health: {h1} \nExprience:  {e3}\n".format(p1=self.name, l1=self.level, t1=self.type1, m1=self.max_health, h1=self.current_health, e3=self.exp))
    
  def lose_health(self,hit):
    dead = None
    self.current_health = self.current_health - hit
    if dead == True:
      print(self.name, " is ko'd")
    if self.current_health < 1:
      print("{p1} has been ko'd".format(p1=self.name))
    else:
      return print("{p1} has {h1} health left\n".format(h1=self.current_health, p1=self.name)), self.current_health, dead
  
  def regain_health(self,revive):
    if self.current_health == 0:
      print("{} has been revived!".format(self.name))
    self.current_health = self.current_health + revive
    return self.current_health, print(self.name + " has regained health to " + str(self.current_health) + " points.")
  
  deadxx = False
  
  def attack(self, rival):
    dead = False
    rival.dead = dead
    if self.current_health < 1:
      return print("{} is ko'd and cannot attack anyone".format(self.name))
    if rival.current_health < 1:
      rival.dead = True
      return print(rival.name, " is ko'd you cannot attack.\n"), rival.dead
    if self.type1 == "fire" or self.type1 == "ice" and rival.type1 == "grass":
      rival.current_health = rival.current_health - self.base_attack * 1.5
    else:# self.type1 == "grass" or self.type1 == "ice" and rival.type1 == "fire":
      rival.current_health = rival.current_health - self.base_attack
    if rival.current_health < 1:
        print("\n" + rival.name + " has benn ko'd after being attacked by {}. Sad!.".format(self.name))
        self.exp = self.exp + 50
        return self.exp
    if self.exp > 100:
      self.exp = self.exp - 100
      self.level = self.level + 1
      self.base_attack = self.base_attack * 2
      self.current_health = self.current_health * 2
      self.max_halth = self.max_health * 2
      print("{} has levelled up! now at level {}!!\n\n".format(self.name, self.level))
      print(" Name: {p1} \n Level: {l1} \n Type: {t1} \n Max Health: {m1} \n Current Health: {h1} \nExprience:  {e3}\n".format(p1=self.name, l1=self.level, t1=self.type1, m1=self.max_health, h1=self.current_health, e3=self.exp))
    else:  
      print("{s2} has been attacked! by {self} with {t1}! {s2} has {h1} health left.".format(s2=rival.name,t1=self.type1, self=self.name, h1=rival.current_health))
      
    
class Trainer:
  def __init__(self,trainer, pokemon,potions, hit_pts, active_pokemon, dead=False):
    self.hit_pts = hit_pts
    self.trainer = trainer.title()
    self.pokemon = pokemon
    self.dead = dead
    #print(type(self.pokemon))
    self.active_pokemon= active_pokemon
    print("{} is now!!!!!!!active".format(self.active_pokemon.name))
    if len(self.pokemon) > 6:
      print("a trainer has a limit of 6 pokemon")
      self.pokemon.pop([6]) 
    self.potions = []
    self.potions = int(potions)
   
  
  def trainerf(self, otherT):
    self.otherT = otherT
    if self.potions < 1:
      print("you have no more potions.")
    if self.otherT.hit_pts < 1:
      print("{so} is ko'd you cannot attack.".format(so=otherT.trainer))
      self.otherT.dead =True
      return otherT.dead
    else:
      self.potions = self.potions - 1
      self.otherT.hit_pts = self.otherT.hit_pts - 10
      print("you attacked {so} with a potion, {so} has {h1} health left".format(so=self.otherT.trainer, h1=self.otherT.hit_pts))
    
    
  def trainerh(self, pokemon1, revive=10):
    self.revive = revive
    if self.potions < 1:
      print("you have no more potions to use")
      return
    if self.pokemon1.dead is True:
      print("{} has been revived!".format(self.name))
    if self.pokemon1.current_health + self.revive > self.pokemon1.max_health:
      self.pokemon1.current_health = self.pokemon1.max_health
      return print(self.pokemon1.name, "has max health")
    self.pokemon1.current_health = self.pokemon1.current_health + self.revive
    return self.pokemon1.current_health, print(self.pokemon1.name, " has regained health to " + str(self.pokemon1.current_health) + " points.")
    self.potions = self.potions - 1
  
  def switch(self, pokemon1):
    self.pokemon1 = pokemon1
    if pokemon1.dead is True:
      return print("cannot switch to dead pokemon")
    for i in self.pokemon:
      if self.pokemon1 == i:
        self.active_pokemon = i
        print("{} is now active pokemon".format(self.active_pokemon.name))
        
pika = Pokemon("pikachu", 4, "ice", 99, 45, 10, 61)
meow = Pokemon("meowf", 4, "grass", 99, 34, 13, 44)
jigg = Pokemon("jigglypuff", 4, "fire", 99, 39, 11, 23)
spiff = Pokemon("spiffamungus", 2, "ice", 99, 69, 12, 9)

pika.lose_health(45)
pika.regain_health(4)
pika.attack(jigg)
jigg.attack(spiff)
meow.attack(jigg)
pika.attack(jigg)
pika.attack(jigg)
pika.attack(jigg)
pika.attack(spiff)
trainer1 = Trainer("brian",[pika, meow, jigg,spiff], 10 ,40, meow)
trainer2 = Trainer("Jen", [spiff, jigg], 4 ,34, jigg)
trainer1.trainerf(trainer2)
trainer1.trainerf(trainer2)
trainer1.trainerf(trainer2)
trainer1.trainerf(trainer2)
trainer1.trainerf(trainer2)
trainer1.trainerf(trainer2)
trainer1.switch(meow)
trainer1.trainerh(pika)
trainer1.trainerh(meow)
trainer1.trainerh(meow)
trainer1.trainerh(pika)
trainer1.trainerh(meow)
trainer1.trainerh(meow)
trainer1.trainerh(pika)
trainer1.trainerh(meow)
trainer1.trainerh(meow)
trainer1.trainerh(meow)
trainer1.trainerh(pika)
trainer1.trainerh(pika)