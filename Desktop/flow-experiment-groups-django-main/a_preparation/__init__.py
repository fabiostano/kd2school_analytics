
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'a_preparation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # ----- SETUP ----- #
    booth = models.StringField(
        label='Which KD2Lab booth is used?',
        choices=["B01", "B02", "B06"]
    )

    # ----- DEMOGRAPHICS ----- #
    handedness = models.StringField(
        label='Which one is your dominant hand?',
        choices=["Left", "Right", "Both (Ambidextrous)"]
    )

    english = models.StringField(
        label='Please indicate the level of your English language proficiency.',
        choices=["A1 Beginner – I can understand and use familiar everyday expressions and very basic phrases.",
                 "A2 Elementary English – I can understand sentences and frequently used expressions related to areas of most immediate relevance.",
                 "B1 Intermediate English – I understand the main points of clear input on familiar matters regularly encountered in work, school, etc.",
                 "B2 Upper-Intermediate English – I understand the main ideas of complex text on concrete and abstract topics, incl. technical discussions, etc.",
                 "C1 Advanced English – I can understand a wide range of demanding, longer texts, and recognise implicit meaning.",
                 "C2 Proficiency English – I can understand with ease virtually everything I hear or read."]
    )

    age = models.IntegerField(
        label='What is your age?'
    )

    gender = models.StringField(
        label='What is your gender?',
        choices=["Male", "Female", "Diverse"]
    )

    glasses = models.StringField(
        label='Are you wearing glasses right now?',
        choices=["Yes", "No"]
    )

    occupation = models.StringField(
        label='What is your current occupation?',
        choices=["Apprentice", "Student", "Employee", "Entrepreneur", "Other"]
    )

    familiarity_1 = models.StringField(
        label='How well do you know the first other participant?',
        choices=['Not at all', 'A little', 'Well', 'Very well']
    )

    familiarity_2 = models.StringField(
        label='How well do you know the second other participant?',
        choices=['Not at all', 'A little', 'Well', 'Very well']
    )

    # ----- REST ACTIONS ----- #
    rest_actions_eo = models.StringField(label = "")
    rest_actions_ec = models.StringField(label = "")

    # ----- TASK ACTIONS ----- #
    math_actions = models.StringField(label = "")

    def make_7p_likert_field(label):
        return models.IntegerField(
            label=label,
            choices=[1, 2, 3, 4, 5, 6, 7],
            widget=widgets.RadioSelectHorizontal
        )

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

class Setup(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        setup_fields = ['booth']
        return setup_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Demographics(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        dem_fields = ['gender', 'age', 'handedness', 'glasses', 'english', 'fatigue_state',
                      'occupation', "familiarity_1", "familiarity_2"]

        form_fields = dem_fields
        return form_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class A_Welcome(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class B_Rest_EO(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class C_Rest_EC(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class MathInstructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 or player.round_number == 2

class D_MentalArithmetic_Moderate(Page):
    form_model = 'player'
    form_fields = ['math_actions']

    def vars_for_template(player: Player):
        return {"round_duration_ms": 120 * 1000,
                "trial_duration_ms": 20 * 1000,
                "difficulty_level": 2}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class E_MentalArithmetic_Hard(Page):
    form_model = 'player'
    form_fields = ['math_actions']

    def vars_for_template(player: Player):
        return {"round_duration_ms": 120 * 1000,
                "trial_duration_ms": 20 * 1000,
                "difficulty_level": 3}

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2

class F_Task_Questionnaire(Page):
    form_model = 'player'
    all_fields = []

    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = ['fss01', 'fss02', 'fss03', 'fss04', 'fss05', 'fss06', 'fss07', 'fss08', 'fss09', 'fss10']
        random.shuffle(flow_fields)
        flow_fields += ['flow_single']
        all_fields = flow_fields

        tlx_fields = ['tlx_mental', 'tlx_temporal', 'tlx_performance', 'tlx_effort', 'tlx_frustration', 'tlx_physical']
        all_fields += tlx_fields

        return all_fields

class TLX_Fat_Survey(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        form_fields = ['tlx_mental', 'tlx_temporal', 'tlx_performance', 'tlx_effort', 'tlx_frustration', 'tlx_physical',
                       'fatigue_state']
        return form_fields

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

page_sequence = [Setup, A_Welcome, Demographics,
                 C_Rest_EC, B_Rest_EO, TLX_Fat_Survey,
                 MathInstructions, E_MentalArithmetic_Hard, D_MentalArithmetic_Moderate,
                 F_Task_Questionnaire]