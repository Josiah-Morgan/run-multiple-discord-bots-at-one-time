# run-multiple-discord-bots-at-one-time
Runs other bots from a command from one main bot. Other bots are turned with threads


# How to use it

Put a discord bot token in the data.py and invite the bot to a server

Make a folder(s)/cog(s) for the commands you want on the bots on threads (not the main bot, put any extra commands for the main bot in the folder you use for the data.py cog loader)

Run either one of the commands: /bot-add-server or /bot-add-global


# Why use this?

- To run multiple custom bots that use the same code on one host (you have one main bot and users can run a command to turn on the custom/private bot)
- Have one host provider to run all your bots, instead of having to get a new host everytime you make a new bot, just run them all on the same one
