from otree.api import *
import random
from os import walk
from os.path import join

c = cu

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'c_team'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 4

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    # Get all the snippets
    root = '_static/snippets/'
    trans_imgs = [join(path, name) for path, subdirs, files in walk(root) for name in files]
    # Remove the '_static/' part again
    trans_imgs = [s.replace('_static/', '') for s in trans_imgs]
    # Remove other files
    trans_imgs = [f for f in trans_imgs if f.endswith('.jpg')]

    # Shuffle the snippets
    random.shuffle(trans_imgs)

    for p in subsession.get_players():
        p.participant.trans_imgs_team = trans_imgs

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    def make_7p_likert_field(label):
        return models.IntegerField(
            label=label,
            choices=[1, 2, 3, 4, 5, 6, 7],
            widget=widgets.RadioSelectHorizontal
        )

    # ---- Task Actions ---- #
    trans_actions = models.LongStringField(blank=True)

    # ----- FLOW ----- #
    fss01 = make_7p_likert_field('I felt just the right amount of challenge.')
    fss02 = make_7p_likert_field('My thoughts/activities ran fluidly and smoothly.')
    fss03 = make_7p_likert_field('I didn’t notice time passing.')
    fss04 = make_7p_likert_field('I had no difficulty concentrating.')
    fss05 = make_7p_likert_field('My mind was completely clear.')
    fss06 = make_7p_likert_field('I was totally absorbed in what I was doing.')
    fss07 = make_7p_likert_field('The right thoughts/movements occurred of their own accord.')
    fss08 = make_7p_likert_field('I knew what I had to do each step of the way.')
    fss09 = make_7p_likert_field('I felt that I had everything under control.')
    fss10 = make_7p_likert_field('I was completely involved in the task.')
    flow_single = models.IntegerField(
        label='How intense was your flow?',
        choices=[0, 1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

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

    # ----- Team Variables ------
    # Team Performance(TLX Item)
    # Team Effort(TLX Item)
    # Team Satisfaction(TLX Item)
    # Synchronisation
    tlx_teamperformance = models.IntegerField(min=0, max=21)
    tlx_teameffort = models.IntegerField(min=0, max=21)
    tlx_teamsatisfaction = models.IntegerField(min=0, max=21)
    team_synchronisation = make_7p_likert_field("How much were you on the same wavelength with your team?")


class X_WaitPage(WaitPage):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class A_Task_Explanation(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class B_Practice(Page):
    form_model = 'player'
    form_fields = ['trans_actions']

    @staticmethod
    def live_method(player: Player, data):
        if data["information_type"] == "started":
            if player.id_in_group == 1:
                return {2: {"information_type": "started1", "started": data["started"]},
                        3: {"information_type": "started1", "started": data["started"]}}
            elif player.id_in_group == 2:
                return {1: {"information_type": "started2", "started": data["started"]},
                        3: {"information_type": "started2", "started": data["started"]}}
            else:
                return {1: {"information_type": "started3", "started": data["started"]},
                        2: {"information_type": "started3", "started": data["started"]}}
        elif data["information_type"] == "solved":
            if player.id_in_group == 1:
                return {2: {"information_type": "solved1", "solved": data["solved"]},
                        3: {"information_type": "solved1", "solved": data["solved"]}}
            elif player.id_in_group == 2:
                return {1: {"information_type": "solved2", "solved": data["solved"]},
                        3: {"information_type": "solved2", "solved": data["solved"]}}
            else:
                return {1: {"information_type": "solved3", "solved": data["solved"]},
                        2: {"information_type": "solved3", "solved": data["solved"]}}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "imageList": player.participant.trans_imgs_team,
            "groupID": player.id_in_group,
            "round": player.round_number,
            "trialTime": 2*60
        }

class C_Coordination(Page):
    form_model = 'player'

class D_Task(Page):
    form_model = 'player'
    form_fields = ['trans_actions']

    @staticmethod
    def live_method(player: Player, data):
        if data["information_type"] == "started":
            if player.id_in_group == 1:
                return {2: {"information_type": "started1", "started": data["started"]},
                        3: {"information_type": "started1", "started": data["started"]}}
            elif player.id_in_group == 2:
                return {1: {"information_type": "started2", "started": data["started"]},
                        3: {"information_type": "started2", "started": data["started"]}}
            else:
                return {1: {"information_type": "started3", "started": data["started"]},
                        2: {"information_type": "started3", "started": data["started"]}}
        elif data["information_type"] == "solved":
            if player.id_in_group == 1:
                return {2: {"information_type": "solved1", "solved": data["solved"]},
                        3: {"information_type": "solved1", "solved": data["solved"]}}
            elif player.id_in_group == 2:
                return {1: {"information_type": "solved2", "solved": data["solved"]},
                        3: {"information_type": "solved2", "solved": data["solved"]}}
            else:
                return {1: {"information_type": "solved3", "solved": data["solved"]},
                        2: {"information_type": "solved3", "solved": data["solved"]}}

    @staticmethod
    def vars_for_template(player: Player):
        n = (player.round_number - 1) * 30
        transimgs = player.participant.trans_imgs_team
        imageList = transimgs[n:]

        return {
            "imageList": imageList,
            "groupID": player.id_in_group,
            "round": player.round_number,
            "trialTime": 4*60
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 1

class E_Task_Questionnaire(Page):
    form_model = 'player'
    all_fields = []

    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = ['fss01', 'fss02', 'fss03', 'fss04', 'fss05',
                       'fss06', 'fss07', 'fss08', 'fss09', 'fss10']
        random.shuffle(flow_fields)
        flow_fields += ['flow_single']
        all_fields = flow_fields

        tlx_fields = ['tlx_mental', 'tlx_temporal', 'tlx_performance',
                      'tlx_effort', 'tlx_frustration', 'tlx_physical']
        all_fields += tlx_fields

        team_fields = ['tlx_teamperformance', 'tlx_teameffort',
                       'tlx_teamsatisfaction', 'team_synchronisation']
        all_fields += team_fields

        return all_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 1


class F_TLX_Survey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['tlx_mental', 'tlx_temporal', 'tlx_performance', 'tlx_effort', 'tlx_frustration', 'tlx_physical',
                       'fatigue_state', 'headset_comfort']
        return form_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number > 1


class G_Break(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        taskType = "Transcription Task"

        return {
            "breakTime": 15,
            "taskType": taskType,
            "currTask": player.round_number,
            "maxTask": 3
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number < 4

class Wait_Page_1(WaitPage):
    form_model = 'player'

    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Wait_Page_2(WaitPage):
    form_model = 'player'

    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number < 4


page_sequence = [A_Task_Explanation, Wait_Page_1, B_Practice, D_Task, E_Task_Questionnaire, Wait_Page_2, G_Break]