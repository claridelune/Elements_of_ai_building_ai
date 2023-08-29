import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def load_data(data_str):
    """Load data from string and separate it into features and target variables."""
    data = np.genfromtxt(StringIO(data_str), skip_header=1)
    X = data[:, :-1]
    y = data[:, -1]
    return X, y

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function
    train_X, train_y = load_data(train_string)
    test_X, test_y = load_data(test_string)                                        #save the dependent variable in the test data to test_y
    c = np.linalg.lstsq(train_X, train_y)[0]                          #get least square coefficients from the test data
    print(c)                                                          #print the coefficients
    print(test_X @ c)                                                 #apply the coefficients to the test data and print it

main()
