from Fool import Fool
import pytest
# import sys
# sys.setrecursionlimit(10)

class TestFool:
    def setup(self):
        self.game = Fool(3)
        k = 0
        for i in range(1, self.game.n_players + 1):
            setattr(Fool, 'pl' + str(i), self.game.deck[k:i * 6])
            k += 6
        self.game.deck = self.game.deck[k:]
        self.game.bita = []
        self.game.out_of_game = []

    def resetup(self):
        k = 0
        for i in range(1, self.game.n_players + 1):
            setattr(Fool, 'pl' + str(i), self.game.deck[k:i * 6])
            k += 6
        self.game.deck = self.game.deck[k:]
        self.game.bita = []
        self.game.out_of_game = []

    @property
    def get_game(self):
        return self.game

    @get_game.setter
    def get_game(self,N):
        if 2 < int(N) <= 6:
            self.game = Fool(int(N))
        else:
            raise ValueError('Неправильное число игроков')


    def teardown(self):
        del self.game

    def test_deck(self):
        assert type(self.game.deck) == type(list())

    def test_bita(self):
        self.game.move('1')
        assert isinstance(self.game.bita[0][1],int)

    def test_out_of_game(self):
        assert len(self.game.out_of_game) == 0

        with pytest.raises(ValueError):
            self.get_game = 8


    def test_n_pl(self):
        self.get_game = 6
        assert self.game.n_players < 7
        assert self.game.n_players ==6

    def test_pl1(self):
        self.get_game = 6
        assert hasattr(self.game,'pl1')

    def test_pl2(self):
        self.get_game = 6
        assert hasattr(self.game,'pl2')

    def test_pl3(self):
        self.get_game = 6
        self.resetup()
        assert hasattr(self.game,'pl3')

    def test_pl4(self):
        self.get_game = 6
        assert hasattr(self.game,'pl4')

    def test_pl5(self):
        self.get_game = 6
        self.resetup()
        assert hasattr(self.game,'pl5')

    def test_pl6(self):
        self.get_game = 6
        self.resetup()
        assert hasattr(self.game,'pl6')

    def test_deck(self):
        assert len(self.game.hearts)==len(self.game._spades)==len(self.game._clubs)==len(self.game._diamonds)

    def test_looser(self):
        self.game.move('1')
        self.game.looser('2')
        assert len(self.game.pl2) == 7

# pytest -s pytest_class.py
# coverage run pytest_class.py
# coverage report

# Name              Stmts   Miss  Cover
# -------------------------------------
# Fool.py              73     62    15%
# pytest_class.py      70     48    31%
# -------------------------------------
# TOTAL               143    110    23%
