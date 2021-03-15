# 13.1 Plotting Using Matplotlib
import matplotlib.pyplot as plt

# Code from page 259
plt.figure(1) # create figure 1
plt.plot([1,2,3,4], [1,2,3,4]) # draw on figure 1

plt.figure(2) # create figure 2
plt.plot([1,4,2,3], [5,6,7,8]) # draw on figure 2
plt.savefig('Figure-Addie') # save figure 2

plt.figure(1) # go back to working on figure 1
plt.plot([5,6,10,3]) # draw again on figure 1
plt.savefig('Figure-Jane') # save figure 1
