# 16.2 The Drunkard's Walk

import random
import math
import matplotlib.pyplot as plt

# # Figure 16-2 from page 326
class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self._x, self._y = x, y
        
    def move(self, delta_x, delta_y):
        """delta_x and delta_y are numbers"""
        return Location(self._x + delta_x, self._y + delta_y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def dist_from(self, other):
        ox, oy = other._x, other._y
        x_dist, y_dist = self._x - ox, self._y - oy
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return f'<{self._x}, {self._y}>'


class Field(object):
    def __init__(self):
        self._drunks = {}   # {drunk : location}
        
    def add_drunk(self, drunk, loc):
        if drunk in self._drunks:
            raise ValueError('Duplicate drunk')
        else:
            self._drunks[drunk] = loc
            
    def move_drunk(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self._drunks[drunk]
        # Use move method of Location to get new location
        self._drunks[drunk] = current_location.move(x_dist, y_dist)
        
    def get_loc(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        return self._drunks[drunk]


# # Figure 16-3 from page 327        
class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self._name = name

    def __str__(self):
        if self != None:
            return self._name
        return 'Anonymous'


class Usual_drunk(Drunk):
    def take_step(self):
        step_choices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(step_choices)


def test_Usual_drunk():
    drunk = Usual_drunk()
    for i in range(10):
        choice = drunk.take_step()
        print(choice)


# # Figure 16-4 from page 328  
def walk(f, d, num_steps):
    """Assumes: f a Field, d a Drunk in f, and num_steps an int >= 0.
       Moves d num_steps times; returns the distance between the
       final location and the location at the start of the  walk."""
    start = f.get_loc(d)    # (0, 0)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


# sim_walks with correction described on page 329
def sim_walks(num_steps, num_trials, d_class):
    """Assumes num_steps an int >= 0, num_trials an int > 0,
          d_class a subclass of Drunk
        Simulates num_trials walks of num_steps steps each.
        Returns a list of the final distances for each trial"""
    drunk = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        field = Field()
        field.add_drunk(drunk, origin)
        distances.append(round(walk(field, drunk, num_steps), 1))
    return distances


def drunk_test(walk_lengths, num_trials, d_class):
    """Assumes walk_lengths a sequence of ints >= 0
         num_trials an int > 0, d_class a subclass of Drunk
       For each number of steps in walk_lengths, runs sim_walks with
         num_trials walks and prints results"""
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'walk of', num_steps, 'steps: Mean =',
              f'{sum(distances)/len(distances):.3f}, Max =',
              f'{max(distances)}, Min = {min(distances)}')
        

# Finger exercise: write code to produce plot in Figure 16-5
def plot_mean_distance(walk_lengths, num_trials, d_class):
    mean_distances = []
    sqrt_steps = []
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        mean_dist = sum(distances) / len(distances)
        mean_distances.append(mean_dist)
        sqrt_step = math.sqrt(num_steps)
        sqrt_steps.append(sqrt_step)

    plt.plot(walk_lengths, mean_distances, 'r', label = d_class.__name__)
    plt.plot(walk_lengths, sqrt_steps, 'b', label = 'sqrt(steps)', linestyle='--')
    plt.legend(loc="upper left")
    plt.xlabel('Number of Steps', fontsize = 'large')
    plt.ylabel('Distance from Origin', fontsize = 'large')
    plt.title(f"Mean Distance from Origin ({num_trials} trials)")
    plt.xscale('log')
    plt.yscale('log')


if __name__ == "__main__":
    random.seed(0)
    
    # test_Usual_drunk()
    
    # drunk_test((0,1), 100, Usual_drunk)
    # drunk_test((10, 100, 1000, 10000), 100, Usual_drunk)
    
    plot_mean_distance((10, 100, 1000, 10000), 100, Usual_drunk)
