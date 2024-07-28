# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:46:13 2024

@author: alhe551
"""

import os
from glob import glob
from PIL import Image

print(f"\nRunning {os.path.basename(__file__)} ...")

DIR = r"C:\Users\alhe551\OneDrive - The University of Auckland\Documents\PhD\Writting\Photos\Ecotaxa"
# trgt_width, trgt_height = 180, 0

#%%
def trgt_size(img_width, img_height, trgt_width, trgt_height):
    if trgt_width == 0:
        res_width, res_height = (
            round(img_width * (trgt_height / img_height)),
            trgt_height,
        )
    elif trgt_height == 0:
        res_width, res_height = trgt_width, round(img_height * (trgt_width / img_width))
    return (res_width, res_height)


#%%
for file in glob(os.path.join(DIR, "*.jpg")):
    with Image.open(file) as img:
        img.thumbnail(trgt_size(img.width, img.height, 0, 180))
        img.save(file.replace(".jpg", "_180hgt.jpg"))
#%% END
print(f"\nEnd of the program {os.path.basename(__file__)}", "\a")
