# Voici tout les modules dont nous avons besoin pour faire fonctionner le jeu. 
# from os import system, name
from colors import Colors as c
import random, json
from os import path, listdir
import time, sys
from clear import clear

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress):
    barLength = 20 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: Le chargement sera fait à la demande.\r\n"
    if progress < 0:
        progress = 0
        status = "Fini...\r\n"
    if progress >= 1:
        progress = 1
        status = "Fini...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "▒"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# update_progress test script
print ("Chargement de la sauvegarde...")
update_progress("hello")
time.sleep(1)

print ("Chargement des couleurs")
update_progress(3)
time.sleep(2)

print("")
print ("Chargment des valeurs")
#update_progress(10)
#time.sleep(2)
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100.0)
  

print ("Chargement de la mine")
#update_progress([23])
#time.sleep(1)
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100.0)
  
print("")
print ("Chargment de la boutique")
#update_progress(10)
#time.sleep(2)
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100.0)

print ("Chargement des prix de la boutique")
update_progress("hello")
time.sleep(1)

print ("")
print ("chagement du café")
update_progress(10)
time.sleep(2)

print ("")
print ("Démarrage du jeu")
for i in range(101):
    time.sleep(0.1)
    update_progress(i/100.0)

print ("")
print ("Jeu chargé avec succès!")
time.sleep(2)
clear()
print("affichage du début...")
time.sleep(2)
clear()

# Si tout les modules ne sont pas installé, Python vous dira que le module est manquant.
# Ces lignes permettent de créer des erreurs personnalisés. 
try:
  import getkey
except ModuleNotFoundError:
  raise Exception("Vous devez installer le module `getkey` !")

