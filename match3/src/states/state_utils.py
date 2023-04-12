import settings


def get_virtual_position(position):
    pos_x, pos_y = position
    pos_x = pos_x * settings.VIRTUAL_WIDTH // settings.WINDOW_WIDTH
    pos_y = pos_y * settings.VIRTUAL_HEIGHT // settings.WINDOW_HEIGHT

    return pos_x, pos_y
