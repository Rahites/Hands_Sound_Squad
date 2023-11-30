## Hand_Sound_Squad_UI

0. Make folder
- tts/ : tts file save path  
- weight/ : your own weight (which has an architecture in "predict_coordinate.py")  
- npy_file/ : your won word npy  
- tts/ : tts file save path 

1. Env setting
- Window 10
- python 3.10
- `pip install -r requirements.txt`

2. Execution
- `python main.py`

3. To Make '.exe' File
- `pip install pyinstaller`
- `pyinstaller main.py --copy-metadata tqdm --copy-metadata regex --copy-metadata requests --copy-metadata packaging --copy-metadata filelock --copy-metadata numpy --copy-metadata tokenizers --copy-metadata huggingface-hub --copy-metadata safetensors --copy-metadata pyyaml --copy-metadata torch`