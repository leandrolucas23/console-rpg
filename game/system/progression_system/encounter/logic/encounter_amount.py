import random

class EncounterAmount:

    @classmethod
    def roll_encounter_amount(cls):
        count = 1
        chance = 50

        while count < 5:

            if random.randint(1, 100) <= chance:
                count += 1
                chance /= 1.
            else:
                break

        return count