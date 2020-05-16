"""
Author: BronTheDev

Simple Text Based TicTacToe Game
"""
print("Welcome to TicTacToe \n")


def start_Game():

    def play():
        game = True
        while game is True:
            p1 = input("Welcome Player One, Please enter a Character for your board \n")
            print("\n")
            p2 = input("Welcome Player Two, Please enter a Character for your board \n")
            print("\n")
            token = {"T1": "1",
                     "T2": "2",
                     "T3": "3",
                     "T4": "4",
                     "T5": "5",
                     "T6": "6",
                     "T7": "7",
                     "T8": "8",
                     "T9": "9"}
            pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                       2: "-------------------------",
                       3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                       4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                       }
            board = {1: [1],
                     2: [2],
                     3: [3],
                     4: [2],
                     5: [4],
                     }
            for x in range(1, 6):
                for patterns in board[x]:
                    print(pattern[patterns])
            print("\n")

            def check_Win():
                if token["T1"] == token["T2"] == token["T3"]:
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

                if token["T7"] == token["T8"] == token["T9"]:
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

                if (token["T4"] == token["T5"] == token["T6"]):
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

                if (token["T1"] == token["T5"] == token["T9"]):
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

                if (token["T7"] == token["T5"] == token["T3"]):
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

                if (token["T1"] == token["T4"] == token["T7"]):
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

                if (token["T2"] == token["T5"] == token["T8"]):
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

                if (token["T3"] == token["T6"] == token["T9"]):
                    if token["T1"] == p1:
                        print("Congratulations. Player One! YOU WIN!!!!")
                        return True
                    else:
                        print("Congratulations. Player Two! YOU WIN!!!!")
                        return True

            for turn in range(0, 9):
                if check_Win():
                    game = False
                    break
                if turn % 2 == 0:
                    b_Piece = input("Player 1, Choose a coordinate to place your token \n")
                    if int(b_Piece) == 1:
                        token["T1"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }

                    if int(b_Piece) == 2:
                        token["T2"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 3:
                        token["T3"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 4:
                        token["T4"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 5:
                        token["T5"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 6:
                        token["T6"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 7:
                        token["T7"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 8:
                        token["T8"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 9:
                        token["T9"] = p1
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }

                else:
                    b_Piece = input("Player 2, Choose a coordinate to place your token \n")
                    if int(b_Piece) == 1:
                        token["T1"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 2:
                        token["T2"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 3:
                        token["T3"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 4:
                        token["T4"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 5:
                        token["T5"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 6:
                        token["T6"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 7:
                        token["T7"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 8:
                        token["T8"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }
                    if int(b_Piece) == 9:
                        token["T9"] = p2
                        pattern = {1: f"   {token['T1']}   |   {token['T2']}   |   {token['T3']}   ",
                                   2: "-------------------------",
                                   3: f"   {token['T4']}   |   {token['T5']}   |   {token['T6']}   ",
                                   4: f"   {token['T7']}   |   {token['T8']}   |   {token['T9']}   ",
                                   }

                for x in range(1, 6):
                    for patterns in board[x]:
                        print(pattern[patterns])
                print("\n")


    play()


start_Game()
