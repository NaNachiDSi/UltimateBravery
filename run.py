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
            "Resolve": "Resolve.csv",
            "Domination": "Domination.csv",
            "Inspiration": "Inspiration.csv",
            "Precision": "Precision.csv",
            "Sorcery": "Sorcery.csv"
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
            itempicks = [item[0] for item in self.pick_random_entries(self.items, 5)]
            itempicks.append(support_item)
        else:
            itempicks = [item[0] for item in self.pick_random_entries(self.items, 6)]
        print("**Item Build:**", " | ".join(itempicks))

    # Adjusted rune picking logic
    def pick_runes(self):
        # First Pick
        big_rune_1 = self.pick_random_entries(self.bigrunes)[0]  # Pick a big rune
        print(f"**First Big Rune:** {big_rune_1}")

        # Check if the key exists
        if big_rune_1 in self.rune_files:
            rune_set_1 = self.load_csv(self.rune_files[big_rune_1])
            # Pick one element from each of the available columns
            column_picks_1 = [random.choice(column) for column in zip(*rune_set_1)]  # Transpose and pick one from each
            print(f"**First Rune Picks:** {' | '.join(column_picks_1)}")
        else:
            print(f"Error: {big_rune_1} is not a valid key in the rune files.")

        # Second Pick
        big_rune_2 = self.pick_random_entries(self.bigrunes)[0]  # Pick another big rune
        print(f"**Second Big Rune:** {big_rune_2}")

        # Check if the key exists
        if big_rune_2 in self.rune_files:
            rune_set_2 = self.load_csv(self.rune_files[big_rune_2])

            # Ignore the first column and get the remaining columns
            remaining_columns = list(zip(*rune_set_2))[1:]  # Skip the first column

            # Filter out any empty columns
            remaining_columns = [col for col in remaining_columns if any(col)]

            # Check the number of available remaining columns
            if len(remaining_columns) < 2:
                print("Not enough remaining columns to sample from. Picking all available columns.")
                selected_columns = remaining_columns  # Use all available columns
            else:
                selected_columns = random.sample(remaining_columns, 2)  # Pick two random columns

            # Pick one element from each of the selected columns
            column_picks_2 = [random.choice(column) for column in selected_columns]
            print(f"**Second Rune Picks:** {' | '.join(column_picks_2)}")
        else:
            print(f"Error: {big_rune_2} is not a valid key in the rune files.")

        # Third Pick
        minirunepicks = [random.choice(column) for column in zip(*self.minirunes)]  # Pick one from each column
        print(f"**Mini Runes Picks:** {' | '.join(minirunepicks)}")

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