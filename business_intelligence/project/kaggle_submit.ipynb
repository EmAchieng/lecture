{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Kaggle 후기\n",
    "   - Two Sigma Connect: Rental Listing Inquiries\n",
    "   - 목적 : 집의 특성을 가지고 입주자의 만족도 조사(Multiclassification problem ex) high ,medium ,low)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 데이터 종류\n",
    "\n",
    "   - bathrooms\n",
    "   - bedrooms\n",
    "   - building_id\n",
    "   - created\n",
    "   - description\n",
    "   - display_address\n",
    "   - features\n",
    "   - latitude\n",
    "   - listing_id\n",
    "   - longitude\n",
    "   - manager_id\n",
    "   - photos\n",
    "   - price\n",
    "   - street_address\n",
    "   - interest_level"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feature Engineering"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.base_feature(A)\n",
    " - 경도를 가지고 Feature를 생성함\n",
    " - 가격을 13000 기준으로 생성함\n",
    " - 가격을 log함수로 생성함\n",
    " - 침실과 화장실을 더해 총 방의 개수를 생성함\n",
    " - 평당 가격을 생성함\n",
    " - 집의 특징을 단어의 갯수로 생성함\n",
    " - 생성일시를 년도, 월, 날짜, 시간에 맞추어 생성함\n",
    " - manager_id를 통한 만족도를 예측함 (경험기반으로 한 방식)\n",
    " - Feature를 가지고 CountVectorizer를 생성하여 위의 Feature 병합"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.base_feature(B)\n",
    " - base_feature(A) + 알파\n",
    " - 알파 : 사진부분의 생성날짜 (월, 주, 일, 시간, 등)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3.base_feature(C)\n",
    " - base_feature(A) + 베타\n",
    " - 베타 : 구글의 s2sphere라는 프로그램"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Model"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. xgboost\n",
    "2. ensemble\n",
    "   - AdaBoostClassifier\n",
    "   - KNeighborsClassifier\n",
    "   - GradientBoostingClassifier\n",
    "   - RandomForestClassifier\n",
    "   - ExtraTreesClassifier"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Oversampling\n",
    " - 데이터의 비율을 똑같게 3063개로 1:1:1로 9189개 실험\n",
    " - 데이터의 비율 제시한 그대로 유지"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 실험결과"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature - A - XGboost_No_Oversampling  \n",
    "     - Accuracy = 0.76"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|                     | <h1>       0        </h1>    | <h1>       1        </h1>     | <h1>      2   </h1>  | <h1> avg / total </h1>|    \n",
    "| :------------:      | :--------------------------: |  :--------------------------: |  :--------------------------: |  :-------------: | \n",
    "|   <h1>precision</h1>| <h1>  0.60   </h1>           |  <h1>  0.52   </h1>           |  <h1>  0.83   </h1>           |  <h1>  0.74  </h1>|   \n",
    "|   <h1>recall   </h1>| <h1>  0.34   </h1>           |  <h1>  0.44   </h1>           | <h1>  0.92  </h1>           |  <h1>  0.76   </h1>| \n",
    "|   <h1>f1-score </h1>| <h1>  0.43   </h1>           |  <h1>  0.47   </h1>           | <h1>  0.87   </h1>           | <h1>  0.75   </h1>| \n",
    "|   <h1>support  </h1>| <h1>  776    </h1>           |  <h1>  2229   </h1>           | <h1>  6866    </h1>           | <h1>  9871   </h1>| "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature - B - Ensemble_No_Oversampling  \n",
    "     - Accuracy = 0.73"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|                     | <h1>       0        </h1>    | <h1>       1        </h1>     | <h1>      2   </h1>  | <h1> avg / total </h1>|    \n",
    "| :------------:      | :--------------------------: |  :--------------------------: |  :--------------------------: |  :-------------: | \n",
    "|   <h1>precision</h1>| <h1>  0.29   </h1>           |  <h1>  0.55   </h1>           |  <h1>  0.84   </h1>           |  <h1>  0.73  </h1>|   \n",
    "|   <h1>recall   </h1>| <h1>  0.54   </h1>           |  <h1>  0.26   </h1>           | <h1>  0.90  </h1>           |  <h1>  0.73   </h1>| \n",
    "|   <h1>f1-score </h1>| <h1>  0.38   </h1>           |  <h1>  0.35   </h1>           | <h1>  0.87   </h1>           | <h1>  0.71   </h1>| \n",
    "|   <h1>support  </h1>| <h1>  776    </h1>           |  <h1>  2229   </h1>           | <h1>  6866    </h1>           | <h1>  9871   </h1>| "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature - B - XGboost_No_Oversampling  \n",
    "     - Accuracy = 0.77"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|                     | <h1>       0        </h1>    | <h1>       1        </h1>     | <h1>      2   </h1>  | <h1> avg / total </h1>|    \n",
    "| :------------:      | :--------------------------: |  :--------------------------: |  :--------------------------: |  :-------------: | \n",
    "|   <h1>precision</h1>| <h1>  0.61   </h1>           |  <h1>  0.54   </h1>           |  <h1>  0.84   </h1>           |  <h1>  0.76  </h1>|   \n",
    "|   <h1>recall   </h1>| <h1>  0.33   </h1>           |  <h1>  0.47   </h1>           | <h1>  0.92  </h1>           |  <h1>  0.77   </h1>| \n",
    "|   <h1>f1-score </h1>| <h1>  0.43   </h1>           |  <h1>  0.50   </h1>           | <h1>  0.88   </h1>           | <h1>  0.76   </h1>| \n",
    "|   <h1>support  </h1>| <h1>  776    </h1>           |  <h1>  2229   </h1>           | <h1>  6866    </h1>           | <h1>  9871   </h1>| "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature - C - Ensemble_Yes_Oversampling  \n",
    "     - Accuracy = 0.56"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|                     | <h1>       0        </h1>    | <h1>       1        </h1>     | <h1>      2   </h1>  | <h1> avg / total </h1>|    \n",
    "| :------------:      | :--------------------------: |  :--------------------------: |  :--------------------------: |  :-------------: | \n",
    "|   <h1>precision</h1>| <h1>  0.16   </h1>           |  <h1>  0.45   </h1>           |  <h1>  0.95   </h1>           |  <h1>  0.77  </h1>|   \n",
    "|   <h1>recall   </h1>| <h1>  0.81   </h1>           |  <h1>  0.31   </h1>           | <h1>  0.61  </h1>           |  <h1>  0.56   </h1>| \n",
    "|   <h1>f1-score </h1>| <h1>  0.27   </h1>           |  <h1>  0.61   </h1>           | <h1>  0.74   </h1>           | <h1>  0.62   </h1>| \n",
    "|   <h1>support  </h1>| <h1>  776    </h1>           |  <h1>  2229   </h1>           | <h1>  6866    </h1>           | <h1>  9871   </h1>| "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature - C - XGboost_Yes_Oversampling  \n",
    "     - Accuracy = 0.68"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|                     | <h1>       0        </h1>    | <h1>       1        </h1>     | <h1>      2   </h1>  | <h1> avg / total </h1>|    \n",
    "| :------------:      | :--------------------------: |  :--------------------------: |  :--------------------------: |  :-------------: | \n",
    "|   <h1>precision</h1>| <h1>  0.36   </h1>           |  <h1>  0.41   </h1>           |  <h1>  0.92   </h1>           |  <h1>  0.76  </h1>|   \n",
    "|   <h1>recall   </h1>| <h1>  0.68   </h1>           |  <h1>  0.54   </h1>           | <h1>  0.73 </h1>           |  <h1>  0.69   </h1>| \n",
    "|   <h1>f1-score </h1>| <h1>  0.47   </h1>           |  <h1>  0.47   </h1>           | <h1>  0.82   </h1>           | <h1>  0.71   </h1>| \n",
    "|   <h1>support  </h1>| <h1>  776    </h1>           |  <h1>  2229   </h1>           | <h1>  6866    </h1>           | <h1>  9871   </h1>| "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature - C - Ensemble_No_Oversampling  \n",
    "     - Accuracy = 0.73"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|                     | <h1>       0        </h1>    | <h1>       1        </h1>     | <h1>      2   </h1>  | <h1> avg / total </h1>|    \n",
    "| :------------:      | :--------------------------: |  :--------------------------: |  :--------------------------: |  :-------------: | \n",
    "|   <h1>precision</h1>| <h1>  0.32   </h1>           |  <h1>  0.56   </h1>           |  <h1>  0.82   </h1>           |  <h1>  0.72  </h1>|   \n",
    "|   <h1>recall   </h1>| <h1>  0.45   </h1>           |  <h1>  0.26   </h1>           | <h1>  0.92 </h1>           |  <h1>  0.73   </h1>| \n",
    "|   <h1>f1-score </h1>| <h1>  0.37   </h1>           |  <h1>  0.36   </h1>           | <h1>  0.87   </h1>           | <h1>  0.71   </h1>| \n",
    "|   <h1>support  </h1>| <h1>  776    </h1>           |  <h1>  2229   </h1>           | <h1>  6866    </h1>           | <h1>  9871   </h1>| "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Feature - C - XGboost_No_Oversampling  \n",
    "     - Accuracy = 0.77"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|                     | <h1>       0        </h1>    | <h1>       1        </h1>     | <h1>      2   </h1>  | <h1> avg / total </h1>|    \n",
    "| :------------:      | :--------------------------: |  :--------------------------: |  :--------------------------: |  :-------------: | \n",
    "|   <h1>precision</h1>| <h1>  0.62   </h1>           |  <h1>  0.53   </h1>           |  <h1>  0.84   </h1>           |  <h1>  0.75  </h1>|   \n",
    "|   <h1>recall   </h1>| <h1>  0.35   </h1>           |  <h1>  0.46   </h1>           | <h1>  0.92 </h1>           |  <h1>  0.77   </h1>| \n",
    "|   <h1>f1-score </h1>| <h1>  0.45   </h1>           |  <h1>  0.49   </h1>           | <h1>  0.88   </h1>           | <h1>  0.76   </h1>| \n",
    "|   <h1>support  </h1>| <h1>  776    </h1>           |  <h1>  2229   </h1>           | <h1>  6866    </h1>           | <h1>  9871   </h1>| "
   ]
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
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
