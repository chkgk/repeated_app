from otree.api import *
from app1 import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app1_copy'
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
    print("creating_session in app1_copy")