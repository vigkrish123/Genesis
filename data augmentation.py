{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.preprocessing.image import ImageDataGenerator\n",
    "from keras.preprocessing.image import array_to_img\n",
    "from keras.preprocessing.image import img_to_array\n",
    "from keras.preprocessing.image import load_img\n",
    "\n",
    "datagen = ImageDataGenerator(\n",
    "    rotation_range=40,\n",
    "    width_shift_range=0.2,\n",
    "    horizontal_flip=False,\n",
    "    shear_range=0.2,\n",
    "    zoom_range=0.2,\n",
    "    height_shift_range=0.2)\n",
    "\n",
    "img = load_img('F:\\AVML Proj\\Traffic timer images\\TL 2\\TL 200001.png')\n",
    "x = img_to_array(img)\n",
    "x = x.reshape((1,) + x.shape)\n",
    "\n",
    "i = 0\n",
    "for batch in datagen.flow(x, batch_size=1, save_to_dir ='F:\\AVML Proj\\Traffic timer images\\TL 2\\Augmented TL 2'):\n",
    "    i += 1\n",
    "    if i > 10:\n",
    "        break   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:proj] *",
   "language": "python",
   "name": "conda-env-proj-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
