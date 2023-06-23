import random

class Game:
    def __init__(self):
        self.player_card = None
        self.comp_card = None
        self.tokens = 90
        self.player_score = 0
        self.comp_score = 0

    def start_game(self):
        print('Начало игры')

    def build_bingo_card(self):
        card = []
        numbers = list(range(1, 91))
        random.shuffle(numbers)

        for _ in range(3):
            row = []
            for _ in range(9):
                if numbers:
                    # Вероятность пропуска числа составляет 20%
                    if random.random() < 0.4:
                        row.append('')
                    else:
                        row.append(numbers.pop())
                else:
                    row.append('')
            card.append(row)

        return card

    def print_bingo_card(self, card):
        for row in card:
            print(*row)

    def print_combined_cards(self):
        print("------ Ваша карточка -----")
        self.print_bingo_card(self.player_card)
        print("--------------------------")
        print("-- Карточка компьютера ---")
        self.print_bingo_card(self.comp_card)
        print("--------------------------")

    def make_move(self):
        if self.tokens == 0:
            print("Фишки закончились.")
            self.print_scores()
            self.end_game()
            return

        print("Новый бочонок: {} (осталось {})".format(self.current_number, self.tokens))
        self.print_combined_cards()
        choice = input("Зачеркнуть цифру? (y/n): ")

        if choice.lower() == 'y':
            if self.current_number in self.player_card:
                self.player_card = self.mark_number(self.player_card, self.current_number)
                self.check_win()
            else:
                print("Вы проиграли.")
                self.comp_score += 1
                self.print_scores()
                self.end_game()
        elif choice.lower() == 'n':
            if self.current_number in self.player_card:
                print("Вы проиграли.")
                self.comp_score += 1
                self.print_scores()
                self.end_game()
            else:
                self.check_win()

    def mark_number(self, card, number):
        for row in card:
            if number in row:
                row[row.index(number)] = '-'
        return card

    def check_win(self):
        if all(all(cell == '-' for cell in row) for row in self.player_card):
            print("Вы победили!")
            self.player_score += 1
            self.print_scores()
            self.end_game()
            return True
        elif all(all(cell == '-' for cell in row) for row in self.comp_card):
            print("Компьютер победил.")
            self.comp_score += 1
            self.print_scores()
            self.end_game()
            return True
        return False

    def print_scores(self):
        print("Счет:")
        print("Игрок: {}".format(self.player_score))
        print("Компьютер: {}".format(self.comp_score))

    def end_game(self):
        print("Программа завершена.")

    def run(self):
        self.start_game()
        self.player_card = self.build_bingo_card()
        self.comp_card = self.build_bingo_card()

        while True:
            self.current_number = random.randint(1, 90)
            self.tokens -= 1

            self.make_move()

            if self.check_win():
                break

            print()

        self.print_scores()
        self.end_game()

if __name__ == '__main__':
    game = Game()
    game.run()