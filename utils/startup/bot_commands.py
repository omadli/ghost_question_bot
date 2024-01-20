from aiogram import Bot, types


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            types.BotCommand(command="start", description="Start bot"),
            types.BotCommand(command="help", description="Help"),
            types.BotCommand(command="about", description="About"),
            types.BotCommand(command="cancel", description="Cancel action"),
            types.BotCommand(command="language", description="Set language"),
        ]
    )
    