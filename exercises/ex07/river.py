"""EX07."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

"""EX07."""
__author__ = "730641436"


"""File to define River class."""


class River:
    """Class River."""

    # the class we created

    day: int
    """Variable day."""
    # day variable in the class
    fish: list[Fish]
    """Variable fish."""
    # fish variable in the class
    bears: list[Bear]
    """Variable bears."""
    # bear variable in the class

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # creatting lists to show the number of fish and bears using the age
        # the age will be in the list num_fish or num_bear amount of times
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())  # constructor
            # this will append _fish at age () num_fish times
        for _ in range(0, num_bears):
            self.bears.append(Bear())
            # This is also doing the same but for bears now

    def check_ages(self):
        """This checks ages of the fish and removed them is a certain age or higher."""
        new_blist: list[Bear] = []
        # create new list to litteratr and modify
        # it is a list if Bear becasue it is refering to each induvidual bear
        new_flist: list[Fish] = []
        # new list created to itterate and modify
        # it is a list of Fish becaue it is referifng to each induvidual Fish
        for bear in self.bears:
            # itterating through the self.bears list to see if any bears are less than age 5
            if bear.age < 5:
                # if that bear is less than age 5
                # refer to age by saying bear.age becasue we are refering to the age variable in the induficual bear that is stored in the heap
                new_blist.append(bear)
                # now we append that bear to the enw list
        self.bears = new_blist
        # make self.bears that new list with bears of age less than 5

        for fish in self.fish:
            # itterating through the self.fish list
            # checking for each fish in this list
            if fish.age < 3:
                # checking is the fish and at that certain age is less than 3 to keep
                # need to specify age though so that we can refer to that age in the fish which is stored in the heap
                new_flist.append(fish)
                # If so we append that fish less than 3 years of age to the new list
        self.fish = new_flist
        # make this new list the self.fish list now
        return None

    def bears_eating(self):
        """This calls the eat and remove_fish functions to eat the fish and remove fish for certain amount of bears."""
        # call eat and remove_fish
        for bear in self.bears:
            # for in loop to go through the bears in the lsit
            if len(self.fish) > 5:
                # This makes sure that there are at least 5 fish in the river for teh bear to eat 3
                self.remove_fish(3)
                # calls remove_fish to get rid of three fish
                bear.eat(num_fish=3)
                # This allows the bear to eat 3 fish
        # this will continually loop through the bear list to get rid of the bears that are too hungry

        return None

    def check_hunger(self):
        """This checks hunger of bears by removing bear is starving."""
        copy_bear_l: list[Bear] = []
        # making a copy of the lsit of Bears
        for bear in self.bears:
            # alluding to the lsit of self.bears
            if bear.hunger_score >= 0:
                # we just want to append the bears that have hunger score that is greater than 0
                # referring to the hunger_score for that specific copy/ bear in the lsit which will referto the hunger score for that particular bear in the lsit
                copy_bear_l.append(bear)
                # appending the bear that is not starving
        self.bears = copy_bear_l
        # now having the self.bears as the new list
        return None

    def repopulate_fish(self):
        """This adds more fish to the pool - reproduction of fish."""
        new_fish: int = (len(self.fish) // 2) * 4
        # creating new variable to see how many fish we need to add
        for _ in range(0, new_fish):
            self.fish.append(Fish())
            # we want to add a new fish itself, so we are calling the class to create new Fish om the heap
        return None

    def repopulate_bears(self):
        """This adds more bears to the ppol - reproduction of bears."""
        new_bears: int = len(self.bears) // 2
        # creating new variable to see how mnay bears to add to the Bear popualtion
        for _ in range(0, new_bears):
            self.bears.append(Bear())
            # adding a whole new bear;
            # capital bear w/o parentases is refering to the class (Bear), but with parentaases calling innit --> the constructor
            # parenthases is calling a method!!
        return None

    # Check this one!
    def view_river(self):
        """This gives a rundown of popuation and day."""
        # using f striongs for string concatination
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        # this fucntion basically gives a run down of the popualtions of fish and bears present in the river ecosystem
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """This gives us a seven week outlook of population progression."""
        # calling one_river_day 7 times
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            # saying that while the idx is less that 7 will call that fucntion 7 times
        return None

    def remove_fish(self, amount: int):
        """This removes fish for a function used above."""
        for num in range(0, amount):
            # syaing for the num in the range of 0 to the amount will take out that many fish
            self.fish.pop(num)
            # used in anotehr function above.
        return None
