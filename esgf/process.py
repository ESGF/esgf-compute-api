"""
Process Module.
"""

from esgf import parameter

class Process(parameter.Parameter):
    def __init__(self, process, name=None):
        super(Process, self).__init__(name)

        self.__process = process
        self.__response = None
        self.__inputs = None
        self.__params = None

    def __getattr__(self, name):
        if hasattr(self.__process, name):
            return getattr(self.__process, name)

        if hasattr(self.__response, name):
            return getattr(self.__response, name)

        raise AttributeError(name)

    def __set_inputs(self, inputs):
        self.__inputs = [x.name for x in inputs]

    inputs = property(None, __set_inputs)

    def __set_parameters(self, params):
        self.__params = [x.parameterize() for x in params]

    parameters = property(None, __set_parameters)

    def __set_response(self, response):
        self.__response = response

    response = property(None, __set_response)

    def parameterize(self):
        params = {
                'name': self.__process.identifier,
                'input': self.__inputs,
                'result': self.name
                }

        for p in self.__params:
            params.update(p)

        return params
