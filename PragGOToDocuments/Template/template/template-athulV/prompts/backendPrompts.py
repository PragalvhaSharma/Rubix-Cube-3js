databaseSchemaMaker = """

        ***Business Problem***:
        {business_problem}

        ***PageByPage Plan***:
        {overallPlan}

        ***Tech Stack***:
        Django

        You are an expert in Django and web development. You are making a backend structure for an ERP system based on the business problem described. 
        
        1. Please design a database model for the ERP system, including the entities, their attributes, and the relationships between them. 
        2. Ensure that the model supports scalability and maintains data integrity.
        3. DO NOT WRITE CODE YET. ENSURE THAT YOUR DESIGN IS THOUGHTFUL
        4. ENSURE the plan is production ready and scalable. 
        5. ENSURE the models you create adhere to the PageByPage Plan. 
        6. CREATE APPROPRIATE NUMBER OF TABLES  TO ENSURE THE SYSTEM WORKS PERFECTLY.

        
        ***GIVE ME THE OUTPUT IN THE FOLLOWING FORMAT BELOW***:

        ### Entities and Relationships
            **Table Name : [Table Name]**
                **Attributes**:
                    [List attributes here]
                **Relationships To other tables**:
                    [List relationships here]

"""


backendLogicPlanner = """
        **Business Problem and Requirements**:
        {business_problem}

        ***Frontend PageByPage Plan***:
        {overallPlan}

        ***Database Schema***:
        {databaseSchema}

        ***Tech Stack***:
        Django REST Framework and PostgreSQL

        You are an expert in Django and web development. You are currently working on a project that requires you to create a backend structure for an ERP system.

        1. Given the information above, I need you to generate a backend business logic that is extremely detailed.
        2. I simply want the business logic based off of the information given above.
        3. I WANT THE PLAN TO BE WELL STRUCTURED AND WITH AS MUCH DETAIL AS POSSIBLE.
        4. DO NOT WRITE ANY CODE
        5. ENSURE THE PLAN IS CONSISTANT AND THAT IT WORKS WITH THE FRONTEND PLAN.
        6. ENSURE THERE IS SUFFICIENT INFORMATION TO CREATE VIEWS.

        THE OUTPUT SHOULD BE SIMPLY IN THIS FORMAT :
        
        ### API Endpoints
        - List all reqired API endpoints
        - Specify the HTTP methods for each endpoint (GET, POST, PUT, DELETE).
        - MENTION AND SPECIFY the BUSINESS LOGIC TO IMPLEMENT FOR EACH ENDPOINT 
        - Ensure the business logic is detailed and outlines with the API logic


"""


databaseModelCoder = """
        ***Database Schema***:
        {databaseSchema}

        ***Tech Stack***:
        Django

        You are an expert in Django and writing python code.

        1. ONLY WRITE THE CODE FOR models.py.
        2. Ensure that the code is clean, readable, and follows the Django conventions.
        3. Ensure that the code is scalable and maintainable.
        4. Ensure that the code maintains data integrity.
        5. Provide unique related_name attributes for the groups and user_permissions fields in your custom User model within the AbstractUser class definition, not in the Meta class.
        6. ENSURE the code is production ready and scalable.

        ***GIVE ME THE OUTPUT IN THE FOLLOWING FORMAT BELOW***:

        ***File Name***: models.py
        [Code here]
"""


databaseSerializerCoder = """
        ***Database Schema***:
        {databaseSchema}

        ***models.py***
        {modelsCode}

        ***Tech Stack***:
        Django

        You are an expert in Django and writing python code.
        
        1. ONLY WRITE THE CODE FOR serializers.py
        2. Ensure that the code is clean, readable and follows the Django conventions.
        3. Ensure that the code is scalable and maintainable.
        4. Ensure that the code maintains data integrity.
        5. Ensure to follow business logic outlined in the database schema
        6. ENSURE the code is production ready and scalable. 


        ***GIVE ME THE OUTPUT IN THE FOLLOWING FORMAT BELOW***:

        ***File Name***: serializers.py
        [Code here]
"""

viewsPlanner = """


"""



databaseViewsCoder ="""
        ***Database Schema***:
        {databaseSchema}

        ***models.py***
        {models}

        ***serializer.py***
        {serealizers}

        ***API Endpoints***:
        {apiEndpoints_Details}

        ***Tech Stack***:
        Django

        You are an expert in Django and writing python code. You are currently writing views for a React Frontend. 
        
        1. ONLY WRITE THE CODE FOR views.py.
        2. Ensure that the code is scalable and maintainable.
        3. Ensure to follow business logic outlined in API ENDPOINTS.
        4. Ensure to create all API endpoints specified. I DO NOT CARE HOW LONG THE CODE IS.
        5. STRICTLY FOLLOW THE OUTLINE LISTED IN API ENDPOINTS.
        6. ENSURE TO COMPLETE THE BUSINESS LOGIC FOR ALL API ENDPOINTS.


        ***GIVE ME THE OUTPUT IN THE FOLLOWING FORMAT BELOW***:

        ***File Name***: views.py
        [Code here]
"""


databaseUrlsCoder ="""
        ***views.py***
        {views}

        ***Tech Stack***:
        Django

        You are an expert in Django and writing python code. You are working on a Django project and need to write the urls.py file for an ERP system.
        
        1. ONLY WRITE THE CODE FOR urls.py.
        2. Ensure that the code is clean, readable and follows the Django conventions.
        3. Ensure to follow business logic outlined in the database schema for all the views
        4. ENSURE the code is production ready and scalable. 
        5. ENUSRE THE URLS CONNECT TO THE VIEWS
        5. ENSURE TO HAVE ALL THE URLS UNDER API ENDPOINTS


        ***GIVE ME THE OUTPUT IN THE FOLLOWING FORMAT BELOW***:

        ***File Name***: urls.py
        [Code here]
"""



#Creating tests

creatingTests = """
        ***models.py***
        {models}

        ***serializer.py***
        {serealizers}

        ***views.py***:
        {viewsCode}

        ***urls.py***:
        {urlsCode}

        You are an expert in Django and writing python code. You are working on a Django project and need to write the tests.py file for an ERP system.

        1. Write tests for the models, serializers and views in the Django project.
        2. Ensure proper setup of test data using fixtures or setUp methods to create a consistent testing environment.
        3. Test edge cases and error conditions to ensure the application can handle unexpected inputs and scenarios gracefully
        


        ***File Name***: urls.py
        [Code here]

"""