# On choisit un mot/phrase au hasard dans le fichier "random.txt" et on le met dans la console. 
with open("random.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split())) 
  
    
    print(random.choice(words)) 
  
x = 0
y = 0
items = 0
depth = 1


#ici, on définit le premier menu du jeu. Sur ce menu, on choisit notre pseudo et on informe l'utilisateur de l'existence du README.md


  #Ici, la partie de code qui fait en sorte d'afficher "Pressez ENTER pour continuer"
def waiting():
  input("Pressez ENTER pour continuer")
  clear()
n = input("█████████████████████████████████\n█▄─▀█▀─▄█▄─▄█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀█\n██─█▄█─███─███─█▄▀─███─▄█▀██─▄─▄█\n▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀\n꒦‧₊˚⊹ Avant de commencer à jouer, merci de lire les informations: show files > README.MD ₊˚੭ \n˃ ᴗ ˂ : Hello. Bienvenue sur MINER! 𓂃 ‹3 \n・ᘏ₊˚⁺ S'il vous plait, tapez votre pseudo ⋆﹆ \n₊˚ꔫ si vous avez sauvegardé votre partie, tapez le même pseudo et d - charger ₊˚  ੭\n ࿔꒰・Version 1.5\n")

#ici, on définit les valeurs par défaut de TOUTES les données que le joueur sera susceptible d'utiliser durant sa partie. 

stamina = 100;
nbresave = 0;
gem = 0;
gold = 0;
iron = 0;
diam = 0;
allIron = 0;
allGold = 0;
allGem = 0;
allDiam = 0;
allPickaxeUsed = 0;
money = 0;
allMoney = 0;
pickaxeLevel = 1;
backpackLevel = 1;
auraLevel = 1;
pickUpCost = 100;
backUpCost = 100;
auraUpCost = 140;
coffeeCost = 10;
pickaxeHealth = pickaxeLevel * 20

#ici, il s'agit de la "mine"

field = [
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "#", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
]
counterX = 0
counterY = 0

#On choisit les chances d'afficher le minerai.
#Pour cela, on choisit pour chaque 0 de la "mine" un nombre entre 1 et 100. si ce nombre est:
  #Est entre 6 et 10, le minerai affiché sera une gem
  #Est entre 11 et 40, le minerai affiché sera un or.
  #Est inférieur à 5, le minerai sera un diamant.
  #Tout les 0 supérieurs à 41 seront des minerais de fer.

for line in field:
  counterY += 1
  counterX = 0
  for item in line:
    counterX += 1
    a = random.randint(1,100)
    color = c.white
    if field[counterY - 1][counterX - 1] == "#":
      color = c.red
    elif a >=6 and a <= 10:
      color = c.magenta
    elif a >= 11 and a <= 40:
      color = c.bright_yellow
    elif a <=5:
      color = c.blue
    field[counterY - 1][counterX - 1] = f"{color}{field[counterY - 1][counterX - 1]}{c.r}"
def newDepth():
  counterX = 0
  counterY = 0
  for line in field:
    counterY += 1
    counterX = 0
    for item in line:
      counterX += 1
      a = random.randint(1,100)
      color = c.white
      if field[counterY - 1][counterX - 1] == "#":
        color = c.red
      elif a >=6 and a <= 10:
        color = c.magenta
      elif a >= 11 and a <= 40:
        color = c.bright_yellow
      elif a <=5:
        color = c.blue
      if field[counterY - 1][counterX - 1] == "#":
        field[counterY - 1][counterX - 1] = f"{color}#{c.r}"
      else:
        field[counterY - 1][counterX - 1] = f"{color}0{c.r}"
def out(f):
      for line in f:
        counter = 0
        for item in line:
          counter += 1
          if (counter != 10):
            print(f"{item} ", end="", flush=True)
          else:
            print(f"{item} ")


#Ce texte s'affiche juste après avoir saisi le pseudo
def start():
  print(f"˃ ᴗ ˂ : Bienvenue dans LA VIE DE {n.upper()}! le but de ce jeu est de réaliser une carrière de mineur. Vous devez miner des minerais, améliorer votre équipement et essayer d'avoir le meilleur score. ₊˚  ੭")
  waiting()

#On reviens dans "la mine"
  #on définit les coordonnées du joueur (le #) dans le terrain.

def findPos():
  global x, y
  for Y in range(len(field)):
    for X in range(len(field[Y])):
      if item == "#":
        x = X
        y = Y
        break

#Ici, on va définir les propriétés des minerais, c'est à dire le nombre de minerai en plus quand on en récupère un, et la durabilité de la pioche.
def atCoordinateMine(xCoord, yCoord):
  global iron, gem, gold, diam, allIron, allGold, allGem, allDiam, pickaxeHealth, allPickaxeUsed, stamina
  it = field[yCoord - 1][xCoord - 1]
  
  #Si le minerai récupéré est du fer:
    #On ajoute 1 de fer
    #On ajoute aussi 1 au compteur total.
    #On enlève 1 à la durabilité de la pioche.
  if it == f"{c.white}0{c.r}":
    iron += 1
    allIron += 1
    allPickaxeUsed += 1
    pickaxeHealth -= 1
    op = 1
      
  #Si le minerai récupéré est de l'or:
    #On ajoute 1 à or
    #On ajoute aussi 1 au compteur total.
    #On enlève 1 à la durabilité de la pioche.  
  elif it == f"{c.bright_yellow}0{c.r}":
    gold += 1
    allGold += 1
    allPickaxeUsed += 1
    pickaxeHealth -= 3
    op = 1

  #Si le minerai récupéré est une gem:
    #On ajoute 1 de gem
    #On ajoute aussi 1 au compteur total.
    #On enlève 5 à la durabilité de la pioche.  
  elif it == f"{c.magenta}0{c.r}":
    gem += 1
    allGem += 1
    stamina -= 2
    allPickaxeUsed += 1
    pickaxeHealth -= 5
    op = 1

  #Si le minerai récupéré est du diamant:
    #On ajoute 0.5 diamant
    #On ajoute aussi 0.5 au compteur total.
    #On enlève 8 à la durabilité de la pioche.  
  elif it == f"{c.blue}0{c.r}":
    diam += 0.5
    allDiam += 0.5
    stamina -= 3
    allPickaxeUsed += 1
    pickaxeHealth -= 8
    op = 1
  else:
    op = 0
  return op

#On va définir le café.

def coffee():
  global money, stamina, coffeeCost, update_progress
  while True:
    print(f"Bienvenue au café! Prenez donc un café et détendez-vous!\n")
    print(f"࿔꒰・Energie: {stamina}    ࿔꒰・Monnaie: {money}\n ")
    while True:
      sel = input(f"₊˚ ੭Choisissez votre action: \n࿔⸝⸝₊╭・A: Prendre un café:\n coût: {coffeeCost}; restaure 10.\n ₊˚ ੭Choisissez votre action: \n࿔⸝⸝₊╰・B: Partir\n")
      sel = sel.lower()
      if sel not in ["a", "b"]:
        clear()
        coffee()
      else: 
        break
    if sel == "a":
      
      clear()
      if money < coffeeCost:
        print(f"꒦‧₊˚⊹ Vous n'avez pas assez d'argent pour acheter un café qui coute {coffeeCost}. Minez encore un peu, vendez vos minerais et revenez plus tard! 𓂃 ‹3")
        waiting()
        clear()
        coffee()

      if stamina >= 90:
        print(f"꒦‧₊˚⊹ Vous êtes bien energique, il n'est pas nécessaire de ce reposer. Allez travailler")
        waiting()
        coffee()
        
      else:
        money -= coffeeCost
        stamina += 10
        coffeeCost += (1 + (pickaxeLevel - 1) * 0.5)
        coffeeCost = round(coffeeCost)
        print ("Voici votre café, Servez-vous!")
#update_progress(10)
#time.sleep(2)
        for i in range(101):
          time.sleep(0.01)
          update_progress(i/100.0)
        print(f"˃ ᴗ ˂ : On dirait que votre énergie est revenu! ₊˚ꔫ")
        waiting()
        clear()
        coffee()

    if sel == "b":
      clear()
      mine()
      
          
      
      
  
#On passe à la définition de l'interface du shop.


def shop():
  global money, pickaxeLevel, pickaxeHealth, backpackLevel, auraLevel, pickUpCost, backUpCost, auraUpCost, iron, gold, gem, diam, allIron, allGold, allGem, allDiam, allMoney
  while True:
    print(f"࿔꒰・niveau de la pioche: {pickaxeLevel}    ࿔꒰・taille du sac: {backpackLevel}      ࿔꒰・multiplieur de bonnes affaires: {auraLevel}      Monnaie: {money}\n ")
    while True:
      sel = input(f"₊˚ ੭Choisissez votre action: \n࿔⸝⸝₊╭・A: vendre tout mes minerais\n࿔⸝⸝₊┇B: améliorer ma pioche: {pickUpCost}\n࿔⸝⸝₊┇C: améliorer la taille du sac: {backUpCost}\n࿔⸝⸝₊┇D: avoir de meilleurs prix sur les minerais: {auraUpCost}\n࿔⸝⸝₊╰・E: quitter la boutique.\n")
      sel = sel.lower()
      if sel not in ["a", "b", "c", "d", "e"]:
        clear()
        shop()
      else:
        break
    if sel == "a":

      clear()
      amountSold = round((iron * 1 + gold * 3 + gem * 9 + diam * 12) * (1 + auraLevel * 0.3)) 
      iron = 0
      gold = 0
      gem = 0
      diam = 0
      money += amountSold
      allMoney += amountSold
      print(f"꒦‧₊˚⊹ Vous vendez tout vos minerais pour {amountSold}. Vous avez désormais {money} d'argent! 𓂃 ‹3")
      waiting()
      clear()
      shop()
    if sel == 'b':
      if money < pickUpCost:
        print(f"꒦‧₊˚⊹ Vous n'avez pas assez d'argent pour améliorer votre pioche qui coûte {pickUpCost}. Minez encore un peu et revenez plus tard ! 𓂃 ‹3")
        waiting()
        clear()
        shop()
      else:
        money -= pickUpCost
        pickaxeLevel += 1
        pickaxeHealth = 20 * pickaxeLevel
        pickUpCost *= (1 + (pickaxeLevel - 1) * 0.5)
        pickUpCost = round(pickUpCost)
        print(f"˃ ᴗ ˂ : Vous avez amélioré votre pioche au niveau {pickaxeLevel} ₊˚ꔫ")
        waiting()
        clear()
        shop()
    if sel == "c":
      if money < backUpCost:
        print(f"꒦‧₊˚⊹ Vous n'avez pas assez d'argent pour améliorer votre sac à dos, ce qui coûte {backUpCost}.  Minez encore un peu et revenez plus tard ")
        waiting()
        clear()
        shop()
      else:
        money -= backUpCost
        backpackLevel += 1
        backUpCost *= (1 + (backpackLevel - 1) * 0.5)
        backUpCost = round(backUpCost)
        print(f"˃ ᴗ ˂ : Vous avez amélioré votre sac au niveau {backpackLevel} ₊˚ꔫ")
        waiting()
        clear()
        shop()
    if sel == "d":
      if money < auraUpCost:
        print(f"꒦‧₊˚⊹ Vous n'avez pas assez d'argent pour mettre à niveau vos skill en négociation, ce qui coûte {auraUpCost}.  Minez encore un peu et revenez plus tard ₊˚੭")
        waiting()
        clear()
        shop()
      else:
        money -= auraUpCost
        auraLevel += 1
        auraUpCost *= (1 + (auraLevel - 1) * 0.5)
        auraUpCost = round(auraUpCost)
        print(f"˃ ᴗ ˂ : Vous avez augmenté vos skill en négociation au niveau {auraLevel}₊˚ꔫ")
        waiting()
        clear()
        shop()
    if sel == "e":
      clear()
      mine()


def mining():
  global x, y, items, depth, pickaxeHealth, pickaxeLevel, stamina

  while True:
    clear()
    print(f"࿔꒰・Gem: {gem}  ࿔꒰・or: {gold}      ࿔꒰・Fer: {iron}      ࿔꒰・diamant: {diam}      ࿔꒰・sac: {items}/{backpackLevel * 10}     ࿔꒰・Durabilité de la pioche: {pickaxeHealth}/{pickaxeLevel * 20}      ࿔꒰・Energie: {stamina}/100")
    out(field)
    current = getkey.getkey()
    current = current.lower()
    if current.lower() in ['w', 'a', 's', 'd']:
      prev_y = y
      prev_x = x
      if current == "w":
        stamina -= 1
        if y != 1:
          put = atCoordinateMine(x, y - 1)
          if put == 1:
            items += 1
          y -= 1
        else:
          clear()
          mining()
      if current == "s":
        stamina -= 1
        if y != 10:
          put = atCoordinateMine(x, y + 1)
          if put == 1:
            items += 1
          y += 1
        else:
          clear()
          mining()
      if current == "a":
        stamina -= 1
        if x != 1:
          put = atCoordinateMine(x - 1, y)
          if put == 1:
            items += 1
          x -= 1
        else:
          clear()
          mining()
      if current == "d":
        stamina -= 1
        if x != 10:
          put = atCoordinateMine(x + 1, y)
          if put == 1:
            items += 1
          x += 1
        else:
          clear()
          mining()
      yy = 0
      xx = 0
      for line in field:
        yy += 1
        xx = 0;
        for item in line:
          xx += 1
          if xx == x and yy == y:
            field[yy - 1][xx - 1] = f"{c.red}#{c.r}"
          elif xx == prev_x and yy == prev_y:
            field[yy - 1][xx - 1] = " "
          else:
            field[yy - 1][xx - 1] = field[yy - 1][xx - 1]
      if items >= backpackLevel * 10:
        clear()
        pickaxeHealth = pickaxeLevel * 20
        newDepth()
        mine()
      if pickaxeHealth <= 0:
        clear()
        pickaxeHealth = pickaxeLevel * 20
        newDepth()
        mine()
      if items < backpackLevel * 10 and items > 99 * depth:
        depth += 1
        newDepth()

      clear()
def mine():
  global x, y, items, n, field, gem, gold, iron, diam, money, pickUpCost, backUpCost, auraUpCost, pickaxeLevel, backpackLevel, auraLevel, pickaxeHealth, nbresave, allIron, allGold, allGem, allDiam, allPickaxeUsed, allMoney, stamina, coffeeCost, update_progress
  while True:
    print(f"˃ ᴗ ˂ : Bienvenue à nouveau sur LA VIE DE {n.upper()}!\n choisissez la lettre pour faire votre action:\n࿔⸝⸝₊╭・A: Miner\n࿔⸝⸝₊┇B: aller à la boutique\n࿔⸝⸝₊┇C: sauvgarder \n࿔⸝⸝₊┇D: charger\n࿔⸝⸝₊┇E: Tableau des leaders\n࿔⸝⸝₊┇F: crédit\n࿔⸝⸝₊┇G: Statistiques\n࿔⸝⸝₊╰・H: Café |NOUVEAU|")
    selection = input()
    selection = selection.lower()
    if selection in ["a", "b", "c", "d", "e", "f", "g", "h"]:
      break
    else:
      clear()
  clear()
  if selection == "a":
    if (stamina <= 15):
      print(f"Vous êtes épuisé. Votre patron vous interdit d'aller à la mine.")
      waiting()
      mine()
    else:
      print ("")
      print ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⠛⠛⠛⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿\n⣿⣿⣀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⡶⢶⣶⣶⣿⣿⣿⣿⣿\n⣿⣿⣿⡿⠉⢹⣿⣿⠋⣠⣿⣿⡿⢃⠸⣿⣿⣿⣿⣿⣷⠀⠸⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⡇⠀⢸⡟⢁⣴⣿⣿⣧⢀⣉⠁⢹⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⡇⠀⣾⣧⣾⣿⣿⣿⣿⣤⣭⣴⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⡟⠀⠀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⡿⠛⠿⢿⣧⡶⠾⠿⠛⣿⣿⣿⣿\n⣿⣿⡇⠀⠀⣿⣿⣿⣿⠁⢠⣬⣭⣽⡿⠿⠿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠾⠿⣿⣿\n⣿⣿⡇⠀⢸⣿⣿⣇⡀⢀⣀⣀⣀⣘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿\n⣿⣿⣶⣦⣼⣿⣏⡉⢀⣈⣉⣉⣉⣉⣹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿\n⣿⣿⣿⣿⣿⠿⠟⠀⠾⠿⠿⠿⠿⠿⠿⢿⣆⣀⣀⡀⠀⠀⠀⢀⣀⣀⢸⣿⣿⣿\n⣿⣿⣿⣿⣿⣟⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⣿⣿⣿⣿⣿⡉⢙⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\nchagement de la mine")
      update_progress(10)
      time.sleep(2)

      field[5][4] = f"{c.red}#{c.r}"
      x = 5
      y = 6
      print("࿔꒰・⛏・──Bienvenue à la mine ₊˚੭")
      items = 0
      mining()
  elif selection == "b":
    print ("")
    print ("^             ^               ^!^\n   ^ ______________________________\n _    [=U=U=U=U=U=U=U=U=U=U=U=U=U=U=U=]\n    |.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.|\n    |        +-+-+-+-+-+-+-+        |\n    |        |Bait & Tackle        |\n    |        +-+-+-+-+-+-+-+        |\n    |.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.|\n   |  _________  __ __  _________  |\n  _ | |___   _  ||[]|[]||  _      | | _\n (!)||OPEN|_(!)_|| ,| ,||_(!)_____| |(!)\n.T~T|:.....:T~T.:|__|__|:.T~T.:....:|T~T. \n||_||||||||||_|||||||||||||_||||||||||_||\n~\=/~~~~~~~~\=/~~~~~~~~~~~\=/~~~~~~~~\=/~\n  | -------- | ----------- | -------- |\n~ |~^ ^~~^ ~~| ~^  ~~ ^~^~ |~ ^~^ ~~^ |^~\nchagement des prix de la boutique")
    update_progress(10)
    time.sleep(1)
    print("꒦‧₊˚⊹ bienvenue dans la boutique ! 𓂃 ‹3")
    shop()
  
  elif selection == "c":
    nbresave += 1
    with open(f"file/{n}.json", "w") as F:
      jsonFile = {"name": n, "field": field, "stamina": stamina, "gem": gem, "gold": gold, "iron": iron, "diam": diam, "money": money, "pickUp": pickUpCost, "backUp": backUpCost, "auraUp": auraUpCost, "coffeeCost": coffeeCost, "pickLevel": pickaxeLevel, "backLevel": backpackLevel, "auraLevel": auraLevel, "pickHealth": pickaxeHealth, "nbresave": nbresave, "allIron": allIron, "allGold": allGold, "allGem": allGem, "allDiam": allDiam, "allPickaxeUsed": allPickaxeUsed, "allMoney": allMoney}
      json.dump(jsonFile, F)
      print ("")
      print ("███████████████████████████████████▀█\n█─▄▄▄▄██▀▄─██▄─█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█\n█▄▄▄▄─██─▀─███▄▀▄███─███─█▄▀─██─██▄─█\n▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀\nSauvegarde en cours...")
      for i in range(101):
        time.sleep(0.1)
      update_progress(i/100.0)
      clear()
    print("・ᘏ₊˚⁺ JEU SAUVÉ ⋆﹆")
    mine()
  elif selection == "d":
    if path.exists(f"file/{n}.json"):
      with open(f"file/{n}.json", "r") as ff:
        data = json.load(ff)
        n = data["name"]
        field = data["field"]
        gem = data["gem"]
        stamina = data["stamina"]
        gold = data["gold"]
        iron = data["iron"]
        diam = data["diam"]
        allGem = data["allGem"]
        allGold = data["allGold"]
        allIron = data["allIron"]
        allDiam = data["allDiam"]
        allPickaxeUsed = data["allPickaxeUsed"]
        money = data['money']
        pickUpCost = data["pickUp"]
        backUpCost = data['backUp']
        auraUpCost = data['auraUp']
        coffeeCost = data["coffeeCost"]
        pickaxeLevel = data['pickLevel']
        backpackLevel = data['backLevel']
        auraLevel = data['auraLevel']
        pickaxeHealth = data['pickHealth']
        nbresave = data['nbresave']
        allMoney = data["allMoney"]
        ff.close()

        print ("")
        print ("█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀\n█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█\nChargement de la sauvegarde..")
        for i in range(101):
          time.sleep(0.01)
      update_progress(i/100.0)
      clear()
      print("JEU CHARGÉ")
      mine()
    else:
      print("࿔꒰✒・LE FICHIER À VOTRE NOM N'EXISTE PAS ⋆﹆")
      mine()

  elif selection == "f":
      clear()
      print("₊˚੭ jeu originalement crée par: aguy11")
      print("˃ ᴗ ˂ : traduction en fr par: valvo_fluttershy et !bêta wolfy")
      print("・─────────────")
      print("₊˚੭ game created by: aguy11")
      print("˃ ᴗ ˂ : tranlated in french by: valvo_fluttershy and !bêta wolfy\n")
      waiting()
      mine()

  elif selection == "h":
    coffee()

  elif selection == "g":
    clear()
    print ("")
    print ("chagement de vos stats")
    update_progress(10)
    time.sleep(2)
    print("Statistiques: ")
    print(f"࿔⸝⸝₊╭・Minerais(en sac):\n ࿔꒰・Gem: {gem} ࿔꒰・or: {gold} ࿔꒰・Fer: {iron} ࿔꒰・diamant: {diam}\n࿔⸝⸝₊┇Minerais(depuis le début):\n ࿔꒰・Gem: {allGem} ࿔꒰・or: {allGold} ࿔꒰・Fer: {allIron} ࿔꒰・diamant: {allDiam} \n ࿔⸝⸝₊┇Mine\n ࿔꒰・sac: {items}/{backpackLevel * 10} ࿔꒰・Durabilité de la pioche: {pickaxeHealth}/{pickaxeLevel * 20} ࿔꒰・Coups de pioche total: {allPickaxeUsed} \n࿔⸝⸝₊┇Boutique\n ࿔꒰・niveau de la pioche: {pickaxeLevel} ࿔꒰・taille du sac: {backpackLevel} ࿔꒰・multiplieur de bonnes affaires: {auraLevel}\n ࿔⸝⸝₊╰・Autres:\n ࿔꒰・Monnaie: {money} ࿔꒰・Monnaie(depuis le début): {allMoney} ࿔꒰・Nombre de sauvegarde: {nbresave}\n")
    waiting()
    mine()

  elif selection == "e":
    users = []
    orderedUsers = []
    high = 0
    for filename in listdir("file"):
      print(filename)
      us = open(f"file/{filename}", 'r')
      d = us.read()
      data = json.loads(d)
      users.append([data["name"], data["money"]])
      us.close()
    for user in users:
      if high <= user[1]:
        orderedUsers.insert(0, user)
        high = user[1]
      else:
        if len(orderedUsers) == 0:
          orderedUsers.insert(0, user)
        else:
          counter = 0
          for use in orderedUsers:
            if user[1] >= use[1]:
              orderedUsers.insert(counter, user)
            else:
              if counter == len(orderedUsers) - 1:
                orderedUsers.append(user)
              else:
                continue
            counter += 1
      clear()
      print("₊˚  ੭ ─ LEADERBOARD")
      counter = 0
      for u in orderedUsers:
        counter += 1
        if counter <= 5:
          # print(f"{counter}) {u[0]}........{u[1]}")
          print("1) Wolfy........1018")
          print(f"{n}........{money}")
          print("\n₊˚ꔫ j'ai pu aprercevoir le problème du leaderboard chez aguy11, le créateur du jeu. La seul solution pour le moment est que vous me dites en commantaire vos stats. je les ajouterai au jeu toutes les semaines. SVP n'utilisez pas le compte des autres!・ᘏ₊˚⁺")
        else:
          break

      waiting()
      clear()
      mine()
    
start()
mine()


# la ligne du diable?