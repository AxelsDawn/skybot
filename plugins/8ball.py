from util import hook
import random
r="\x02\x0305" #red
g="\x02\x0303" #green
y="\x02\x0308" #yellow
answers = [g+"As I see it, yes",
g+"It is certain",
g+"It is decidedly so",
g+"Most likely",
g+"Outlook good",
g+"Signs point to yes",
g+"Without a doubt",
g+"Yes",
g+"Yes, definitely",
g+"You may rely on it",
y+"Reply hazy, try again",
y+"Ask again later",
y+"Better not tell you now",
y+"Cannot predict now",
y+"Concentrate and ask again",
r+"Don't count on it",
r+"My reply is no",
r+"My sources say no",
r+"Outlook not so good",
r+"Very doubtful"]

@hook.command
@hook.command("8ball")
def eightball(inp, say=None):
    ".8ball <question> - ask the 8ball a question"
    return inp+": "+random.choice(answers)
