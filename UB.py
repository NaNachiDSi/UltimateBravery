import csv
import random

def pick_champ():
    with open("champs.csv", 'r') as champs:
        champreader = list(csv.reader(champs))
        champpick = random.choice(champreader)
        print("**Champion:**", "|".join(champpick))

def pick_lane():
    with open("lanes.csv",'r') as lanes:
        lanereader = list(csv.reader(lanes))
        lanepick = random.choice(lanereader)
        print("**Lane:**", "|".join(lanepick))
        return lanepick[0]

def pick_spells(lanepick):
    with open("spells.csv", mode='r') as spells:
        spellreader = list(csv.reader(spells))

        # Ensure "Smite" is included for Jungle lane
        if lanepick == "Jungle":
            random_spell = random.choice(spellreader)[0]
            spellpicks = [random_spell, "Smite"]
        else:
            spellpicks = random.sample(spellreader, 2)  # Pick 2 spells
            spellpicks = [spell[0] for spell in spellpicks]  # Extract names

        # Remove duplicates, if any
        spellpicks = list(set(spellpicks))
        print("**Summoner Spells:**", spellpicks)

def pick_starter(lanepick):
    with open("starter.csv", 'r') as starter:
        starterreader = list(csv.reader(starter))
        if lanepick == "Support":
            starterpick = "World Atlas"
        elif lanepick == "Jungle":
            with open("junglepets.csv", 'r') as pets:
                petreader = list(csv.reader(pets))
            starterpick = random.choice(petreader)[0]
        else:
            starterpick = random.choice(starterreader)[0]
        print("**Starter Item:**", starterpick)

def pick_boots():
    with open("boots.csv",'r') as boots:
        bootreader = list(csv.reader(boots))
        bootpick = random.choice(bootreader)
        print("**Boots:**", " | ".join(bootpick))

def pick_items(lanepick):
    with open("items.csv",'r') as items:
        itemreader = list(csv.reader(items))

        if lanepick == "Support":  # Compare with a string, not a list
            # Pick one item from supportitems.csv
            with open("supportitems.csv", mode='r') as support_items:
                supportreader = list(csv.reader(support_items))
                support_item = random.choice(supportreader)[0]  # Extract the first element (item name)
            itempicks = random.sample(itemreader, 5)  # Pick 4 items from regular items
            itempicks = [item[0] for item in itempicks]  # Extract item names
            itempicks.append(support_item)  # Add the support item
        else:
            itempicks = random.sample(itemreader, 6)  # Pick 5 items from regular items
            itempicks = [item[0] for item in itempicks]
        print("**Item Build:**", " | ".join(itempicks))

