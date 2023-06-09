# class 2

class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def say(self):
        return self.words + '.'


class Quote1(Quote):
    def say(self):
        return self.words + '!'


class Quote2(Quote):
    def say(self):
        return self.words + '?'


quote = Quote("person1", "what's up1")
quote1 = Quote1("person2", "what's up2")
quote2 = Quote2("person3", "what's up3")

a = quote
b = quote1
c = quote2

print(a.who(), a.say())
print(b.who(), b.say())
print(c.who(), c.say())
