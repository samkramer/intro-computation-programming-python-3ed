# 13.2 Plotting Mortgages, an Extended Example
import matplotlib.pyplot as plt
import numpy as np

def find_payment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at a monthly rate of r for m months"""
    return loan * ((r * (1+r)**m) / ( (1+r)**m - 1) )

# Figure 13-7 from page 264    
class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        self._loan = loan
        self._rate = annRate / 12.0
        self._months = months
        self._paid = [0.0] 
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = None #description of mortgage
        
    def make_payment(self):
        self._paid.append(self._payment)
        reduction = self._payment - (self._outstanding[-1] * self._rate)
        self._outstanding.append(self._outstanding[-1] - reduction)
        
    def get_total_paid(self):
        return sum(self._paid)
    
    def __str__(self):
        return self._legend

    def plot_payments(self, style):
        plt.plot(self._paid[1:], style, label = self._legend)
    
    def plot_balance(self, style):
        plt.plot(self._outstanding, style, label = self._legend)

    def plot_tot_pd(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        plt.plot(tot_pd, style, label = self._legend)

    def plot_net(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        equity_acquired = np.array([self._loan]*len(self._outstanding))
        equity_acquired = equity_acquired-np.array(self._outstanding)
        net = np.array(tot_pd) - equity_acquired
        plt.plot(net, style, label = self._legend)
        
        
# Code from Figure 13-8 on page 267
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self._legend = f'Fixed, {r*100:.1f}%'
        
class Fixed_with_pts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self._pts = pts
        self._paid = [loan*(pts/100)]
        self._legend = f'Fixed, {r*100:.1f}%, {pts} points'

class Two_rate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._teaser_rate = teaser_rate
        self._nextRate = r/12
        self._legend = (f'{100*teaser_rate:.1f}% for ' +
                f'{self._teaser_months} months, then {100*r:.1f}%')
        
    def make_payment(self):
        if len(self._paid) == self._teaser_months + 1:
            self._rate = self._nextRate
            self._payment = find_payment(self._outstanding[-1],
                                self._rate,
                                self._months - self._teaser_months)
        Mortgage.make_payment(self)


# Code from Figure 13-9 on page 268
def compare_mortgages(amt, years, fixed_rate, pts, pts_rate,
                      var_rate1, var_rate2, var_months):
    tot_months = years * 12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = Fixed_with_pts(amt, pts_rate, tot_months, pts)
    two_rate = Two_rate(amt, var_rate2, tot_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    plot_mortgages(morts, amt)


# Code from Figure 13-10 on page 269    
def plot_mortgages(morts, amt):
    def label_plot(figure, title, x_label, y_label):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc = 'best')
        
    styles = ['k-', 'k-.', 'k:']
    
    # Give names to figure numbers
    payments, cost, balance, net_cost = 0, 1, 2, 3
    
    for i in range(len(morts)):
        plt.figure(payments)
        morts[i].plot_payments(styles[i])
        plt.figure(cost)
        morts[i].plot_tot_pd(styles[i])
        plt.figure(balance)
        morts[i].plot_balance(styles[i])
        plt.figure(net_cost)
        morts[i].plot_net(styles[i])
        
    label_plot(payments, f'Monthly Payments of ${amt:,} Mortages',
               'Months', 'Monthly Payments')
    label_plot(cost, f'Cash Outlay of ${amt:,} Mortgages',
               'Months', 'Total Payments')
    label_plot(balance, f'Balance Remaining of ${amt:,} Mortages',
               'Months', 'Remaining Loan Balance of $')
    label_plot(net_cost, f'Net Cost of ${amt:,} Mortgages',
              'Months', 'Payments - Equity $')

if __name__ == "__main__":
    # Code from page 268
    compare_mortgages(amt=200000, years=30, fixed_rate=0.07,
                      pts = 3.25, pts_rate=0.05, var_rate1=0.045,
                      var_rate2=0.095, var_months=48)
    
    