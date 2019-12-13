from tkinter import *
import tkinter.messagebox
import tkinter
import random


class play(object):
    
    block_size = 100
    def __init__(self, parent):
        parent.title('Tic Tac Toe GUI')
        self.parent = parent

        self.initialize_game()

    def initialize_game(self):
        self.board = [None, None, None, None, None, None, None, None, None]
        self.map = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5, (2, 0): 6, (2, 1): 7,
                    (2, 2): 8}
        self.top_frame = tkinter.Frame(self.parent)
        self.top_frame.pack(side=tkinter.TOP)

        restart_button = tkinter.Button(self.top_frame, text='New Game', width=30, height=3,
                                        command=self.restart)
        restart_button.pack()

        self.bottom_frame=tkinter.Frame(self.parent)
        self.bottom_frame.pack(side=tkinter.BOTTOM)

        self.my_lbl=tkinter.Label(self.bottom_frame,text=None)
        self.my_lbl.pack()

        self.canvas = tkinter.Canvas(self.top_frame,
                                     width=self.block_size * 3,
                                     height=self.block_size * 3)

        for ro in range(3):
            for col in range(3):

                self.canvas.create_rectangle(self.block_size * col,
                                             self.block_size * ro,
                                             self.block_size * (col + 1),
                                             self.block_size * (ro + 1),fill='white')

        self.canvas.bind("<Button-1>", self.play)
        self.canvas.pack()

    def board_full(self):
        if None not in self.board:
            return True
        else:
            return False


    def possible_moves(self):
        """return: list of possible moves"""
        possible_moves = []
        for i in range(0, 9):
            if self.board[i] is None:
                possible_moves.append(i)
            else:
                pass
        return possible_moves

    def pc_move(self):
        m = True
        while m:
            pc_move = random.randint(0, 8)
            if pc_move in self.possible_moves():
                self.board[pc_move] = 'O'
                self.canvas.itemconfigure(tagOrId=(pc_move+1),fill='blue')
                m = False
            else:
                continue
        return self

    def draw_out(self):
        """to be deleted"""
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])

    def play(self, event):
        """
        when the player clicks on a un-taken square, this method first translate cursor into cell number,
        then update game board and check game result based on condition
        :parameter: click
        :return: updated game object
        """
        print('clicked', event.y, event.x)
        cx = self.canvas.canvasx(event.x)
        cy = self.canvas.canvasy(event.y)
        cid = self.canvas.find_closest(cx,cy)[0]
        my_move = self.map[(cy // self.block_size, cx // self.block_size)]
        if self.board[my_move] is None:
            self.board[my_move] = 'X'
            self.canvas.itemconfigure(cid,fill='green') # green color for player
        else:
            return None

        self.draw_out()
        if self.check_game()is not None:
            print(self.check_game())
        else:
            pass
        self.possible_moves()
        self.pc_move()                            
        self.draw_out()                          
        if self.check_game()is not None:
            print(self.check_game()) 
        else:
            pass
        return self

    def check_game(self):
        """
        Check if the game is win or lost or a tie
        Return:  win, lose, tie, none """
        result=None
        if (self.board[0] == self.board[1] == self.board[2] == 'X') or (
                            self.board[3] == self.board[4] == self.board[5] == 'X') or (
                            self.board[6] == self.board[7] == self.board[8] == 'X') or (
                            self.board[0] == self.board[3] == self.board[6] == 'X') or (
                            self.board[1] == self.board[4] == self.board[7] == 'X') or (
                            self.board[2] == self.board[5] == self.board[8] == 'X') or (
                            self.board[0] == self.board[4] == self.board[8] == 'X') or (
                            self.board[2] == self.board[4] == self.board[6] == 'X'):
            result = 'You win!'
            self.my_lbl.configure(text=result)
        elif (self.board[0] == self.board[1] == self.board[2] == 'O') or (
                            self.board[3] == self.board[4] == self.board[5] == 'O') or (
                            self.board[6] == self.board[7] == self.board[8] == 'O') or (
                            self.board[0] == self.board[3] == self.board[6] == 'O') or (
                            self.board[1] == self.board[4] == self.board[7] == 'O') or (
                            self.board[2] == self.board[5] == self.board[8] == 'O') or (
                            self.board[0] == self.board[4] == self.board[8] == 'O') or (
                            self.board[2] == self.board[4] == self.board[6] == 'O'):
            result = 'You lost!'
            self.my_lbl.config(text=result)
        elif self.board_full()is True:
                result = 'A tie!'
                self.my_lbl.configure(text=result)
        else:
            pass
        return result


    def restart(self):
        
        self.top_frame.destroy()
        self.bottom_frame.destroy()
        self.initialize_game()


def main():
    root = tkinter.Tk()
    the_game = play(root)
    root.mainloop()

if __name__ == '__main__':
    main()