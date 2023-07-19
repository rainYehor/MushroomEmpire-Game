SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

BLOCK_WIDTH = SCREEN_WIDTH // 20
BLOCK_HEIGHT = SCREEN_HEIGHT // 20

under_level_1_1 = [
    ['3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 'o', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd5_1', '0', 's'],
    ['3', '3', '3', '3', '3', 'd6', '0', '0', 'e1', '0', '0', '0', '0', '0', '0', '0', '0', 'c_r', '0', 's'],
    ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', 'e', '0', '0', '0', 'e', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
    ['3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '3', '3', '3', '3', '3'],
    ['0', 's', '0', '0', '0', '0', '0', 'e1', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', '0', '0', 'd5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]

under_level_1_2 = [
    ['3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 'o', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd5_1', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 'd6', '0', '0', 'e1', '0', '0', '0', '0', '0', '0', '0', 'c_r', '0', '0', 's'],
    ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', 'e', '0', '0', '0', 'e', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
    ['3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '3', '3', '3', '3', '3'],
    ['0', 's', '0', '0', '0', '0', '0', 'e1', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', '0', '0', 'd5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]

under_level_1_3 = [
    ['3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 'o', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd5_1', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 'd6', '0', '0', 'e1', '0', '0', '0', '0', '0', '0', '0', 'c_r', '0', '0', 's'],
    ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '0', '0', '0', '0', 'e', '0', '0', '0', 'e', '0', '0', '0', '0', 's'],
    ['0', '0', '0', '0', '0', 's', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
    ['3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', 's', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', 's', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '3', '3', '3', '3', '3'],
    ['0', 's', '0', '0', '0', '0', '0', 'e1', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', 's', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['0', '0', '0', 'd5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
]

under_level_2_1 = [
    ['5', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', 'o_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd7_1', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'c_r', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', 'e', '0', '0', '0', 'e', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
    ['5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '5', '5', '5', '5', '5'],
    ['0', 's_c', '0', 'e2', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd7', 's_c', '0', '0', '0', '0', '0'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']
]

under_level_2_2 = [
    ['5', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', 'o_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd7_1', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'c_r', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', 'e', '0', '0', '0', 'e', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
    ['5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '5', '5', '5', '5', '5'],
    ['0', 's_c', '0', 'e2', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd7', 's_c', '0', '0', '0', '0', '0'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']
]

under_level_2_3 = [
    ['5', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', 'o_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd7_1', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'c_r', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', 'e', '0', '0', '0', 'e', '0', '0', '0', '0', 's_c'],
    ['0', '0', '0', '0', '0', 's_c', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
    ['5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', 's_c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '5', '5', '5', '5', '5'],
    ['0', 's_c', '0', 'e2', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd7', 's_c', '0', '0', '0', '0', '0'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 's_c', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 's_c', '0', '0', '0', '0', '0'],
    ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5']
]

under_levels = {"under1" : under_level_1_1,
                "under2" : under_level_1_2,
                "under3" : under_level_1_3,
                "under4" : under_level_2_1,
                "under5" : under_level_2_2,
                "under6" : under_level_2_3}