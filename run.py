import csv
import random

class GameSetup:
    def __init__(self):
        # Load all necessary CSV data once during initialization
        self.champs = self.load_csv("champs.csv")
        self.spells = self.load_csv("spells.csv")
        self.pets = self.load_csv("junglepets.csv")
        self.starters = self.load_csv("starter.csv")
        self.support_items = self.load_csv("supportitems.csv")
        self.items = self.load_csv("items.csv")
        self.boots = self.load_csv("boots.csv")
        self.bigrunes = self.load_csv("BigRunes.csv")
        self.minirunes = self.load_csv("MiniRunes.csv")
        self.rune_files = {
            "Resolve": self.load_csv("Resolve.csv"),
            "Domination": self.load_csv("Domination.csv"),
            "Inspiration": self.load_csv("Inspiration.csv"),
            "Precision": self.load_csv("Precision.csv"),
            "Sorcery": self.load_csv("Sorcery.csv")
        }

        # Lane order constant
        self.lane_order = ["Top", "Jungle", "Mid", "ADC", "Support"]

    # Helper function to load CSV data
    def load_csv(self, filename):
        with open(filename, 'r') as file:
            return list(csv.reader(file))

    # Helper function to pick random entries
    def pick_random_entries(self, data, num=1):
        if num == 1:
            return random.choice(data)
        return random.sample(data, num)

    # Picking random champion
    def pick_champ(self):
        champ = self.pick_random_entries(self.champs)
        print("**Champion:**", "|".join(champ))

    # Picking spells based on lane
    def pick_spells(self, lanepick):
        if lanepick == "Jungle":
            spellpicks = [self.pick_random_entries(self.spells)[0], "Smite"]
        else:
            spellpicks = [spell[0] for spell in self.pick_random_entries(self.spells, 2)]
        print("**Summoner Spells:**", list(set(spellpicks)))

    # Picking starter items based on lane
    def pick_starter(self, lanepick):
        starterpick = ""
        if lanepick == "Support":
            starterpick = "World Atlas"
        elif lanepick == "Jungle":
            starterpick = self.pick_random_entries(self.pets)[0]
        else:
            starterpick = self.pick_random_entries(self.starters)[0]
        print("**Starter Item:**", starterpick)

    # Picking random boots
    def pick_boots(self):
        bootpick = self.pick_random_entries(self.boots)
        print("**Boots:**", " | ".join(bootpick))

    # Picking random items based on lane
    def pick_items(self, lanepick):
        if lanepick == "Support":
            support_item = self.pick_random_entries(self.support_items)[0]
            itempicks = [item[0] for item in self.pick_random_entries(self.items, 4)]
            itempicks.append(support_item)
        else:
            itempicks = [item[0] for item in self.pick_random_entries(self.items, 5)]
        print("**Item Build:**", " | ".join(itempicks))

    # Simplified rune picking
    def pick_runes(self):
        bigrunepicks = [rune[0] for rune in self.pick_random_entries(self.bigrunes, 2)]
        for rune in bigrunepicks:
            rune_set = self.rune_files.get(rune.strip("'[] "), [])
            if rune_set:
                selected_runes = [self.pick_random_entries(rune_set)[0] for _ in range(min(4, len(rune_set)))]
                print(f"**{rune}:**", " | ".join(selected_runes))

        # Pick Mini Runes
        minirunepicks = [self.pick_random_entries(self.minirunes)[i] for i in range(3)]
        print("**Mini Runes:**", " | ".join(minirunepicks))

    # Main game loop for up to 5 players with randomization, maintaining lane order
    def start_game(self):
        repetitions = int(input("How many players are going to play? (Max 5): "))
        repetitions = min(repetitions, 5)

        selected_lanes = random.sample(self.lane_order, repetitions)
        selected_lanes.sort(key=lambda lane: self.lane_order.index(lane))

        for i in range(repetitions):
            print("\n" * 3, f"Player {i + 1}")

            self.pick_champ()
            lanepick = selected_lanes[i]
            print(f"**Lane:** {lanepick}")
            self.pick_spells(lanepick)
            self.pick_starter(lanepick)
            self.pick_boots()
            self.pick_items(lanepick)
            self.pick_runes()


if __name__ == "__main__":
    game = GameSetup()
    game.start_game()
    input()