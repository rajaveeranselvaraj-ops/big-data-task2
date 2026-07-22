MapReduce Word Count using Python
Project Title

MapReduce Word Count Implementation in Python

Project Overview

This project demonstrates a simple implementation of the MapReduce programming model using Python. It counts the number of occurrences of each word (or weather condition) in an input file.

The project simulates the four stages of Hadoop MapReduce:

Mapping
Partitioning
Sorting (performed in main.py)
Reducing

The input contains weather conditions:

Sunny
Rainy
Sunny
Cloudy
Rainy
Sunny

The program outputs the frequency of each weather condition.

Example Output

Cloudy  1
Rainy   2
Sunny   3
Project Structure
MapReduce_Project/
│
├── input.txt
├── mapper.py
├── partitioner.py
├── reducer.py
├── main.py
└── README.md
File Description
1. input.txt

Purpose:

Contains the input data that will be processed.

Content:

Sunny
Rainy
Sunny
Cloudy
Rainy
Sunny

Each line represents one record.

2. mapper.py

Purpose:

The Mapper reads each line from the input file and converts it into a key-value pair.

Example:

Input

Sunny
Rainy
Sunny

Mapper Output

Sunny   1
Rainy   1
Sunny   1

Working

Reads data line by line
Removes extra spaces
Emits
word    1

for every record.

3. partitioner.py

Purpose:

The partitioner receives mapper output and forwards the key-value pairs.

In Hadoop, the partitioner sends keys to different reducers.

In this project, it simply passes the data without changing it.

Example

Input

Sunny   1
Rainy   1

Output

Sunny   1
Rainy   1
4. reducer.py

Purpose:

The Reducer receives sorted key-value pairs and counts the occurrences of each key.

Example

Input

Cloudy 1
Rainy 1
Rainy 1
Sunny 1
Sunny 1
Sunny 1

Output

Cloudy 1
Rainy 2
Sunny 3

Working

Reads sorted input
Groups identical keys
Adds their counts
Prints the final frequency
5. main.py

Purpose

Acts as the driver program.

Responsibilities

Reads input.txt
Executes mapper.py
Collects mapper output
Sorts the intermediate data
Sends sorted data to reducer.py
Displays the final output

Flow

Input File
     │
     ▼
 Mapper
     │
     ▼
Intermediate Output
     │
     ▼
Sorting
     │
     ▼
Reducer
     │
     ▼
Final Result
Algorithm
Step 1

Read the input file.

Step 2

Run the mapper.

Step 3

Generate

word    1

for every line.

Step 4

Sort all key-value pairs.

Step 5

Send sorted data to reducer.

Step 6

Reducer groups identical keys.

Step 7

Reducer counts total occurrences.

Step 8

Display the final frequency of each word.

Sample Execution

Input

Sunny
Rainy
Sunny
Cloudy
Rainy
Sunny

Mapper Output

Sunny   1
Rainy   1
Sunny   1
Cloudy  1
Rainy   1
Sunny   1

Sorted Output

Cloudy  1
Rainy   1
Rainy   1
Sunny   1
Sunny   1
Sunny   1

Reducer Output

Cloudy  1
Rainy   2
Sunny   3
Software Requirements
Python 3.x
Command Prompt / Terminal
No external libraries required
How to Run

Place all files in the same folder.

Run:

python main.py

Expected Output

Cloudy  1
Rainy   2
Sunny   3
MapReduce Workflow
              input.txt
                  │
                  ▼
             mapper.py
                  │
                  ▼
      Intermediate Key-Value Pairs
                  │
                  ▼
        Sorting (main.py)
                  │
                  ▼
            reducer.py
                  │
                  ▼
            Final Output
Time Complexity
Stage	Complexity
Mapping	O(n)
Sorting	O(n log n)
Reducing	O(n)
Overall	O(n log n)
Advantages
Easy to understand MapReduce concepts.
Demonstrates the Mapper and Reducer workflow.
Uses only standard Python libraries.
Can be extended for larger datasets.
Simulates Hadoop MapReduce processing.
Limitations
Runs on a single machine.
Does not provide true distributed processing.
Partitioner only forwards data and does not distribute keys across multiple reducers.
Suitable only for learning and demonstration purposes.
Conclusion

This project successfully demonstrates the MapReduce Word Count algorithm in Python. The Mapper transforms input records into key-value pairs, the data is sorted, and the Reducer aggregates the counts to produce the final frequency of each unique word. Although it is a simplified implementation without Hadoop, it clearly illustrates the core concepts of the MapReduce programming model and serves as a solid foundation for understanding distributed data processing.
