
from otree.api import *
c = cu

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'd_end'
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

    # ----- FLOW TRAIT -----
    flow_trait_single = models.IntegerField(
        label='... I experience flow.',
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds1 = models.IntegerField(
        label='... I feel just the right amount of challenge.',
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds2 = models.IntegerField(
        label='... my thoughts / activities run fluidly and smoothly.',
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds3 = models.IntegerField(
        label="... I don’t notice time passing.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds4 = models.IntegerField(
        label="... I have no difficulty concentrating.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds5 = models.IntegerField(
        label="... my mind is completely clear.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds6 = models.IntegerField(
        label="... I am totally absorbed in what I am doing.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds7 = models.IntegerField(
        label="... the right thoughts / movements occur of their own accord.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds8 = models.IntegerField(
        label="... I know what I have to do each step of the way.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds9 = models.IntegerField(
        label="... I feel that I have everything under control.",
        choices=[1, 2, 3, 4, 5, 6, 7],
        widget=widgets.RadioSelectHorizontal
    )

    flow_trait_sfds10 = models.IntegerField(
        label="... I am completely lost in thought.",
        choices=[1, 2, 3, 4, 5, 6, 7],
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

    # ----- End reports ------
    dcs_flow_output = models.IntegerField(
        label='How does the flow experience impact produced output (i.e.the amount of completed work).',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_flow_quality = models.IntegerField(
        label='How does the flow experience impact produced quality (i.e.the quality of completed work).',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_performance_flow = models.IntegerField(
        label='How does feedback on task performance impact flow experience?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_performance_load = models.IntegerField(
        label='How does feedback on task performance impact mental load/demand?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_performance_performance = models.IntegerField(
        label='How does feedback on task performance impact task performance?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_load_flow = models.IntegerField(
        label='How does feedback on mental load/demand impact flow experience?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_load_performance = models.IntegerField(
        label='How does feedback on mental load/demand impact task performance?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_load_load = models.IntegerField(
        label='How does feedback on mental load/demand impact mental load/demand?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_flow_load = models.IntegerField(
        label='How does feedback on flow experience impact mental load/demand?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_flow_performance = models.IntegerField(
        label='How does feedback on flow experience impact task performance?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    dcs_flow_flow = models.IntegerField(
        label='How does feedback on flow experience impact flow experience?',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelectHorizontal
    )

    def make_7p_likert_field(label):
        return models.IntegerField(
            label=label,
            choices=[1, 2, 3, 4, 5, 6, 7],
            widget=widgets.RadioSelectHorizontal
        )

    mathsRating = make_7p_likert_field('I enjoyed the mental arithmetic task.')
    transcriptionRating = make_7p_likert_field('I enjoyed the individual transcription task.')
    transcriptionTeamRating = make_7p_likert_field('I enjoyed the team transcription task.')

    mathSkill = make_7p_likert_field('my mental arithmetic skill level is ...')
    transcriptionSkill = make_7p_likert_field('my transcription skill level is ...')
    transcriptionTeamSkill = make_7p_likert_field('our teams transcription skill level is ...')

    mathDifficulty = make_7p_likert_field('the mental arithmetic task was ...')
    transcriptionDifficulty = make_7p_likert_field('the individual transcription task was ...')
    transcriptionTeamDifficulty = make_7p_likert_field('the transcription task for the team was ...')

    feedback = models.LongStringField(blank=True)

class FlowTrait(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        flow_trait_fields = ['flow_trait_single', 'flow_trait_sfds1', 'flow_trait_sfds2', 'flow_trait_sfds3', 'flow_trait_sfds4', 'flow_trait_sfds5', 'flow_trait_sfds6', 'flow_trait_sfds7', 'flow_trait_sfds8', 'flow_trait_sfds9', 'flow_trait_sfds10']

        form_fields = flow_trait_fields
        return form_fields

class FeedbackPredictions(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random

        dcs_fields = ['dcs_flow_output', 'dcs_flow_quality',
                      'dcs_performance_flow', 'dcs_performance_load', 'dcs_performance_performance',
                      'dcs_load_flow', 'dcs_load_performance', 'dcs_load_load',
                      'dcs_flow_load', 'dcs_flow_performance', 'dcs_flow_flow']
        random.shuffle(dcs_fields)

        form_fields = dcs_fields

        return form_fields

class Debriefing(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random

        deb_fields = ['mathsRating', 'transcriptionRating', 'transcriptionTeamRating']
        skill_fields = ['mathSkill', 'transcriptionSkill', 'transcriptionTeamSkill']
        difficulty_fields = ['mathDifficulty', 'transcriptionDifficulty', 'transcriptionTeamDifficulty']
        random.shuffle(deb_fields)
        random.shuffle(skill_fields)
        random.shuffle(difficulty_fields)
        all_fields = deb_fields + skill_fields + difficulty_fields + ['feedback']

        return all_fields

class B_FeedbackPredictions(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random

        dcs_fields = ['dcs_flow_output', 'dcs_flow_quality',
                      'dcs_performance_flow', 'dcs_performance_load', 'dcs_performance_performance',
                      'dcs_load_flow', 'dcs_load_performance', 'dcs_load_load',
                      'dcs_flow_load', 'dcs_flow_performance', 'dcs_flow_flow']
        random.shuffle(dcs_fields)

        form_fields = dcs_fields

        return form_fields

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

class ThankYou(Page):
    form_model = 'player'

page_sequence = [D_Rest_EC, C_Rest_EO, TLX_Fat_Survey,
                 Debriefing, FlowTrait, FeedbackPredictions, ThankYou]