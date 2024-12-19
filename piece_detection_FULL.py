import os
import time
import subprocess
import requests
import json
import matplotlib.pyplot as plt
import chess
import chess.engine
from PIL import Image, ImageDraw, ImageFont
from emailer import send_email

ROBOFLOW_API_KEY = "kHFc4vjYE3ReeCa39o4T"  
model_id = "chess-piece-detection-5ipnt/2" 
api_url = f"https://detect.roboflow.com/{model_id}?api_key={ROBOFLOW_API_KEY}"

stockfish_path = r"/home/levi/stockfish/src/stockfish"

engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

# with open("inference_result.jpg", "rb") as img_file:
#     response = requests.post(api_url, files={"file": img_file})

# results = response.json()
# print(json.dumps(results, indent=2))

# draw = ImageDraw.Draw(image)
# font = ImageFont.load_default()  # Use default font

# for prediction in results['predictions']:
#     x = prediction['x']
#     y = prediction['y']
#     width = prediction['width']
#     height = prediction['height']
#     confidence = prediction['confidence']
#     label = prediction['class']

#     top_left = (x - width // 2, y - height // 2)
#     bottom_right = (x + width // 2, y + height // 2)

#     if confidence > 0.75:
#         color = "green"
#     elif 0.5 <= confidence <= 0.75:
#         color = "yellow"
#     else:
#         color = "red"

#     draw.rectangle([top_left, bottom_right], outline=color, width=2)
#     draw.text((top_left[0], top_left[1] - 10), f"{label} ({confidence:.2f})", fill=color, font=font)

# output_path = "annotated_output_image.jpg"
# image = image.resize((1200, 1200), Image.Resampling.LANCZOS) 
# image.save(output_path)

# plt.figure(figsize=(12, 12))  
# plt.imshow(image)
# plt.axis('off')
# plt.show()

folder_to_monitor = "./modified_images"

existing_files = set(os.listdir(folder_to_monitor))

print(f"Monitoring folder: {folder_to_monitor}...")
try:
    while True:
        current_files = set(os.listdir(folder_to_monitor))
        
        new_files = current_files - existing_files
        print(new_files)
        if new_files:
            for new_file in new_files:

                array = [[None for _ in range(8)] for _ in range(8)]

                def find_letter(pred_class):
                    parsed = pred_class.split("-")
                    letter = None
                    if (parsed[1] == "pawn"):
                        letter = "p"
                    elif (parsed[1] == "rook"):
                        letter = "r"
                    elif (parsed[1] == "bishop"):
                        letter = "b"
                    elif (parsed[1] == "knight"):
                        letter = "n"
                    elif (parsed[1] == "king"):
                        letter = "k"
                    elif (parsed[1] == "queen"):
                        letter = "q"

                    if (parsed[0] == "white"): 
                        letter = letter.upper()

                    return letter

                def find_position(x,y,height,image_width,image_height):
                    first_index = int((y + height / 4 - 90) / (image_height - 90 * 2) * 8) # int to floor
                    second_index = int((x - 90) / (image_width - 90 * 2) * 8)

                    return first_index, second_index

                def place_letter(letter, first_index, second_index):
                    array[first_index][second_index] = letter

                def matrix_to_fen(matrix):
                    fen_rows = []

                    for row in matrix:
                        fen_row = ""
                        empty_count = 0
                        for square in row:
                            if square is None:
                                empty_count += 1
                            else:
                                if empty_count > 0:
                                    fen_row += str(empty_count)
                                    empty_count = 0
                                fen_row += square

                        if empty_count > 0:
                            fen_row += str(empty_count)

                        fen_rows.append(fen_row)

                    board_fen = "/".join(fen_rows)

                    side_to_move = "w"       
                    castling = "KQkq"        
                    en_passant = "-"         
                    halfmove_clock = "0"     
                    fullmove_number = "1"    

                    fen = f"{board_fen} {side_to_move} {castling} {en_passant} {halfmove_clock} {fullmove_number}"

                    return fen

                def get_best_move(fen: str):
                    board = chess.Board(fen)

                    result = engine.play(board, chess.engine.Limit(depth=20)) 
                    best_move = result.move

                    return best_move

                with open("inference_result.jpg", "rb") as img_file:
                    response = requests.post(api_url, files={"file": img_file})

                data = response.json()

                image_width = data["image"]["width"]
                image_height = data["image"]["height"]

                predictions = data["predictions"]
                for prediction in predictions:
                    x = prediction["x"]
                    y = prediction["y"]
                    height = prediction["height"]
                    pred_class = prediction["class"]

                    letter = find_letter(pred_class)
                    first_index, second_index = find_position(x, y, height, image_width, image_height)
                    place_letter(letter, first_index, second_index)

                print(array)
                fen = matrix_to_fen(array)
                print(fen)

                try:
                    best_move = get_best_move(fen)
                    print("Best move:", best_move)
                    subject = str(best_move)
                    engine.quit()
                except Exception as e:
                    subject = "retry image:" + str(e)
                    print(subject)
                    
                send_email(subject)
                
                file_path = folder_to_monitor + "/" + str(new_file) 
                os.remove(file_path)
        
        existing_files = current_files
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
