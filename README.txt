README - 2024-04-21

*****************************************
main.py
*****************************************
Region 1
********
This is concerned with the parameter tuning process. Here ranges of parameters and increments are set up and fed into a purpose built tuning class.

Output: A console log containing the best performing parameters.

To run: Un-comment the desired algorithm tuning process and set up parameter numbers. Then run main.py.

Region 2
********
This is a test region, where an algorithm can be ran once, in isolation, with given parameters.

Output: A console log containing the result.

To run: Un-comment the desired algorithm and enter parameters in the run function. Then run main.py.

Region 3
********
This is The experiment. Each algorithm is set up, with parameters (in a separate array) that should come from parameter tuning. These are passed to the experiment class which runs all algorithms, 100 times, with the given parameters.

Output: A csv file with the number of evaluations taken to find a good soluiton (0 is good enough solution not found).

To run: Un-comment the region and enter parameters into the correct array. Then run main.py.



*****************************************
analysis.py
*****************************************
Gets the success rate, average evaluations, min evaluations, max evaluations, standard deviation and variance of a given csv file, with 1 column.

Output: A console log of the analysis.

To run: Edit ALGORITHM_NAME to the name of the algorithm's csv file (must be in root directory of the program). Then run analysis.py



*****************************************
t_test.py
*****************************************
Performs a statistical t-test on the data from 2 different algorithms.

Output: A console log of the algorithm comparison.

To run: Enter name of first csv into csv1 anf name of second in csv2. Run t_test.py.