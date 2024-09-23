# Technologies used

## Python
### Version 3.11.3
### pip version 24.2

# Instructions

First, install the dependencies using pip and requirements file:

```pip install -r requirements.txt```

To run each script, simply navigate to the project source folder and input the command: 

```python3 src/step_{step number}.py```

The reports will then be generated in the "results" directory as .csv files related to each step.

For testing, run the following command:
```pytest```

The test coverage will be produced and placed in the "htmlcov" directory, and can be accessed by opening index.html