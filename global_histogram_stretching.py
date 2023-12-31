{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a937c931",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def histogram_r(r_array,height, width):\n",
    "    length = height * width\n",
    "    R_rray = []\n",
    "    for i in range(height):\n",
    "        for j in range(width):\n",
    "            R_rray.append(r_array[i][j])\n",
    "    R_rray.sort()\n",
    "    I_min = int(R_rray[int(length / 500)])\n",
    "    I_max = int(R_rray[-int(length / 500)])\n",
    "    array_Global_histogram_stretching = np.zeros((height, width))\n",
    "    for i in range(0, height):\n",
    "        for j in range(0, width):\n",
    "            if r_array[i][j] < I_min:\n",
    "                # p_out = r_array[i][j]\n",
    "                array_Global_histogram_stretching[i][j] = I_min\n",
    "            elif (r_array[i][j] > I_max):\n",
    "                p_out = r_array[i][j]\n",
    "                array_Global_histogram_stretching[i][j] = 255\n",
    "            else:\n",
    "                p_out = int((r_array[i][j] - I_min) * ((255 - I_min) / (I_max - I_min)))+ I_min\n",
    "                array_Global_histogram_stretching[i][j] = p_out\n",
    "    return (array_Global_histogram_stretching)\n",
    "\n",
    "def histogram_g(r_array,height, width):\n",
    "    length = height * width\n",
    "    R_rray = []\n",
    "    for i in range(height):\n",
    "        for j in range(width):\n",
    "            R_rray.append(r_array[i][j])\n",
    "    R_rray.sort()\n",
    "    I_min = int(R_rray[int(length / 500)])\n",
    "    I_max = int(R_rray[-int(length / 500)])\n",
    "    array_Global_histogram_stretching = np.zeros((height, width))\n",
    "    for i in range(0, height):\n",
    "        for j in range(0, width):\n",
    "            if r_array[i][j] < I_min:\n",
    "                p_out = r_array[i][j]\n",
    "                array_Global_histogram_stretching[i][j] = 0\n",
    "            elif (r_array[i][j] > I_max):\n",
    "                p_out = r_array[i][j]\n",
    "                array_Global_histogram_stretching[i][j] = 255\n",
    "            else:\n",
    "                p_out = int((r_array[i][j] - I_min) * ((255) / (I_max - I_min)) )\n",
    "                array_Global_histogram_stretching[i][j] = p_out\n",
    "    return (array_Global_histogram_stretching)\n",
    "\n",
    "def histogram_b(r_array,height, width):\n",
    "    length = height * width\n",
    "    R_rray = []\n",
    "    for i in range(height):\n",
    "        for j in range(width):\n",
    "            R_rray.append(r_array[i][j])\n",
    "    R_rray.sort()\n",
    "    I_min = int(R_rray[int(length / 500)])\n",
    "    I_max = int(R_rray[-int(length / 500)])\n",
    "    array_Global_histogram_stretching = np.zeros((height, width))\n",
    "    for i in range(0, height):\n",
    "        for j in range(0, width):\n",
    "            if r_array[i][j] < I_min:\n",
    "                # p_out = r_array[i][j]\n",
    "                array_Global_histogram_stretching[i][j] = 0\n",
    "            elif (r_array[i][j] > I_max):\n",
    "                # p_out = r_array[i][j]\n",
    "                array_Global_histogram_stretching[i][j] = I_max\n",
    "            else:\n",
    "                p_out = int((r_array[i][j] - I_min) * ((I_max) / (I_max - I_min)))\n",
    "                array_Global_histogram_stretching[i][j] = p_out\n",
    "    return (array_Global_histogram_stretching)\n",
    "\n",
    "def stretching(img):\n",
    "    height = len(img)\n",
    "    width = len(img[0])\n",
    "    img[:, :, 2] = histogram_r(img[:, :, 2], height, width)\n",
    "    img[:, :, 1] = histogram_g(img[:, :, 1], height, width)\n",
    "    img[:, :, 0] = histogram_b(img[:, :, 0], height, width)\n",
    "    return img\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68d1ee37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
