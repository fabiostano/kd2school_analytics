
from otree.api import *
c = cu

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'rest_break'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # ----- REST ACTIONS ----- #
    rest_actions_eo = models.StringField(label="")
    rest_actions_ec = models.StringField(label="")

    # ----- FATIGUE ----- #
    fatigue_state = models.StringField(
        label='How tired/awake are you right now?',
        choices=['Fully alert, wide awake ',
                 'Very lively, responsive, but not at peak',
                 'Okay, somewhat fresh',
                 'A little tired, less than fresh',
                 'Moderately tired, let down',
                 'Extremely tired, very difficult to concentrate',
                 'Completely exhausted, unable to function effectively']
    )

    # ----- TLX ------
    # "Please indicate on each scale at the point that best indicates your experience of the last few minutes."
    tlx_mental = models.IntegerField(min=0, max=21)
    tlx_temporal = models.IntegerField(min=0, max=21)
    tlx_performance = models.IntegerField(min=0, max=21)
    tlx_effort = models.IntegerField(min=0, max=21)
    tlx_frustration = models.IntegerField(min=0, max=21)
    tlx_physical = models.IntegerField(min=0, max=21)

class C_Rest_EO(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']

class D_Rest_EC(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec']

class TLX_Fat_Survey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['tlx_mental', 'tlx_temporal', 'tlx_performance', 'tlx_effort', 'tlx_frustration',
                       'tlx_physical',
                       'fatigue_state']
        return form_fields

page_sequence = [D_Rest_EC, C_Rest_EO, TLX_Fat_Survey]