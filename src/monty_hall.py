import random


class MontyHall:
    def __init__(self):
        self._prize_door = self._pick_door()
        self._selected_door = None
        self._removed_door = None

    def _pick_door(self):
        return random.randint(1, 3)

    def _select_door(self):
        self._selected_door = self._pick_door()

    def _remove_door(self):
        door = self._pick_door()
        while door == self._selected_door or door == self._prize_door:
            door = self._pick_door()
        self._removed_door = door

    def _switch_choice(self):
        self._selected_door = 6 - self._selected_door - self._removed_door

    def _user_wins(self):
        return True if self._selected_door == self._prize_door else False

    def run_game(self, switch=True):
        self._select_door()
        self._remove_door()
        if switch:
            self._switch_choice()
        return self._user_wins()
