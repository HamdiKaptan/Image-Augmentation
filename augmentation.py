import os,shutil
from keras_preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
for i in (os.listdir("path")):
    dosya, uzantı = os.path.splitext('{}'.format(i))
    split = dosya.split("_")
    if int(split[1])%15 == 0 :
        img = load_img('path/{}.jpg'.format(dosya))
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)
        a=0
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir='/path/', save_prefix='{}'.format(dosya), save_format='jpg'):
            a += 1
            if a > 5:
                break
mid = 1
oid =1
os.chdir("/path/")
for i in os.listdir("/path/"):
    file, uzantı = os.path.splitext('{}'.format(i))

    if file[0] == "M" :
        file = 'M_' + str(mid) + ''
        mid += 1
        os.replace(i, file + uzantı)

    else:
        file = 'O_' + str(oid) + ''
        oid += 1
        os.rename(i, file + uzantı)
