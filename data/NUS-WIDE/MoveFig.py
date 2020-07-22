import os
import shutil

for dir_name in os.listdir("../Flickr"):
    dir_path = os.path.join("../Flickr", dir_name)
    for fig_name in os.listdir(dir_path):
        fig_path = os.path.join(dir_path, fig_name)
        dest_path = os.path.join("./images", fig_name)
        if os.path.exists(dest_path) == False:
            shutil.move(fig_path, "./images")
            print(fig_path + ": done!")
