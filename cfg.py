'''配置文件'''
import os


'''屏幕大小'''
SCREENSIZE = (1200, 600)
'''FPS'''
FPS = 55
'''音频素材路径'''
AUDIO_PATHS = {
    'die': os.path.join(os.getcwd(), 'resources/audios/die.wav'),
    'jump': os.path.join(os.getcwd(), 'resources/audios/jump.wav'),
    'point': os.path.join(os.getcwd(), 'resources/audios/point.wav')
}
'''图片素材路径'''
IMAGE_PATHS = {
    'droid': [
        os.path.join(os.getcwd(), 'resources/images/droid_big.png'),
        os.path.join(os.getcwd(), 'resources/images/droid_big_blast.png'),
        os.path.join(os.getcwd(), 'resources/images/droid_small.png'),
        os.path.join(os.getcwd(), 'resources/images/droid_small_blast.png'),
        os.path.join(os.getcwd(), 'resources/images/droid_explode.png')
    ],
    'cloud': os.path.join(os.getcwd(), 'resources/images/cloud.png'),
    'blast': [
        os.path.join(os.getcwd(), 'resources/images/blast_red.png'),
        os.path.join(os.getcwd(), 'resources/images/blast_blue.png')
    ],
    'player': [
        os.path.join(os.getcwd(), 'resources/images/ank1.png'),
        os.path.join(os.getcwd(), 'resources/images/ank2.png'),
        os.path.join(os.getcwd(), 'resources/images/ank3.png'),
        os.path.join(os.getcwd(), 'resources/images/ank4.png'),
        os.path.join(os.getcwd(), 'resources/images/ank5.png'),
        os.path.join(os.getcwd(), 'resources/images/ank_strike1.png'),
        os.path.join(os.getcwd(), 'resources/images/ank_strike2.png'),
        os.path.join(os.getcwd(), 'resources/images/ank_jump.png')
    ],
    'gameover': os.path.join(os.getcwd(), 'resources/images/gameover.png'),
    'ground': os.path.join(os.getcwd(), 'resources/images/ground.png'),
    'numbers': os.path.join(os.getcwd(), 'resources/images/numbers.png'),
    'vulture': os.path.join(os.getcwd(), 'resources/images/vulture.png'),
    'replay': os.path.join(os.getcwd(), 'resources/images/replay.png'),
    'background_start': os.path.join(os.getcwd(), 'resources/images/background_start.png'),
    'background': os.path.join(os.getcwd(), 'resources/images/background.png')
}

'''背景颜色'''
BACKGROUND_COLOR = (235, 235, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
