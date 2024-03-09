COMPARE_FUNCTIONS = {
    "a == b": lambda a, b: a == b,
    "a != b": lambda a, b: a != b,
    "a < b": lambda a, b: a < b,
    "a > b": lambda a, b: a > b,
    "a <= b": lambda a, b: a <= b,
    "a >= b": lambda a, b: a >= b,
}


class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return True
    
class ForceAlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return True


class String:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("STRING", {"default": ""})},
        }

    RETURN_TYPES = ("STRING",)

    RETURN_NAMES = ("STRING",)

    FUNCTION = "execute"

    CATEGORY = "Logic"

    def execute(self, value):
        return (value,)


class Int:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("INT", {"default": 0})},
        }

    RETURN_TYPES = ("INT",)

    RETURN_NAMES = ("INT",)

    FUNCTION = "execute"

    CATEGORY = "meshmesh"

    def execute(self, value):
        return (value,)


class Float:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("FLOAT", {"default": 0, "step": 0.01})},
        }

    RETURN_TYPES = ("FLOAT",)

    RETURN_NAMES = ("FLOAT",)

    FUNCTION = "execute"

    CATEGORY = "meshmesh"

    def execute(self, value):
        return (value,)


class Bool:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"value": ("BOOLEAN", {"default": False})},
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = ("BOOLEAN",)

    FUNCTION = "execute"

    CATEGORY = "meshmesh"

    def execute(self, value):
        return (value,)


class Compare:
    """
    This nodes compares the two inputs and outputs the result of the comparison.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Comparison node takes two inputs, a and b, and compares them.
        """
        s.compare_functions = list(COMPARE_FUNCTIONS.keys())
        return {
            "required": {
                "a": (ForceAlwaysEqualProxy("*"), {"default": 0}),
                "b": (ForceAlwaysEqualProxy("*"), {"default": 0}),
                "comparison": (s.compare_functions, {"default": "a == b"}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)

    RETURN_NAMES = "BOOLEAN"

    FUNCTION = "compare"

    CATEGORY = "meshmesh"

    def compare(self, a, b, comparison):
        """
        Compare two inputs and return the result of the comparison.

        Args:
            a (UNKNOWN): The first input.
            b (UNKNOWN): The second input.
            comparison (STRING): The comparison to perform. Can be one of "==", "!=", "<", ">", "<=", ">=".

        Returns:
            : The result of the comparison.
        """
        return (COMPARE_FUNCTIONS[comparison](a, b),)


class IfExecute:
    """
    This node executes IF_TRUE if ANY is True, otherwise it executes IF_FALSE.

    ANY can be any input, IF_TRUE and IF_FALSE can be any output.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ANY": (ForceAlwaysEqualProxy("*"),),
                "IF_TRUE": (ForceAlwaysEqualProxy("*"),),
                "IF_FALSE": (ForceAlwaysEqualProxy("*"),),
            },
        }

    RETURN_TYPES = (ForceAlwaysEqualProxy("*"),)

    RETURN_NAMES = "?"

    FUNCTION = "return_based_on_bool"

    CATEGORY = "meshmesh"

    def return_based_on_bool(self, ANY, IF_TRUE, IF_FALSE):
        return (IF_TRUE if ANY else IF_FALSE,)
    

class IfExecuteImage:
    """
    This node executes IF_TRUE if ANY is True, otherwise it executes IF_FALSE.

    ANY can be any input, IF_TRUE and IF_FALSE can be any output.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ANY": (ForceAlwaysEqualProxy("*"),),
                "IF_TRUE": (ForceAlwaysEqualProxy("*"),),
                "IF_FALSE": (ForceAlwaysEqualProxy("*"),),
            },
        }

    RETURN_TYPES = ("IMAGE",)

    RETURN_NAMES = "?"

    FUNCTION = "return_based_on_bool"

    CATEGORY = "meshmesh"

    def return_based_on_bool(self, ANY, IF_TRUE, IF_FALSE):
        return (IF_TRUE if ANY else IF_FALSE,)


class DebugPrint:
    """
    This node prints the input to the console.
    """

    @classmethod
    def INPUT_TYPES(s):
        """
        Takes in any input.

        """
        return {"required": {"ANY": (ForceAlwaysEqualProxy({}),)}}

    RETURN_TYPES = ()

    OUTPUT_NODE = True

    FUNCTION = "log_input"

    CATEGORY = "meshmesh"

    def log_input(self, ANY):
        print(ANY)
        return {}


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Compare": Compare,
    "Int": Int,
    "Float": Float,
    "Bool": Bool,
    "String": String,
    "If ANY execute A else B": IfExecute,
    "DebugPrint": DebugPrint,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Compare": "Compare",
    "Int": "Int",
    "Float": "Float",
    "Bool": "Bool",
    "String": "String",
    "If ANY execute A else B": "If",
    "DebugPrint": "DebugPrint",
}
