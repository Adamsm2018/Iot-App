# Mike Adams
# IoT App Layer Project
# 'example_resource.py'
# Class referenced by main.py for server functions
# Coapthon3 library used. Documentation and examples referenced. https://github.com/Tanganelli/CoAPthon

from coapthon.resources.resource import Resource

class BasicResource(Resource):                  # Class to represent topic
    def __init__(self, name="Temperature", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "25c"        # Readout set to 25c

    def render_GET(self, request):      
        return self

    def render_PUT(self, request):  # From example, unused
        self.payload = request.payload
        return self

    def render_POST(self, request): # From example, unused
        res = BasicResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):   # From example, unused
        return True
