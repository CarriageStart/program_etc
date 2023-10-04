import matplotlib.pyplot as plt
import seaborn as sns

year = [2018, 2019, 2020, 2021, 2022, 2023]
python = [5.8, 8.17, 9.31, 11.87, 15.63, 14.51]
C = [13.59, 14.08, 16.72, 14.32, 12.71, 14.73]
java = [15.78, 15.04, 16.73, 11.23, 10.82, 13.23]
JS = [3.49, 2.51, 2.38, 2.44, 2.12, 2.1]


fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)  # 1행 2열의 서브플롯을 생성합니다.

sns.lineplot(x=year, y=python, label="python", ax=ax1)  # seaborn을 이용해 그래프 그리기
sns.lineplot(x=year, y=java, label="java", ax=ax2)  # seaborn을 이용해 그래프 그리기
plt.show()
