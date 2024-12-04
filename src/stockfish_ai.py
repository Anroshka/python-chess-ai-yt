import chess
import chess.engine
import os
from const import *
from move import Move
from square import Square

class StockfishAI:
    def __init__(self, game, depth=10):
        self.game = game
        self.board = game.board
        self.thinking = False
        self.depth = depth
        # Путь к исполняемому файлу Stockfish
        stockfish_path = self._get_stockfish_path()
        try:
            self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
            self.engine.configure({"Skill Level": 20})  # Максимальный уровень мастерства
        except Exception as e:
            print(f"Error initializing Stockfish: {e}")
            self.engine = None

    def _get_stockfish_path(self):
        """Get the path to Stockfish executable based on OS"""
        if os.name == 'nt':  # Windows
            return os.path.join(os.path.dirname(os.path.dirname(__file__)), "stockfish", "stockfish-windows-x86-64-avx2.exe")
        elif os.name == 'posix':  # Linux/Mac
            return os.path.join(os.path.dirname(os.path.dirname(__file__)), "stockfish", "stockfish")
        else:
            raise Exception("Unsupported operating system")

    def get_ai_move(self):
        """Get best move from Stockfish"""
        if not self.engine:
            return None

        self.thinking = True
        try:
            # Convert our board to chess.Board
            fen = self._convert_to_fen()
            chess_board = chess.Board(fen)

            # Get move from Stockfish
            result = self.engine.play(chess_board, chess.engine.Limit(depth=self.depth))
            if result.move:
                # Convert chess.Move to our Move format
                move = self._convert_move(result.move)
                self.thinking = False
                return move
        except Exception as e:
            print(f"Error getting move from Stockfish: {e}")
        
        self.thinking = False
        return None

    def _convert_to_fen(self):
        """Convert our board representation to FEN string"""
        fen = []
        empty = 0
        
        # Board position
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                if square.has_piece():
                    if empty > 0:
                        fen.append(str(empty))
                        empty = 0
                    piece = square.piece
                    symbol = piece.name[0]
                    if piece.name == 'knight':
                        symbol = 'n'
                    if piece.color == 'white':
                        symbol = symbol.upper()
                    fen.append(symbol)
                else:
                    empty += 1
            if empty > 0:
                fen.append(str(empty))
                empty = 0
            if row < 7:
                fen.append('/')
        
        # Active color
        fen.append(' w ' if self.game.next_player == 'white' else ' b ')
        
        # Castling availability (simplified)
        fen.append('KQkq ')
        
        # En passant target square (simplified)
        fen.append('- ')
        
        # Halfmove clock and fullmove number (simplified)
        fen.append('0 1')
        
        return ''.join(fen)

    def _convert_move(self, chess_move):
        """Convert chess.Move to our Move format"""
        from_square = chess_move.from_square
        to_square = chess_move.to_square
        
        from_row = 7 - (from_square // 8)
        from_col = from_square % 8
        to_row = 7 - (to_square // 8)
        to_col = to_square % 8
        
        initial = Square(from_row, from_col)
        final = Square(to_row, to_col)
        
        return Move(initial, final)

    def quit(self):
        """Properly close the Stockfish engine"""
        if self.engine:
            self.engine.quit()
