from states_events.menu_content.button_callbacks import ButtonCallback


def str_to_confirmation(callback: str) -> bool:
    if callback == ButtonCallback.SAVE_GAME:
        return True
    else:
        return False
