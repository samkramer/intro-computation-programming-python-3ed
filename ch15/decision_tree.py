# 15.2 Dynamic Programming and the 0/1 Knapsack Problem
import random
import string


# Code from Figure 14-2
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
        
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight
    
    def __str__(self):
        result = ('<' + self.name + ', ' + str(self.value)
                 + ', ' + str(self.weight) + '>')
        return result

# Glboal variable used for debugging
g_to_print = False

def print_result(result_tuple, label):
    val = result_tuple[0]
    items = result_tuple[1]
    
    items_str = "[]"
    if items:
        items_str_list = []
        for item in items:
            items_str_list.append(str(item))
        items_str = ", ".join(items_str_list)
        items_str = f"[{items_str}]"
        
    result = f"(val={val}, items={items_str})"
    print(f"[INFO] {label:<30} {result}")

# Figure 15-5 on page 313  
# Using a decision tree to solve a knapsack problem
def max_val(to_consider, avail):
    """Assumes to_consider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if g_to_print:
        print_result((avail, to_consider), "Input")
    
    if not to_consider:
        result = (0, ())
        if g_to_print:
            print_result(result, "to_consider == []")
    elif avail == 0:
        result = (0, ())
        if g_to_print:
            print_result(result, "avail == 0")
    elif to_consider[0].get_weight() > avail:
        # Explore right branch only
        if g_to_print:
            print("[INFO] Explore right branch only")
        result = max_val(to_consider[1:], avail)
        if g_to_print:
            print_result(result, "Explore right branch only")
    else:
        next_item = to_consider[0]
        
        # Explore left branch
        if g_to_print:
            print("[INFO] Explore left branch")
        with_val, with_to_take = max_val(to_consider[1:],
                                         avail - next_item.get_weight())
        if g_to_print:
            print_result((with_val, with_to_take), "Explore left branch")
        with_val += next_item.get_value()
        
        # Explore right branch
        if g_to_print:
            print("[INFO] Explore right branch")
        without_val, without_to_take = max_val(to_consider[1:], avail)
        if g_to_print:
            print_result((without_val, without_to_take), "Explore right branch")
        
        # Choose better branch
        if with_val > without_val:
            if g_to_print:
                print("[INFO] with_val > without_val")
            result = (with_val, with_to_take + (next_item,))
            if g_to_print:
                print_result(result, "with_val > without_val")
        else:
            if g_to_print:
                print("[INFO] with_val < without_val")
            result = (without_val, without_to_take)
            if g_to_print:
                print_result(result, "with_val < without_val")
    
    return result


def print_items(items):
    print('Items:')
    for item in items:
        print(item)
    print()

    
def print_items_taken(items_taken, total_val):
    print()
    print('Items Taken:')
    for item in items_taken:
        print(item)
    print()
    print('Total value of items taken =', total_val)

        
# Figure 15-6 on page 314
def small_test():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    print_items(Items)
    
    global g_to_print
    g_to_print = True
        
    val, taken = max_val(Items, 5)
    print_items_taken(taken, val)


def build_many_items(num_items, max_val, max_weight):
    letters = string.ascii_lowercase
    items = []
    for i in range(num_items):
        items.append(Item(letters[i],
                          random.randint(1, max_val),
                          random.randint(1, max_weight)))
    return items


def big_test(num_items, avail_weight):
    items = build_many_items(num_items, 10, 10)
    print_items(items)
    
    val, taken = max_val(items, avail_weight)
    print_items_taken(taken, val)
    
    
if __name__ == "__main__":
    small_test()
    # big_test(10, 40)