def pick_runes():
    with open("BigRunes.csv", "r") as bigrunes:
        bigrunereader = list(csv.reader(bigrunes))
        bigrunepick = random.sample(bigrunereader, 2)
        bigruneone, bigrunetwo = str(bigrunepick).split(",")
        match bigruneone:
            case "[['Resolve']":
                with open("Resolve.csv", 'r') as resolve:
                    Resolvereader = list(csv.reader(resolve))
                    Resolvepick = []
                    Resolvepick.append(random.choice(Resolvereader)[0])
                    Resolvepick.append(random.choice(Resolvereader)[1])
                    Resolvepick.append(random.choice(Resolvereader)[2])
                    Resolvepick.append(random.choice(Resolvereader)[3])
                    print("**Resolve:**", " | ".join(Resolvepick))
            case "[['Domination']":
                with open("Domination.csv", 'r') as Domination:
                    Dominationreader = list(csv.reader(Domination))
                    Dominationpick = []
                    Dominationpick.append(random.choice(Dominationreader)[0])
                    Dominationpick.append(random.choice(Dominationreader)[1])
                    Dominationpick.append(random.choice(Dominationreader)[2])
                    Dominationpick.append(random.choice(Dominationreader)[3])
                    print("**Domination:**", " | ".join(Dominationpick))
            case "[['Inspiration']":
                with open("Inspiration.csv", 'r') as Inspiration:
                    Inspirationreader = list(csv.reader(Inspiration))
                    Inspirationpick = []
                    Inspirationpick.append(random.choice(Inspirationreader)[0])
                    Inspirationpick.append(random.choice(Inspirationreader)[1])
                    Inspirationpick.append(random.choice(Inspirationreader)[2])
                    Inspirationpick.append(random.choice(Inspirationreader)[3])
                    print("**Inspiration:**", " | ".join(Inspirationpick))
            case "[['Precision']":
                with open("Precision.csv", 'r') as Precision:
                    Precisionreader = list(csv.reader(Precision))
                    Precisionpick = []
                    Precisionpick.append(random.choice(Precisionreader)[0])
                    Precisionpick.append(random.choice(Precisionreader)[1])
                    Precisionpick.append(random.choice(Precisionreader)[2])
                    Precisionpick.append(random.choice(Precisionreader)[3])
                    print("**Precision:**", " | ".join(Precisionpick))
            case "[['Sorcery']":
                with open("Sorcery.csv", 'r') as Sorcery:
                    Sorceryreader = list(csv.reader(Sorcery))
                    Sorcerypick = []
                    Sorcerypick.append(random.choice(Sorceryreader)[0])
                    Sorcerypick.append(random.choice(Sorceryreader)[1])
                    Sorcerypick.append(random.choice(Sorceryreader)[2])
                    Sorcerypick.append(random.choice(Sorceryreader)[3])
                    print("**Sorcery:**", " | ".join(Sorcerypick))

        match bigrunetwo:
            case " ['Resolve']]":
                with open("Resolve.csv", 'r') as offResolve:
                    offResolvereader = list(csv.reader(offResolve))
                    runelaneone, runelanetwo = random.sample([1, 2, 3], 2)
                    offResolvepick = []
                    offResolvepick.append(random.choice(offResolvereader)[runelaneone])
                    offResolvepick.append(random.choice(offResolvereader)[runelanetwo])
                    print("**Resolve:**", " | ".join(offResolvepick))
            case " ['Domination']]":
                with open("Domination.csv", 'r') as offDomination:
                    offDominationreader = list(csv.reader(offDomination))
                    runelaneone, runelanetwo = random.sample([1, 2, 3], 2)
                    offDominationpick = []
                    offDominationpick.append(random.choice(offDominationreader)[runelaneone])
                    offDominationpick.append(random.choice(offDominationreader)[runelanetwo])
                    print("**Domination:**", " | ".join(offDominationpick))
            case " ['Inspiration']]":
                with open("Inspiration.csv", 'r') as offInspiration:
                    offInspirationreader = list(csv.reader(offInspiration))
                    runelaneone, runelanetwo = random.sample([1, 2, 3], 2)
                    offInspirationpick = []
                    offInspirationpick.append(random.choice(offInspirationreader)[runelaneone])
                    offInspirationpick.append(random.choice(offInspirationreader)[runelanetwo])
                    print("**Inspiration:**", " | ".join(offInspirationpick))
            case " ['Precision']]":
                with open("Precision.csv", 'r') as offPrecision:
                    offPrecisionreader = list(csv.reader(offPrecision))
                    runelaneone, runelanetwo = random.sample([1, 2, 3], 2)
                    offPrecisionpick = []
                    offPrecisionpick.append(random.choice(offPrecisionreader)[runelaneone])
                    offPrecisionpick.append(random.choice(offPrecisionreader)[runelanetwo])
                    print("**Precision:**", " | ".join(offPrecisionpick))
            case " ['Sorcery']]":
                with open("Sorcery.csv", 'r') as offSorcery:
                    offSorceryreader = list(csv.reader(offSorcery))
                    runelaneone, runelanetwo = random.sample([1, 2, 3], 2)
                    offSorcerypick = []
                    offSorcerypick.append(random.choice(offSorceryreader)[runelaneone])
                    offSorcerypick.append(random.choice(offSorceryreader)[runelanetwo])
                    print("**Sorcery:**", " | ".join(offSorcerypick))

        with open("MiniRunes.csv", 'r') as MiniRunes:
            minirunereader = list(csv.reader(MiniRunes))
            minirunepicks = []
            minirunepicks.append(random.choice(minirunereader)[0])
            minirunepicks.append(random.choice(minirunereader)[1])
            minirunepicks.append(random.choice(minirunereader)[2])
            print("**Mini Runes:**", " | ".join(minirunepicks))

def main():
    repetitions = int(input("How many Players are going to play ? "))
    for i in range(repetitions):
        print("\n"*3,"Player", i+1, )
        pick_champ()
        lanepick = pick_lane()
        pick_spells(lanepick)
        pick_starter(lanepick)
        pick_boots()
        pick_items(lanepick)
        pick_runes()

if __name__ == "__main__":
    main()
    input()