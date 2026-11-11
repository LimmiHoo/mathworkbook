# === Stage 17: Избранное ===
# Project: MathWorkbook
class Favorite:
    def __init__(self, problem_id, flag=True):
        self.problem_id = problem_id
        self.flag = flag

    @property
    def is_favorited(self):
        return self.flag

    def toggle(self):
        self.flag = not self.flag
        return self.flag

    def mark_favorite(self):
        self.flag = True

    def unmark_favorite(self):
        self.flag = False


def is_favorite(problem_id, favorites):
    return problem_id in favorites


def add_favorite(problem_id, favorites):
    favorites.append(Favorite(problem_id, True))
    return True


def remove_favorite(problem_id, favorites):
    for index, favorite in enumerate(favorites):
        if favorite.problem_id == problem_id:
            del favorites[index]
            return True
    return False


def toggle_favorite(problem_id, favorites):
    return add_favorite(problem_id, favorites) if not is_favorite(problem_id, favorites) else remove_favorite(problem_id, favorites)


def get_favorites(favorites):
    return sorted([favorite.problem_id for favorite in favorites], key=lambda problem_id: problem_id)


def is_favorites_empty(favorites):
    return len(favorites) == 0
