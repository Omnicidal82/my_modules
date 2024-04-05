from pathlib import Path

import json

import inspect


def save_variable(data, var_name='save'):
    """
    Saves a single variable to a .json file.

    Args:
        data: The variable to be saved.
        var_name (str, optional): The name of the variable. Defaults to 'save'.

    Example:
        save_variable(var_name)
        save_variable(var_name, 'var_name')
    """
    
    path = Path(f'save_data/{var_name}_data.json')
    
    path.write_text(json.dumps(data))
    
    
def load_variable(var_name='save'):
    """
    Loads a single variable from a .json file.

    Args:
        var_name (str, optional): The name of the variable. Defaults to 'save'.

    Returns:
        The loaded variable, or None if the file was not found.

    Example:
        For a variable saved without a name, use load_variable()
        For a variable saved with a name, use load_variable('var_name')
    """
    
    path = Path(f'save_data/{var_name}_data.json')
    
    try:
        data = json.loads(path.read_text())
        
    except FileNotFoundError:
        print(f"File '{path}' not found!")
        
        return None
    
    else:              
        return data


def save_variables(*data):
    """
    Saves multiple variables to a single .json file.

    Args:
        *data: The variables to be saved.
    """
    
    data_list = []
    
    path = Path('save_data.json')      
   
    # Get the local variables in the caller's scope
    local_vars = inspect.currentframe().f_back.f_locals.items()
    
    # Filter the local variables to only include the ones in args
    data = {k: v for k, v in local_vars if v in data}
    
    for key, value in data.items():
        data_list.append({key: value})
        
    path.write_text(json.dumps(data_list))
    

def load_variables():
    """
    Loads variables from a .json file and returns them as a dictionary.

    Returns:
        A dictionary where the keys are the variable names and the values are 
        the variable values.

    Example:
        To reinitialize the stored data, use:

        variables = load_variables()

        for key, value in variables.items():
            globals()[key] = value
    """
    
    data_list = {}    
    path = Path('save_data.json')    
    try:
        # Load the data from the JSON file
        data_list = json.loads(path.read_text())    
    except FileNotFoundError:
        print(f"File '{path}' not found!")    
    else:
        # Re-initialize the variables
        print("Reloading variables")
        return {key: value for data in data_list for key, value in data.items()}