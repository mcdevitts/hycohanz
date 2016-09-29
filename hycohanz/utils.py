from __future__ import division, print_function, unicode_literals, absolute_import

import warnings
from hycohanz.expression import Expression as Ex

warnings.simplefilter('default')


def collect_parameters_and_attributes(parameters, attributes, parametersName):
    """Collects the the variables and reorders them into the proper format that HFSS' COM interface is expecting.

    :arg parameters
    :arg attributes
    :arg parametersName

    """
    #
    parameterList = ["NAME:{0}".format(parametersName)]
    for k,v in parameters.items():

        # If the variable is an HFSS Expression, convert it to its string form
        if isinstance(v, Ex):
            v = v.expr
        elif not isinstance(v, float) and not isinstance(v, str) and not isinstance(v, int) and not isinstance(v, bool):
            continue
        else:
            pass

        # Change all keys to be of the form:
        #   'My Key:='
        # Append the := and replace any underscores with spaces
        parameterList.extend(['{0}:='.format(k.replace('_', ' ')), v])

    attributeList = ['NAME:Attributes']
    try:
        [attributeList.extend(['{0}:='.format(k), v]) for k, v in attributes.items()]
    except AttributeError:
        attributeList = []

    return parameterList, attributeList


def hfss_com_wrapper(comObj, parameters, attributes, parametersName, functionName):
    """

    :param com_obj:
    :param parameters:
    :param attributes:
    :param parametersName:
    :param functionName:
    :return:
    """
    parameters, attributes = collect_parameters_and_attributes(parameters, attributes, parametersName)
    if attributes:
        return getattr(comObj, functionName)(parameters, attributes)
    else:
        return getattr(comObj, functionName)(parameters)