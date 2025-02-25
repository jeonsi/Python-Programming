import random

class Tic_Tac_Toe:

    # 게임판 생성
    def __init__(self):
        self.__board = []

    # 게임판 초기화
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('*')
            self.__board.append(row)

    # 첫 플레이어 선택
    def select_first_player(self):
        if random.randint(0, 1) == 0:  # randint returns 0 or 1
            return 'X'
        else:
            return 'O'

    # 기호 표시
    def mark_spot(self, row, col, player):
        self.__board[row][col] = player

    # 승리 상태 확인
    def is_win(self, player):
        n = len(self.__board)

        # 행 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.__board[i][j] != player:
                    win = False
                    break
            if win == True:
                return win

        # 열 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.__board[j][i] != player:
                    win = False
                    break
            if win == True:
                return win

        # 대각선 확인(우하향)
        win = True
        for i in range(n):
            if self.__board[i][i] != player:
                win = False
                break
        if win == True:
            return win

        # 대각선 확인(우상향)
        win = True
        for i in range(n):
            if self.__board[i][n - i - 1] != player:
                win = False
                break
        if win == True:
            return win

        return False

    # 잔여 빈칸 여부 확인
    def is_board_full(self):
        for row in self.__board:
            for item in row:
                if item == '*':
                    return False
        return True

    # 플레이어 변경
    def next_player(self, player):
        return 'X' if player == 'O' else 'O'

    # 현재 게임판 상태 출력
    def show_board(self):
        for row in self.__board:
            for item in row:
                print(item, end=" ")
            print()

    # 게임 시작
    def start(self):
        # 새 게임판 생성
        self.create_board()
        self.show_board()

        # 첫 플레이어 선택
        player = self.select_first_player()

        # 게임 루프 시작
        while True:
            # 다음 플레이어 안내
            if player == 'X':
                print("컴퓨터 차례입니다")
            else:
                print("사용자 차례입니다.")

            # 현재 게임판 상태 출력
            self.show_board()

            # 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
            if player == 'X':
                while True:
                    row, col = random.randint(1, 3), random.randint(1, 3)
                    if self.__board[row - 1][col - 1] == '*':
                        break
                print("컴튜터가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()
            else:
                row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요: ").split()))
                print("사용자가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()

            # row, col 입력값이 0, 0인 경우 게임 종료
            if row == 0 and col == 0:
                break

            # 입력된 위치 표시
            self.mark_spot(row - 1, col - 1, player)
            self.show_board()

            # 현재 플레이어가 이겼는지 확인
            if self.is_win(player):
                if player == 'X':
                    print("컴퓨터가 이겼습니다. 다시 도전하세요.")
                else:
                    print("사용자가 이겼습니다. 축하합니다.")
                break

            # 게임판 가득참 확인
            if self.is_board_full():
                print("무승부입니다. 다시 도전하세요")
                break

            # 플레이어 변경
            player = self.next_player(player)

        # 최종 게임판 출력
        print()
        self.show_board()


# 게임 생성
TTT = Tic_Tac_Toe()

# 게임 시작
TTT.start()
