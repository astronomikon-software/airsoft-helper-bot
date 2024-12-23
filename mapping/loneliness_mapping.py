from states_events.menu_content.button_callbacks import ButtonCallback


def str_to_loneliness(callback: str) -> bool:
    if callback == ButtonCallback.TRUE:
        return True
    elif callback == ButtonCallback.FALSE:
        return False
    
def loneliness_to_str(is_loneliness_friendly: bool) -> str:
    if is_loneliness_friendly:
        return 'Да'
    else:
        return 'Нет'