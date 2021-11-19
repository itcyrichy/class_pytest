import random
import types

class Fool:
    def __init__(self,n_players,*args,trump_card = 'random',**kwargs):
        card_suits = ['spades','clubs','hearts','diamonds']
        self.n_players = n_players
        self.trump_card = card_suits[random.randint(0,3)] if trump_card == 'random' else trump_card
        if self.trump_card == 'hearts':
            self.__hearts = {'six_hearts':15,'seven_hearts':16,'eight_hearts':17,'nine_hearts':18,'ten_hearts':19,'jack_hearts':20,'queen_hearts':21,'king_hearts':22,'ace_hearts':23}
        else:
            self.__hearts = {'six_hearts': 6, 'seven_hearts': 7, 'eight_hearts': 8, 'nine_hearts': 9, 'ten_hearts': 10, 'jack_hearts': 11, 'queen_hearts': 12,
                             'king_hearts': 13, 'ace_hearts': 14}
        if self.trump_card == 'spades':
            self._spades = {'six_spades':15,'seven_spades':16,'eight_spades':17,'nine_spades':18,'ten_spades':19,'jack_spades':20,'queen_spades':21,'king_spades':22,'ace_spades':23}
        else:
            self._spades = {'six_spades': 6, 'seven_spades': 7, 'eight_spades': 8, 'nine_spades': 9, 'ten_spades': 10, 'jack_spades': 11, 'queen_spades': 12,
                             'king_spades': 13, 'ace_spades': 14}
        if self.trump_card == 'clubs':
            self._clubs = {'six_clubs':15,'seven_clubs':16,'eight_clubs':17,'nine_clubs':18,'ten_clubs':19,'jack_clubs':20,'queen_clubs':21,'king_clubs':22,'ace_clubs':23}
        else:
            self._clubs = {'six_clubs': 6, 'seven_clubs': 7, 'eight_clubs': 8, 'nine_clubs': 9, 'ten_clubs': 10, 'jack_clubs': 11, 'queen_clubs': 12,
                             'king_clubs': 13, 'ace_clubs': 14}
        if self.trump_card == 'diamonds':
            self._diamonds = {'six_diamonds':15,'seven_diamonds':16,'eight_diamonds':17,'nine_diamonds':18,'ten_diamonds':19,'jack_diamonds':20,'queen_diamonds':21,'king_diamonds':22,'ace_diamonds':23}
        else:
            self._diamonds = {'six_diamonds': 6, 'seven_diamonds': 7, 'eight_diamonds': 8, 'nine_diamonds': 9, 'ten_diamonds': 10, 'jack_diamonds': 11, 'queen_diamonds': 12,
                             'king_diamonds': 13, 'ace_diamonds': 14}
        self.deck = dict(list(self._clubs.items())+list(self._diamonds.items())+list(self._spades.items())+list(self.__hearts.items()))
        self.deck = random.sample([x for x in self.deck.items()],36)

    @property
    def hearts(self):
        return self.__hearts

    def rround(self):
        print('Начните игру')

    def move(self,player_number):
        if str(player_number)=='1':
            print(self.pl1, f'Козырь: {self.trump_card}')
            card1 = input('Выберите карту: ')
            self.bita.append(self.pl1.pop(int(card1)))

        elif str(player_number) == '2':
            print(self.pl2, f'Козырь: {self.trump_card}')
            card2 = input('Выберите карту: ')
            self.bita.append(self.pl2.pop(int(card2)))

        elif str(player_number) == '3':
            print(self.pl3, f'Козырь: {self.trump_card}')
            card3 = input('Выберите карту: ')
            self.bita.append(self.pl3.pop(int(card3)))

        elif str(player_number) == '4':
            print(self.pl4, f'Козырь: {self.trump_card}')
            card4 = input('Выберите карту: ')
            self.bita.append(self.pl4.pop(int(card4)))

        elif str(player_number) == '5':
            print(self.pl5, f'Козырь: {self.trump_card}')
            card5 = input('Выберите карту: ')
            self.bita.append(self.pl5.pop(int(card5)))

        elif str(player_number) == '6':
            print(self.pl6, f'Козырь: {self.trump_card}')
            card6 = input('Выберите карту: ')
            self.bita.append(self.pl6.pop(int(card6)))

        else:
            print('Неверное кол-во игроков')

    def looser(self,player_number):
        if str(player_number) == '1':
            self.pl1 = self.pl1 + self.bita

        elif str(player_number) == '2':
            self.pl2 = self.pl2 + self.bita

        elif str(player_number) == '3':
            self.pl3 = self.pl3 + self.bita

        elif str(player_number) == '4':
            self.pl4 = self.pl4 + self.bita

        elif str(player_number) == '5':
            self.pl5 = self.pl5 + self.bita

        elif str(player_number) == '6':
            self.pl6 = self.pl6+self.bita

    def lucky(self):
        self.out_of_game = self.bita
        self.bita = []

    def take_cards(self,player,num_of_cards):
        for i in range(1,num_of_cards+1):
            player.append(self.deck[-i])

        self.deck = self.deck[:-num_of_cards]
        print(player)


# def play(n_players=5):
#     n_players = int(input('Введите кол-во игроков: '))
#     f = Fool(n_players)
#     no_fool = True
#     while f.n_players > 6 or f.n_players < 1:
#         print('Выберите кол-во игроков от 1-го до 6: ')
#         n_players = int(input('Введите кол-во игроков: '))
#     else:
#         k = 0
#         for i in range(1, f.n_players + 1):
#             setattr(Fool, 'pl' + str(i), f.deck[k:i * 6])
#             k += 6
#     f.deck = f.deck[k:]
#     f.bita = []
#     f.out_of_game = []
#     while no_fool:
#         action = input('Введите действие (ход/бита/снял/взять карту/обстановка): ')
#         if action == 'ход':
#             try:
#                 f.move(input('Введите номер игрока (от 1 до 6): '))
#             except:
#                 print('Неверно указан номер игрока')
#         elif action == 'бита':
#             f.lucky()
#         elif action == 'обстановка':
#             for i in range(1, f.n_players + 1):
#                 if hasattr(f, 'pl' + str(i)):
#                     print(getattr(f, 'pl' + str(i)),'\n')
#             print(len(f.deck),'\n')
#             print(f.out_of_game)
#             print(f.bita)
#
#
#         elif action == 'снял':
#             try:
#                 f.looser(input('Введите номер игрока (от 1 до 6): '))
#                 f.lucky()
#             except:
#                 print('Неверно указан номер игрока')
#         elif action == 'взять карту':
#             action2 = input('Введите номер игрока (от 1 до 6): ')
#             try:
#                 if str(action2) == '1':
#                     player = f.pl1
#                 elif str(action2) == '2':
#                     player = f.pl2
#                 elif str(action2) == '3':
#                     player = f.pl3
#                 elif str(action2) == '4':
#                     player = f.pl4
#                 elif str(action2) == '5':
#                     player = f.pl5
#                 elif str(action2) == '6':
#                     player = f.pl6
#                 num = int(input('Введите кол-во карт: '))
#                 f.take_cards(player,num)
#             except:
#                 print('Неправильно введен номер игрока')
#
#
#         else:
#             print('Ничего не понимаю, неправильная команда')
#         checker = []
#         for i in range(1,f.n_players+1):
#             if hasattr(f, 'pl'+str(i)):
#                 if len(getattr(f,'pl'+str(i))) > 0:
#                     checker.append(1)
#         if len(f.deck)>0:
#             checker.append(1)
#         if sum(checker)>1:
#             no_fool = True
#         else:
#             no_fool = False
#     print('Игра завершена')
#
# play()