# 13.1 Plotting Using Matplotlib
import matplotlib.pyplot as plt

# Code from page 261
principal = 10000 # initial investment
interest_rate = 0.05
years = 20

values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interest_rate


# plt.plot(values, 'bo') # plot using blue circle markers, no line
plt.plot(values, color='blue', marker='o')

plt.title('5% Growth, Compounded Annually',
          fontsize='x-large')
plt.xlabel('Years of Compounding', fontsize='small')
plt.ylabel('Value of Principal ($)', fontsize='medium')