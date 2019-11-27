import os
import shutil
import pandas as pd


def sortHairColor(attrtxt):
    blonde_hair = []
    black_hair = []
    brown_hair = []
    grey_hair = []

    table = pd.read_csv(attrtxt, index_col=0, delim_whitespace=True)

    # create ~10k dataset
    for i in range(10500):
        if table.loc[i, 'Black_Hair'] == 1:
            black_hair.append(table.loc[i, 'filename'])

        elif table.loc[i, 'Blond_Hair'] == 1:
            blonde_hair.append(table.loc[i, 'filename'])

        elif table.loc[i, 'Brown_Hair'] == 1:
            brown_hair.append(table.loc[i, 'filename'])

        elif table.loc[i, 'Gray_Hair'] == 1:
            grey_hair.append(table.loc[i, 'filename'])

    return blonde_hair, black_hair, brown_hair, grey_hair


def copyFilestoFolder(filelist, folders):

    if os.path.isdir(folders) is False:
        os.mkdir(folders)

    for counter, p in enumerate(filelist, 1):
        pic = p
        shutil.copy(pic, folders)
        if counter % 100 == 0:
            print("{}/{}".format(counter, len(filelist)))


if __name__ == "__main__":
    blonde_hair, black_hair, brown_hair, grey_hair = sortHairColor(
           './img_align_celeba_png')
    copyFilestoFolder(blonde_hair, './blonde_hair/')
    copyFilestoFolder(black_hair, './black_hair/')
    copyFilestoFolder(brown_hair, './brown_hair/')
    copyFilestoFolder(grey_hair, './grey_hair/')
