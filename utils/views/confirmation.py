import discord
from discord.ui import View, Button


class ConfirmationView(View):
    decision: bool | None = None
    
    def __init__(self, /, timeout: float = 30, disable_on_timeout: bool = True, **kwargs):
        super().__init__(timeout=timeout, disable_on_timeout=disable_on_timeout, **kwargs)
        self.add_item(Button(label="Yes", style=discord.ButtonStyle.green))
        self.add_item(Button(label="No", style=discord.ButtonStyle.red))
