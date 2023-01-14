class Bot:
    def __init__(self, intro):
        self.intro = intro
    def introduce(self):
        return "My name is " + self.intro + "! I am a BOT!"
    @staticmethod
    def good_luck(good_luck):
        return "Nice to meet you {}! Good luck for the Bootcamp!".format(good_luck)
    @staticmethod
    def random_quote():
        import random
        lis1 = ["Creativity takes courage.", "Your limitation is only your imagination.",
                "Making mistakes is better than faking perfection."]
        return random.choice(lis1)
bot = Bot('Alexa')
print(bot.introduce())
print(bot.good_luck("Siri"))
print(bot.random_quote())
print(bot.random_quote())
print(bot.random_quote())