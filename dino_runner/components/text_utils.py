from pygame.font import Font
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = 'freesansbold.ttf'
black_color = (0,0,0)

def get_message(message,size,witdh = SCREEN_WIDTH // 2,heigth= SCREEN_HEIGHT// 2):
    font =Font(FONT_STYLE,size)
    text=font.render(message, True,black_color)
    text_rect = text.get_rect()
    text_rect.center=(witdh, heigth)
    return text, text_rect
