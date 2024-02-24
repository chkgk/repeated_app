from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Bid(ExtraModel):
    player = models.Link(Player)
    bid = models.IntegerField()

# FUNCTIONS
def creating_session(subsession):
    print("creating_session in app1")


# PAGES
class MyPage(Page):
    @staticmethod
    def live_method(player, data):
        print(f"received a bid from {player.id_in_group}: {data}")
        Bid.create(player=player, bid=data)


class Results(Page):
    pass


page_sequence = [MyPage, Results]
