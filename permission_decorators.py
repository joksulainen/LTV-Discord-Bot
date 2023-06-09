from discord.ext.commands import CheckFailure, check, Context

from handlers.config import CONFIG


def is_admin():
    def predicate(ctx: Context) -> bool:
        if not ctx.author.id in CONFIG.admin_ids:
            raise NotAdmin()
        return True
    return check(predicate)

def is_moderator():
    def predicate(ctx: Context) -> bool:
        if not ctx.author.id in CONFIG.moderator_ids + CONFIG.admin_ids:
            raise NotModerator()
        return True
    return check(predicate)


class NotAdmin(CheckFailure):
    def __init__(self) -> None:
        super().__init__("Not admin")

class NotModerator(CheckFailure):
    def __init__(self) -> None:
        super().__init__("Not moderator")
