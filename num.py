{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7ed2d9ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([1,2,3,4,5])\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8b646151",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4 5]\n",
      " [2 2 2 2 2]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([[1,2,3,4,5],[2,2,2,2,2]])\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "852aefcd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([[1,2,3,4,5],[7,6,5,1,9]])\n",
    "print(arr[0,-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "11575f62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 5)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([[1,2,3,4,5],[7,6,5,1,9]])\n",
    "print(arr.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3f681e5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "7\n",
      "6\n",
      "5\n",
      "1\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([[1,2,3,4,5],[7,6,5,1,9]])\n",
    "for x in arr:\n",
    "    for y in x:\n",
    "        print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8496c7cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([1,2,3,4,5])\n",
    "for x in arr:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c92324d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 5 6 7 0 8]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr1=np.array([1,2,3,4,5])\n",
    "arr2=np.array([5,6,7,0,8])\n",
    "arr3=np.concatenate((arr1,arr2))\n",
    "print(arr3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "3161c20d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4 5 1 2 3 4 5]\n",
      " [7 6 5 1 9 4 3 2 1 0]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr1=np.array([[1,2,3,4,5],[7,6,5,1,9]])\n",
    "arr2=np.array([[1,2,3,4,5],[4,3,2,1,0]])\n",
    "arr3=np.concatenate((arr1,arr2),axis=1)\n",
    "print(arr3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "30d6bfdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4 5]\n",
      " [0 1 2 3 8]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr1=np.array([[1,2,3,4,5],[3,1,8,2,0]])\n",
    "arr3=np.sort(arr1)\n",
    "print(arr3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "176021e7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
