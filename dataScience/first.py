{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>Clump_Thickness</th>\n",
       "      <th>Cell_Size_Uniformity</th>\n",
       "      <th>Cell_Shape_Uniformity</th>\n",
       "      <th>Marginal_Adhesion</th>\n",
       "      <th>Single_Epithelial_Cell_Size</th>\n",
       "      <th>Bare_Nuclei</th>\n",
       "      <th>Bland_Chromatin</th>\n",
       "      <th>Normal_Nucleoli</th>\n",
       "      <th>Mitoses</th>\n",
       "      <th>Cancer_Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1000025</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1002945</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1015425</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1016277</td>\n",
       "      <td>6</td>\n",
       "      <td>8</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1017023</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        ID  Clump_Thickness  Cell_Size_Uniformity  Cell_Shape_Uniformity  \\\n",
       "0  1000025                5                     1                      1   \n",
       "1  1002945                5                     4                      4   \n",
       "2  1015425                3                     1                      1   \n",
       "3  1016277                6                     8                      8   \n",
       "4  1017023                4                     1                      1   \n",
       "\n",
       "   Marginal_Adhesion  Single_Epithelial_Cell_Size Bare_Nuclei  \\\n",
       "0                  1                          2.0           1   \n",
       "1                  5                          NaN          10   \n",
       "2                  1                          2.0           2   \n",
       "3                  1                          3.0           4   \n",
       "4                  3                          2.0           1   \n",
       "\n",
       "   Bland_Chromatin  Normal_Nucleoli  Mitoses  Cancer_Type  \n",
       "0                3                1        1            2  \n",
       "1                3                2        1            2  \n",
       "2                3                1        1            2  \n",
       "3                3                7        1            2  \n",
       "4                3                1        1            2  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(699, 11)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
