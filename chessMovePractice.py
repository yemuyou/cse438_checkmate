import chess
import chess.engine

# Specify the path to your Stockfish binary
stockfish_path = r"C:\Users\louan\CSCE_438\stockfish-windows-x86-64-avx2 (1)\stockfish\stockfish-windows-x86-64-avx2.exe"

# Initialize the engine
engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)


def get_best_move(fen: str):
    # Set up the board using the FEN notation
    board = chess.Board(fen)
    
    # # Use the engine to find the best move
    result = engine.play(board, chess.engine.Limit(depth=20))  # Higher depth for deeper analysis
    best_move = result.move
    print(board)

    return best_move

# Example usage with a FEN string (white to move)
fen = "rnbqkbnr/ppp1pppp/8/3p4/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 2"
best_move = get_best_move(fen)

print("Best move:", best_move)

# Close the engine when done
engine.quit()
