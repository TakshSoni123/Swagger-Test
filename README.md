# Swagger-Test

There are two methods of creating swagger api docs in this repo.

## First method : Creating openAPI spec file manually with apispec
Steps:
- Run openAPISpecGenerator-self.py
    This will update the static/openAPI.json file with the spec details mentioned in our code. 
- Run swagger-ui.py
    This will automatically start the swagger api docs which can be accessed at http://127.0.0.1:5000/api/docs/
    
The openAPI.json file created can be directly used to import all APIs in postman using the steps mentioned in 
https://learning.postman.com/docs/integrations/available-integrations/working-with-openAPI/


## Second method : Using pydantic plugin to create and run swagger
Steps:
- Run openAPIWithPydantic.py
    This will start flask app on http://127.0.0.1:5000/

This python file automatically creates a flask app and uses pydantic plugin to create openAPI spec file and create swagger api docs ui.
You can access the openAPI.json file at http://127.0.0.1:5000/apidoc/openapi.json (Which can be used to import APIs in postman)
You can access the swagger api docs at http://127.0.0.1:5000/apidoc/swagger

Here, the docs are hosted with our flask app. If we need it to be hosted on a different server, we can use the openAPI.json url with the swagger-ui.py file in the first method to host.
