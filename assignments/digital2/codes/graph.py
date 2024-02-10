import matplotlib.pyplot as plt

def generate_data(n_values):
    return [4 * n * (n + 1) for n in n_values]

def stem_plot(n_values, data_values):
    plt.stem(n_values, data_values, linefmt='b-',markerfmt='bo',basefmt='r-',use_line_collection=True)
    plt.stem(n_values[19], data_values[19], linefmt='g-',markerfmt='go',basefmt='r-')
    
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.savefig('digi-graph.png')
    plt.show()
    plt.grid('True')

def main():
    # Choose a range of n values
    n_values = list(range(1, 21))  # You can adjust the range as needed

    # Generate data for the chosen n values
    data_values = generate_data(n_values)
    
    # Plot the stem graph
    stem_plot(n_values, data_values)



if __name__ == "__main__":
    main()
