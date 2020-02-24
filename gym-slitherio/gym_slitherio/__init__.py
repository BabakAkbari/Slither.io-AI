from gym.envs.registration import register

register(
    id='slitherio-v0',
    entry_point='gym_slitherio.envs:SlitherioEnv',
)
'''
register(
    id='slitherio-extrahard-v0',
    entry_point='gym_slitherio.envs:SlitherioExtraHardEnv',
)
'''
