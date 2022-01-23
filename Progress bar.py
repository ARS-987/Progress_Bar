from cgitb import text
from tqdm import tqdm
from time import sleep
for char in tqdm(range(100), colour="RED", ncols=50):
    sleep(0.25)

from cgitb import text
from tqdm import tqdm
from time import sleep
text = ""
for char in tqdm(["we ","iove ","learnpy ", "<3"]):
    sleep(0.25)
    text = text + char
    print(text)