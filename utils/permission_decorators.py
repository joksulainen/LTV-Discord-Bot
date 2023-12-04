from discord.ext.commands import CheckFailure, Context, check


def is_admin():
    def predicate(ctx: Context) -> bool:
        if (not ctx.author.id in ctx.bot.config.admin_ids and
            not (ctx.author.id == ctx.bot.owner_id or ctx.author.id in ctx.bot.owner_ids)):
            raise NotAdmin()
        return True
    return check(predicate)

def is_moderator():
    def predicate(ctx: Context) -> bool:
        if (not (ctx.author.id in ctx.bot.config.moderator_ids + ctx.bot.config.admin_ids) and
            not (ctx.author.id == ctx.bot.owner_id or ctx.author.id in ctx.bot.owner_ids)):
            raise NotModerator()
        return True
    return check(predicate)


class NotAdmin(CheckFailure):
    def __init__(self) -> None:
        super().__init__("Not admin")

class NotModerator(CheckFailure):
    def __init__(self) -> None:
        super().__init__("Not moderator")
