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
2. Set up an Azure Blob Storage account
3. Set up a secrets.json with your email and an app password for your email. An example of this file is:
   ```json
   {
    "AZURE_STORAGE_CONNECTION_STRING": "<your-connection-string>",
    "USER_EMAIL": "<your-email>",
    "USER_PASSWORD": "<your-email-password>"
   }
4. Download Python3.7 and install the associated pip3.7 with
   ```bash
   wget https://bootstrap.pypa.io/pip/3.7/get-pip.py
   python3.7 get-pip.py
5. Create a Python3.7 virtual environment
   ```bash
   python3.7 -m venv .python3-7venv
6. Install the requirements
   ```bash
   pip install keras==2.3.1 tensorflow==1.15.5 scipy==1.4.1 pyclipper==1.2.1 numpy==1.18.5 matplotlib==3.2.2 h5py==2.10.0 tables==3.6.1 opencv-python==4.2.0.34 ipykernel protobuf==3.20.* scikit-learn==0.22.2
7. Download Python3.11 and install the associated pip3.11 with
   ```bash
   wget https://bootstrap.pypa.io/pip/3.11/get-pip.py
   python3.11 get-pip.py
8. Create a Python3.11 virtual environment
   ```bash
   python3.11 -m venv .python3-11venv
9. Install the requirements
   ```bash
   pip install azure-functions inference-sdk pillow
10. Open a terminal and activate the python3.7 environment
    ```bash
    source ./.python3-7venv/bin/activate
11. Run the board detection script from here
    ```bash
    python3 board_detection_FULL.py
12. Open a terminal and activate the python3.11 environment
    ```bash
    source ./.python3-11venv/bin/activate
13. Run the piece detection script from here
    ```bash
    python3 piece_detection_FULL.py
14. Open a terminal and activate the python3.11 environment
    ```bash
    source ./.python3-11venv/bin/activate
15. Run the Azure blob trigger from here
    ```bash
    func start
16. Open a terminal and activate the python3.11 environment
    ```bash
    source ./.python3-11venv/bin/activate
17. Run the binary to jpg converter here
    ```bash
    python3 bin2jpg.py
18. If you want, you can test sending images to Azure Blob Storage
   ```bash
   python3 send_blob.py

---

## Questions and Bugs
make an issue!
