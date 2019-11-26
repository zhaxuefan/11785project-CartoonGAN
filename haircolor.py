import os
import shutil
import pandas as pd


def sortHairColor(path):
    blonde_hair = []
    black_hair = []
    brown_hair = []
    grey_hair = []
    orange_hair = []

    for f in os.listdir(path):

        if '.png' in f:
            continue

        if '_' in f:
            continue

        table = pd.read_csv(os.path.join(path, f), header=None,
                            index_col=0, sep=',')

        if 'hair_color' not in table.index:
            continue

        if table.loc['hair_color', 1] in [0, 1, 4]:
            blonde_hair.append(f[:-4])

        elif table.loc['hair_color', 1] in [5, 6]:
            brown_hair.append(f[:-4])

        elif table.loc['hair_color', 1] == 7:
            black_hair.append(f[:-4])

        elif table.loc['hair_color', 1] in [8, 9]:
            grey_hair.append(f[:-4])

        else:
            orange_hair.append(f[:-4])

    return blonde_hair, black_hair, brown_hair, grey_hair, orange_hair


def copyFilestoFolder(filelist, folders):

    if os.path.isdir(folders) is False:
        os.mkdir(folders)

    for counter, p in enumerate(filelist, 1):
        pic = './cartoonset10k/{}.png'.format(p)
        csv = './cartoonset10k/{}.csv'.format(p)
        shutil.copy(pic, folders)
        shutil.copy(csv, folders)
        if counter % 100 == 0:
            print("{}/{}".format(counter, len(filelist)))


if __name__ == "__main__":
    blonde_hair, black_hair, brown_hair, grey_hair, orange_hair = sortHairColor(
           './cartoonset10k/')
    copyFilestoFolder(blonde_hair, './blonde_hair/')
    copyFilestoFolder(black_hair, './black_hair/')
    copyFilestoFolder(brown_hair, './brown_hair/')
    copyFilestoFolder(grey_hair, './grey_hair/')
    copyFilestoFolder(orange_hair, './orange_hair/')
