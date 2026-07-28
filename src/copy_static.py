import os
import shutil

def copy_static(src, dst):
    # 1. If dst exists, delete it
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # 2. Create dst
    os.mkdir(dst)
    # 3. Loop over everything in src:
    for item_name in os.listdir(src):
        item_fullpath = os.path.join(src, item_name)
        # - if it's a file, copy it to dst 
        if os.path.isfile(item_fullpath):
            shutil.copy(item_fullpath, dst)
        # - if it's a directory, recurse 
    #    - when you recurse into a subdirectory, the destination should be the corresponding subdirectory in dst
        elif os.path.isdir(item_fullpath):
            sub_dst = os.path.join(dst, item_name)
            copy_static(item_fullpath, sub_dst)