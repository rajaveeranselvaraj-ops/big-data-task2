# Weather Count Using MapReduce

## Project Description
This project demonstrates a simple MapReduce program in Python to count the occurrences of weather conditions from an input file.

## Files Included

- `input.txt` – Contains the weather data.
- `mapper.py` – Reads each weather condition and outputs `(weather, 1)`.
- `partitioner.py` – Passes the mapper output to the reducer.
- `reducer.py` – Counts the total occurrences of each weather condition.
- `main.py` – Executes the mapper, sorts the intermediate output, and runs the reducer.
- `README.md` – Project documentation.

## Input

```
Sunny
Rainy
Sunny
Cloudy
Rainy
Sunny
```

## Expected Output

```
Cloudy    1
Rainy     2
Sunny     3
```

## Requirements

- Python 3.x

## Project Structure

```
WeatherCount/
│── input.txt
│── mapper.py
│── partitioner.py
│── reducer.py
│── main.py
│── README.md
```

## How to Run

Open the terminal in the project folder and run:

```bash
python main.py
```

## How It Works

1. **Mapper**
   - Reads each line from `input.txt`.
   - Outputs the weather condition with a value of `1`.

2. **Partitioner**
   - Passes the mapper output to the reducer.

3. **Reducer**
   - Groups the same weather conditions.
   - Adds their counts.
   - Displays the final result.

## Sample Output

```
Cloudy    1
Rainy     2
Sunny     3
```

## Author

**Name:** ______________________

**Register Number:** ______________________

**Course:** Big Data Analytics

**Department:** ______________________
