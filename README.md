# DUCT Programming Assignment 
## Introduction
This assignment introduces the concept of Adapters that we use in DUCT to accomplish the Federation of Models.  
Creating and maintaining of Adapters would be one of the responsibilities of this role.

## Task
We have included a short primer of how Adapters work below to help you with this task. 

Based on your understanding of Adapters, created an Adapter based on the [requirements](task-adapter/README.md) found in `task-adapter`. We have provided you with the general structure of the Adapter in `task-adapter`.

Once you are done, submit your Adapter as a PR to this repository.

## Primer for Adapters
Adapters provide a wrapper interface around a computational model (it could be an application or a even simple script) with a clearly defined specification of inputs/outputs and instructions on how to install/execute it.

### Adapter Structure
A valid Adapter follows a similar folder structure and contain these types of files as shown below:

```
adapter/
├── descriptor.json
├── execute.sh
├── install.sh
├── adapter_script
```

#### Adapter Descriptor (descriptor.json)
An Adapter Descriptor specifies the name, input/output interfaces and configurations of an Adapter.

It is in the form of a JSON file and is structured as follows:

```
{
  "name": ...,
  "input": [
    ...
  ],
  "output": [
    ...
  ],
  "configurations": [
    ...
  ]
}
```

The input/output properties are lists of items that specify the input data consumed and output data produced by the Adapter, respectively. This information is used before and after job execution to verify that the correct data objects are submitted and created.

Structure of Input/Output Item:
```
{
  "name": ...,
  "data_type": ...,
  "data_format": ...
}
```

An item has a name, a data type and data format. `data_type` is a user-defined string and provides the context of how the data is used (e.g. AHProfile is for anthropogenic heat profile). `data_format` is how the data is formatted/encoded (e.g. csv).

The configurations property is a list of user defined strings that describes the runtime configurations supported by this adapter (e.g. "windows", "ubuntu-22.04").

Example of descriptor.json
```json
{
  "name": "test-proc",
  "input": [
    {
      "name": "a",
      "data_type": "JSONObject",
      "data_format": "json"
    },
    {
      "name": "b",
      "data_type": "AHProfile",
      "data_format": "csv"
    }
  ],
  "output": [
    {
      "name": "c",
      "data_type": "JSONObject",
      "data_format": "json"
    }
  ],
  "configurations": [
    "default", 
    "nscc"
  ]
}
```

#### Install Script (install.sh)
The Install script specifies how to set up the proper environment for the adapter. This could include installing software, compiling binaries and downloading external dependencies.

When the script is executed, an argument (a string referencing a valid configuration) is passed to the script which specifies how the adapter should be deployed.

Example of execution
```bash
install.sh default 
```

Example of install.sh
```bash
#!/bin/bash

if [ "$1" == "default" ]; then
    echo "Run default configuration"
  python3 -m pip install -r ./requirements.txt
    exit 0

elif [ "$1" == "nscc" ]; then
    echo "Run nscc configuration"
  python3 -m pip install -r ./requirements.txt
    exit 0

else
    exit 1
fi
```

#### Execute Script (execute.sh)
The Execution script specifies how the adapter should run a given job during the execution stage.

When the script is executed, it is passed two arguments. First, the configuration of the adapter (the same value passed to the install.sh script) and second, the path to the working directory. The working directory is where the inputs files the job needs will be found and where output files of the job should be written to.

Example of execution
```bash
execute.sh default ./working_directory
```

Example of execute.sh
```bash
#!/bin/bash 

if [ "$1" == "default" ]; then
    echo "Run processor.py with default configuration on $2"
    python3 processor.py $2

elif [ "$1" == "nscc" ]; then
    echo "Run processor.py with nscc configuration on $2"
    python3 processor.py $2

else
    exit 1
fi
```

#### Adapter Script (adapter_script)
The Adapter Script is where most of the execution logic is written. This is usually written as a python script named `processor.py`

Example of processor.py
```python
import sys

def function(working_directory: str) -> None:
    return working_directory

if __name__ == "__main__":
    function(sys.argv[1])
```
