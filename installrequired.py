import os

requiredmodules: list = ["requests", "discord"]

for x in requiredmodules:
    print(f"/n Now installing required module: {x}")
    os.system(f"pip install {x}")

import main