# The CheckMate Glasses

Use these glasses to learn the game of chess and beat any opponent! Simply press the button on the side, and the camera will take a picture of the chess board in front of you. *(It works best from a tall angle, but can also work from a slant.)*

## How It Works

1. **Capture the Board**  
   The camera on the glasses captures an image of the chessboard.

2. **Send to Azure Blob Storage**  
   The captured image is uploaded to Azure Blob Storage.

3. **Download Locally**  
   The image is retrieved on your local machine.

4. **Image Processing**  
   Using computer vision, the image is repositioned so the board appears normal and centered.

5. **Piece Detection**  
   A Roboflow object detection model identifies the piece types and their positions on the board.

6. **Calculate Best Move**  
   The Stockfish chess engine analyzes the board and determines the next best move.

7. **Send Move via Email**  
   The suggested move is emailed to the user. (Configure your email in a `secrets.json` file.)

8. **Conquer the Chess World**  
   Prepare to destroy Magnus Carlsen!

---

## Setup

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/checkmate-glasses.git
2. Download Python3.7 and install the associated pip3.7 with
   ```bash
   wget https://bootstrap.pypa.io/pip/3.7/get-pip.py
   python3.7 get-pip.py
3. Create a Python3.7 virtual environment
   ```bash
   python3.7 -m venv .python3-7venv
4. Install the requirements
   ```bash
   python3.7 -m pip install keras==2.3.1 tensorflow==1.15.5 scipy==1.4.1 pyclipper==1.2.1 numpy==1.18.5 matplotlib==3.2.2 h5py==2.10.0 tables==3.6.1 opencv-python==4.2.0.34 ipykernel protobuf==3.20.* scikit-learn==0.22.2
  and check it with
  ```bash
  pip freeze
