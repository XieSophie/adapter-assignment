import sys
import json
import os
import dummy_model

class ErrorHandler(Exception):
    pass

def get_descriptors(working_directory):
    """
    Access all of the name, input/output interfaces and configurations from the descriptor given by the json file name.
    """
    descriptor_file_path = os.path.realpath(working_directory) + '/descriptor.json'
    
    try:
        with open (descriptor_file_path, 'r') as j:
            source = json.loads(j.read())
        return dict(
            inputs = source["input"],
            output = source["output"],
            config = source["configurations"],
        )
    
    except IOError as e:
        error_string = "Counld not process the descriptor file: " + descriptor_file_path
        raise ErrorHandler(error_string)

    except KeyError as e:
        error_string = "Missing descriptor definition for: " + str(e)
        raise ErrorHandler(error_string)


def get_inputs(descriptors, working_directory):
    """
    Get the inputs from the descriptor, including parameters and data.
    """
    error_string = None
    input_path = os.path.realpath(working_directory) + '/test_inputs/'

    try:
        if (len(descriptors["inputs"]) != 2):
            error_string = "Missing input information from descriptor!"
            raise ErrorHandler(error_string)
        
        for input in descriptors["inputs"]:
            if input["name"] == "parameters":
                parameters_path = input_path + input["name"] + '.' + input["data_format"]
                if (os.path.isfile(parameters_path) == False):
                    error_string = "Could not find the parameter file: " + parameters_path
                    raise ErrorHandler(error_string)
                if (os.path.getsize(parameters_path) == 0):
                    error_string = "The parameter input file is empty: " + parameters_path
                    raise ErrorHandler(error_string)
                with open (parameters_path, 'r') as pp:
                    parameters = json.loads(pp.read())

            if input["name"] == "data":
                data_path = input_path + input["name"] + '.' + input["data_format"]
                if (os.path.isfile(data_path) == False):
                    error_string = "Could not find the data file: " + data_path
                    raise ErrorHandler(error_string)
                if (os.path.getsize(data_path) == 0):
                    error_string = "The data input file is empty: " + data_path
                    raise ErrorHandler(error_string)

        return dict(
            a = parameters["a"],
            b = parameters["b"],
            data_csv_path = data_path
        )
    
    except IOError as e:
        error_string = "Could not process the input file: " + parameters_path
        raise ErrorHandler(error_string)

    except KeyError as e:
        error_string = "Missing input definition for: " + str(e)
        raise ErrorHandler(error_string)

def get_output(descriptors, working_directory):
    """
    Get the output from the descriptor, including name and data_format.
    """

    if (len(descriptors["output"]) == 0):
        error_string = "Missing output information from descriptor!"
        raise ErrorHandler(error_string)
    
    for output in descriptors["output"]:
        if output["name"] == "result":
            result_path = os.path.realpath(working_directory) + '/' + output["name"] + '.' + output["data_format"]
            return result_path


def function(working_directory: str) -> None:
    
    error_result_path =  os.path.realpath(working_directory) + '/result.json'

    try:
        # Access the information in the descriptor
        descriptors = get_descriptors(working_directory)
        # Get the parameters from the inputs
        parameters = get_inputs(descriptors, working_directory)
        # Get the output path from the outputs
        result_path = get_output(descriptors, working_directory)
        # Use the dummy model script
        final = dummy_model.main(parameters["a"], parameters["b"], parameters["data_csv_path"])

        with open(result_path, 'w') as result_file:
            result_dict = {"result": final}
            json.dump(result_dict, result_file)   

    except ErrorHandler as e:
        result_dict = {"result": -1, "error": str(e)}
        with open(error_result_path, 'w') as result_file:
            json.dump(result_dict, result_file)    



if __name__ == "__main__":
    function(sys.argv[1])
