class Game:

    def __init__(self) -> None:
        self.answer = None

    def lets_play(self):
        from random import randint

        print("Давай немного отвлечёмся от программирования и немного отдохнем")
        print("Я загадал число, если отгадаешь - отдохнешь 5 минуточек, если нет - шуруй заниматься")
        print(";)")
        print("Кстати, у тебя 10 попыток")
        self.answer = randint(0, 1001)
        k = 10
        while True:
            qui: str = input(f"Давай, осталось {k} попыток: ")
            if qui.isdigit() == False:
                print("Зачем ты вводишь буквы? У тебя и так мало попыток))")
            else:
                qui = int(qui)
                if self.answer == qui:
                    print("Браво! Отдыхай))")
                    break
                elif self.answer > qui:
                    print("Маловато, давай больше")
                else:
                    print("Многовато, убавляй")
            k -= 1
            if k == 0:
                print("Проиграл(( Ну считай, что уже отдохнул")
                break


break_five_sec = Game()
break_five_sec.lets_play()
