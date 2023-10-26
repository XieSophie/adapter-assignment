# Task Adapter Assignment
The Task Adapter is required to wrap around a dummy "model" script [`dummy_model.py`](dummy_model.py). 


## Dummy Model 
The dummy model is a simple python script that outputs the sum of two values found in a given csv file.

The two values are chosen based on parameters `a` and `b` provided by the user, where the first value is found in `a`th row `b`th column, and the second value `b`th row `a`th column.

### Usage
```
python dummy_model.py parameter_a parameter_b data.csv
```

It takes in three arguments:
- value of parameter `a`
- value of parameter `b`
- location of csv file

### Dependencies
The script requires the python dependency `pandas`.


## Adapter Requirements
We should be able to run [`install.sh`](install.sh) to install the model and [`execute.sh`](execute.sh) to run it with the required inputs. 

The expected inputs files would be a `parameter.json` and a `data.csv`.  
- `parameter.json` contains two properties `a` and `b`.
- `data.csv` contains a table of values and can be of any size.

The sample inputs to the script can be found [here](test_inputs).

The expected output file `result.json` should be created if it is ran successfully. It should contain a **numerical** property `result`.

e.g.
```json
{
    "result": 1.234
}
```

You are expected to handle any possible errors in the Adapter. Any errors encountered should produce a `result.json`, with a negative result and a human readable reason that describes the error.

e.g.
```json
{
    "result": -1,
    "error": "Model encountered error: ..."
}
```

The logic for the Adapter should be written in the [`processor.py`](processor.py) file provided.


Wherever required, `data_type` and `configuration` or other names can be any appropriate string defined by you.
