from random import shuffle


class Card:
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    suites = ['буби', 'черви', 'крести', 'пики']

    def __init__(self, v, s):
        """v and s must be integer"""
        self.value = v
        self.suite = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suite < c2.suite:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suite > c2.suite:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' ' + self.suites[self.suite]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(0, 4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def take_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.win = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input('Введите имя первого игрока: ')
        name2 = input('Введите имя второго игрока: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        text = "{} выиграл раунд"
        return text.format(winner)

    def draw(self, p1n, p1c, p2n, p2c):
        text = "{} кладет {}, а {} кладет {}"
        text = text.format(p1n, p1c, p2n, p2c)
        print(text)

    def play_game(self):
        cards = self.deck.cards
        print('Поехали!')

        while len(cards) >= 2:
            message = "Введите X если хотите закончить игру или любую другую кнопку чтобы играть: "
            response = input(message).upper()
            if response == 'X':
                break
            p1c = self.deck.take_card()
            p2c = self.deck.take_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.wins(p1n)
                self.p1.win += 1
            else:
                self.wins(p2n)
                self.p2.win += 1

        win = self.winner(self.p1, self.p2)

        print("Игра окончена. {} победил".format(win))

    def winner(self, p1, p2):
        if p1.win > p2.win:
            return p1.name
        elif p1.win < p2.win:
            return p2.name
        else:
            return 'Ничья!'

game = Game()
game.play_game()