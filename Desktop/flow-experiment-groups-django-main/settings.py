from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='full_sp_mp',
                        num_demo_participants=3,
                        app_sequence=['a_preparation', 'b_alone', 'rest_break', 'c_team', 'd_end']),
                   dict(name='full_mp_sp',
                        num_demo_participants=3,
                        app_sequence=['a_preparation', 'c_team', 'rest_break', 'b_alone', 'd_end']),
                   dict(name='prep_only',
                        num_demo_participants=3,
                        app_sequence=['a_preparation']),
                   dict(name='alone_only',
                        num_demo_participants=3,
                        app_sequence=['b_alone']),
                   dict(name='team_only',
                        num_demo_participants=3,
                        app_sequence=['c_team'])
                   ]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['trans_imgs_solo','trans_imgs_team']
SESSION_FIELDS = []
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


