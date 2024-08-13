import sys
import os

# Add the directory containing 'mainClasses' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from mainClasses.coderClientRequest import CoderClientRequest
from prompts.backendPrompts import databaseModelCoder, databaseSerializerCoder, databaseViewsCoder, databaseUrlsCoder


from dotenv import load_dotenv
load_dotenv()

plannerOutput = """
### Entities and Relationships

#### **Table Name: Users**
- **Attributes**:
  - id (Primary Key)
  - username
  - password
  - email
  - first_name
  - last_name
  - role (e.g. admin, assembler, glazier, installer)
- **Relationships To other tables**:
  - One-to-Many with PurchaseOrders (Created by)
  - One-to-Many with WorkOrders (Assigned to, Completed by)
  
#### **Table Name: PurchaseOrders**
- **Attributes**:
  - id (Primary Key)
  - order_date
  - supplier_name
  - status (e.g. pending, completed, cancelled)
  - created_by (Foreign Key referencing Users(id))
  - total_cost
- **Relationships To other tables**:
  - Many-to-One with Users (Created by)
  - One-to-Many with PurchaseOrderItems

#### **Table Name: PurchaseOrderItems**
- **Attributes**:
  - id (Primary Key)
  - purchase_order_id (Foreign Key referencing PurchaseOrders(id))
  - frame_type
  - quantity
  - unit_price
- **Relationships To other tables**:
  - Many-to-One with PurchaseOrders

#### **Table Name: Frames**
- **Attributes**:
  - id (Primary Key)
  - frame_type
  - dimensions
  - material
  - color
  - cost
- **Relationships To other tables**:
  - One-to-Many with WorkOrders

#### **Table Name: WorkOrders**
- **Attributes**:
  - id (Primary Key)
  - frame_id (Foreign Key referencing Frames(id))
  - status (e.g. pending, in progress, completed)
  - assigned_to (Foreign Key referencing Users(id))
  - completed_by (Foreign Key referencing Users(id))
  - assigned_date
  - completed_date
- **Relationships To other tables**:
  - Many-to-One with Frames
  - Many-to-One with Users (Assigned to)
  - Many-to-One with Users (Completed by)

#### **Table Name: Assembly**
- **Attributes**:
  - id (Primary Key)
  - work_order_id (Foreign Key referencing WorkOrders(id))
  - start_time
  - end_time
  - notes
- **Relationships To other tables**:
  - One-to-One with WorkOrders

#### **Table Name: Glazing**
- **Attributes**:
  - id (Primary Key)
  - work_order_id (Foreign Key referencing WorkOrders(id))
  - start_time
  - end_time
  - notes
- **Relationships To other tables**:
  - One-to-One with WorkOrders

#### **Table Name: Installation**
- **Attributes**:
  - id (Primary Key)
  - work_order_id (Foreign Key referencing WorkOrders(id))
  - start_time
  - end_time
  - notes
- **Relationships To other tables**:
  - One-to-One with WorkOrders

#### **Table Name: Statistics**
- **Attributes**:
  - id (Primary Key)
  - report_date
  - total_orders
  - completed_orders
  - pending_orders
  - total_revenue
- **Relationships To other tables**:
  - None (This table will be used for generating statistical reports)
"""

class Coder(CoderClientRequest):
    def __init__(self, model, backendPath, streaming):
        self.model = model
        self.streaming = streaming 
        self.backendPath = backendPath
    
    def generateModelCode(self, plannerOutput):
        formattedModelGeneration_prompt = databaseModelCoder.format(databaseSchema = plannerOutput)
        super().__init__(formattedModelGeneration_prompt, 
                         "gpt-4o", 
                         "Write code for the models created above in Django in one models.py file. GIVE ME SIMPLY THE CODE AND CODE ALONE", 
                         True)
        modelOutput = super().generate()
        if self.streaming == False:
            outputText = modelOutput.choices[0].message.content
        else:
            outputText = modelOutput
        return outputText
    
    def generateSerealizerCode(self, databaseSchema, modelCode):
        formattedSerealizerGeneration_prompt = databaseSerializerCoder.format(databaseSchema = databaseSchema, 
                                                                              modelsCode = modelCode)
        super().__init__(formattedSerealizerGeneration_prompt, 
                         "gpt-4o", "Write code for the serealizers. GIVE ME SIMPLY THE CODE AND CODE ALONE", 
                         True)
        serealizerOutput = super().generate()
        if self.streaming == False:
            outputSerealizerCode = serealizerOutput.choices[0].message.content
        else:
            outputSerealizerCode = serealizerOutput
        return outputSerealizerCode
    
    def generateViewsCode(self, databaseSchema, modelsCode, serealizerCode, apiEndpoints_Details):
        formattedViewsGeneration_prompt = databaseViewsCoder.format(databaseSchema = databaseSchema,
                                                                    models = modelsCode, 
                                                                    serealizers = serealizerCode,
                                                                    apiEndpoints_Details = apiEndpoints_Details)
        print("----------------- - - - - - - - - -- - - - -- - - - - -- - ")
        print("----------------- - - - - - - - - -- - - - -- - - - - -- - ")
        print(formattedViewsGeneration_prompt)
        print("----------------- - - - - - - - - -- - - - -- - - - - -- - ")
        print("----------------- - - - - - - - - -- - - - -- - - - - -- - ")
        super().__init__(formattedViewsGeneration_prompt, "gpt-4o", "Write code for the views. ENSURE ALL API ENTPOINTS ARE CREATED. GIVE ME SIMPLY THE CODE AND CODE ALONE", True)
        viewsOutput = super().generate()
        if self.streaming == False:
            outputViewsCode = viewsOutput.choices[0].message.content
        else: 
            outputViewsCode = viewsOutput
        return outputViewsCode
    
    def generateUlsCode(self, viewsCode):
        formattedUrls_prompt = databaseUrlsCoder.format(views = viewsCode)
        super().__init__(formattedUrls_prompt, 
                         "gpt-4o", "Write code for the URLS. GIVE ME SIMPLY THE CODE AND CODE ALONE", 
                         True)
        viewsOutput = super().generate()
        if self.streaming == False:
            outputViewsCode = viewsOutput.choices[0].message.content
        else:
            outputViewsCode = viewsOutput
        return outputViewsCode

#Testing
# testObject = Coder("gpt-4o", True)
# testObject.generateModelCode(plannerOutput)
