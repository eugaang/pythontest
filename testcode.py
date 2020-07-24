{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "df = pd.read_excel('/Users/yookangchoi/dev/python/files/kakao_chat2.xls')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20 entries, 0 to 19\n",
      "Data columns (total 3 columns):\n",
      " #   Column   Non-Null Count  Dtype         \n",
      "---  ------   --------------  -----         \n",
      " 0   Date     20 non-null     datetime64[ns]\n",
      " 1   User     20 non-null     object        \n",
      " 2   Message  19 non-null     object        \n",
      "dtypes: datetime64[ns](1), object(2)\n",
      "memory usage: 608.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
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
       "      <th>Date</th>\n",
       "      <th>User</th>\n",
       "      <th>Message</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2020-07-13 18:43:42</td>\n",
       "      <td>유깡</td>\n",
       "      <td>유깡님이 들어왔습니다.\\n운영정책을 위반한 메시지로 신고 접수 시 카카오톡 이용에 ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2020-07-13 18:44:09</td>\n",
       "      <td>영앤리코</td>\n",
       "      <td>영앤리코님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2020-07-13 18:46:20</td>\n",
       "      <td>로고디자인_드라포유</td>\n",
       "      <td>안녕하세요! 소통하는 로고디자인 드라포유 입니다.\\n \\n오래된 연장통에 따르면, ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2020-07-13 18:46:40</td>\n",
       "      <td>그즈리</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2020-07-13 18:46:51</td>\n",
       "      <td>panger</td>\n",
       "      <td>panger님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2020-07-13 18:47:00</td>\n",
       "      <td>겸손한 상어</td>\n",
       "      <td>겸손한 상어님이 나갔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2020-07-13 18:48:45</td>\n",
       "      <td>눙눙</td>\n",
       "      <td>눙눙님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2020-07-13 18:51:10</td>\n",
       "      <td>럭스고고</td>\n",
       "      <td>럭스고고님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2020-07-13 18:53:01</td>\n",
       "      <td>지아이</td>\n",
       "      <td>저도 블로그 게시글 투척합니다! 지금보니 쓴지 벌써 시간이 꽤 지났네요. 다들 독서...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2020-07-13 18:53:05</td>\n",
       "      <td>지아이</td>\n",
       "      <td>https://m.blog.naver.com/rkdsoddlv/221867413100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2020-07-13 18:53:35</td>\n",
       "      <td>지아이</td>\n",
       "      <td>삭제된 메시지입니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2020-07-13 18:53:35</td>\n",
       "      <td>501/민상현/혀니TV</td>\n",
       "      <td>30대 사업가 모임 ‘MARKETFUL’\\nhttps://open.kakao.com...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2020-07-13 18:53:40</td>\n",
       "      <td>김성욱</td>\n",
       "      <td>김성욱님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2020-07-13 18:53:53</td>\n",
       "      <td>김성욱</td>\n",
       "      <td>안녕하세요!</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2020-07-13 18:54:01</td>\n",
       "      <td>문성완</td>\n",
       "      <td>안녕하세요</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2020-07-13 18:55:02</td>\n",
       "      <td>sof</td>\n",
       "      <td>sof님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>2020-07-13 18:55:30</td>\n",
       "      <td>자피치</td>\n",
       "      <td>자피치님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>2020-07-13 18:55:40</td>\n",
       "      <td>후캔두댓 김아빠</td>\n",
       "      <td>와우 에이트</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>2020-07-13 18:56:59</td>\n",
       "      <td>난다요</td>\n",
       "      <td>난다요님이 들어왔습니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>2020-07-13 18:57:58</td>\n",
       "      <td>디노라디</td>\n",
       "      <td>40대도 가능할까요?</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Date          User  \\\n",
       "0  2020-07-13 18:43:42            유깡   \n",
       "1  2020-07-13 18:44:09          영앤리코   \n",
       "2  2020-07-13 18:46:20    로고디자인_드라포유   \n",
       "3  2020-07-13 18:46:40           그즈리   \n",
       "4  2020-07-13 18:46:51        panger   \n",
       "5  2020-07-13 18:47:00        겸손한 상어   \n",
       "6  2020-07-13 18:48:45            눙눙   \n",
       "7  2020-07-13 18:51:10          럭스고고   \n",
       "8  2020-07-13 18:53:01           지아이   \n",
       "9  2020-07-13 18:53:05           지아이   \n",
       "10 2020-07-13 18:53:35           지아이   \n",
       "11 2020-07-13 18:53:35  501/민상현/혀니TV   \n",
       "12 2020-07-13 18:53:40           김성욱   \n",
       "13 2020-07-13 18:53:53           김성욱   \n",
       "14 2020-07-13 18:54:01           문성완   \n",
       "15 2020-07-13 18:55:02           sof   \n",
       "16 2020-07-13 18:55:30           자피치   \n",
       "17 2020-07-13 18:55:40      후캔두댓 김아빠   \n",
       "18 2020-07-13 18:56:59           난다요   \n",
       "19 2020-07-13 18:57:58          디노라디   \n",
       "\n",
       "                                              Message  \n",
       "0   유깡님이 들어왔습니다.\\n운영정책을 위반한 메시지로 신고 접수 시 카카오톡 이용에 ...  \n",
       "1                                      영앤리코님이 들어왔습니다.  \n",
       "2   안녕하세요! 소통하는 로고디자인 드라포유 입니다.\\n \\n오래된 연장통에 따르면, ...  \n",
       "3                                                 NaN  \n",
       "4                                    panger님이 들어왔습니다.  \n",
       "5                                     겸손한 상어님이 나갔습니다.  \n",
       "6                                        눙눙님이 들어왔습니다.  \n",
       "7                                      럭스고고님이 들어왔습니다.  \n",
       "8   저도 블로그 게시글 투척합니다! 지금보니 쓴지 벌써 시간이 꽤 지났네요. 다들 독서...  \n",
       "9     https://m.blog.naver.com/rkdsoddlv/221867413100  \n",
       "10                                        삭제된 메시지입니다.  \n",
       "11  30대 사업가 모임 ‘MARKETFUL’\\nhttps://open.kakao.com...  \n",
       "12                                      김성욱님이 들어왔습니다.  \n",
       "13                                             안녕하세요!  \n",
       "14                                              안녕하세요  \n",
       "15                                      sof님이 들어왔습니다.  \n",
       "16                                      자피치님이 들어왔습니다.  \n",
       "17                                             와우 에이트  \n",
       "18                                      난다요님이 들어왔습니다.  \n",
       "19                                        40대도 가능할까요?  "
      ]
     },
     "execution_count": 211,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "print(len(df))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n"
     ]
    }
   ],
   "source": [
    "print(len(df))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[~df.Message.str.contains(\"나갔습니다\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[~df.Message.str.contains(\"들어왔습니다\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "print(len(df))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
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
       "      <th>Date</th>\n",
       "      <th>User</th>\n",
       "      <th>Message</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2020-07-13 18:46:20</td>\n",
       "      <td>로고디자인_드라포유</td>\n",
       "      <td>안녕하세요! 소통하는 로고디자인 드라포유 입니다.\\n \\n오래된 연장통에 따르면, ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2020-07-13 18:53:01</td>\n",
       "      <td>지아이</td>\n",
       "      <td>저도 블로그 게시글 투척합니다! 지금보니 쓴지 벌써 시간이 꽤 지났네요. 다들 독서...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2020-07-13 18:53:05</td>\n",
       "      <td>지아이</td>\n",
       "      <td>https://m.blog.naver.com/rkdsoddlv/221867413100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2020-07-13 18:53:35</td>\n",
       "      <td>지아이</td>\n",
       "      <td>삭제된 메시지입니다.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2020-07-13 18:53:35</td>\n",
       "      <td>501/민상현/혀니TV</td>\n",
       "      <td>30대 사업가 모임 ‘MARKETFUL’\\nhttps://open.kakao.com...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2020-07-13 18:53:53</td>\n",
       "      <td>김성욱</td>\n",
       "      <td>안녕하세요!</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2020-07-13 18:54:01</td>\n",
       "      <td>문성완</td>\n",
       "      <td>안녕하세요</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>2020-07-13 18:55:40</td>\n",
       "      <td>후캔두댓 김아빠</td>\n",
       "      <td>와우 에이트</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>2020-07-13 18:57:58</td>\n",
       "      <td>디노라디</td>\n",
       "      <td>40대도 가능할까요?</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Date          User  \\\n",
       "2  2020-07-13 18:46:20    로고디자인_드라포유   \n",
       "8  2020-07-13 18:53:01           지아이   \n",
       "9  2020-07-13 18:53:05           지아이   \n",
       "10 2020-07-13 18:53:35           지아이   \n",
       "11 2020-07-13 18:53:35  501/민상현/혀니TV   \n",
       "13 2020-07-13 18:53:53           김성욱   \n",
       "14 2020-07-13 18:54:01           문성완   \n",
       "17 2020-07-13 18:55:40      후캔두댓 김아빠   \n",
       "19 2020-07-13 18:57:58          디노라디   \n",
       "\n",
       "                                              Message  \n",
       "2   안녕하세요! 소통하는 로고디자인 드라포유 입니다.\\n \\n오래된 연장통에 따르면, ...  \n",
       "8   저도 블로그 게시글 투척합니다! 지금보니 쓴지 벌써 시간이 꽤 지났네요. 다들 독서...  \n",
       "9     https://m.blog.naver.com/rkdsoddlv/221867413100  \n",
       "10                                        삭제된 메시지입니다.  \n",
       "11  30대 사업가 모임 ‘MARKETFUL’\\nhttps://open.kakao.com...  \n",
       "13                                             안녕하세요!  \n",
       "14                                              안녕하세요  \n",
       "17                                             와우 에이트  \n",
       "19                                        40대도 가능할까요?  "
      ]
     },
     "execution_count": 218,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(20)"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
