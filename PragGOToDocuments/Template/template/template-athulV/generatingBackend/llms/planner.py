import sys
import os

# Add the directory containing 'mainClasses' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from mainClasses.coderClientRequest import CoderClientRequest
from prompts.backendPrompts import backendLogicPlanner, databaseSchemaMaker

from dotenv import load_dotenv
load_dotenv()

class BackendPlanner(CoderClientRequest):
    def __init__(self, businessProblem, model, streaming):
        self.model = model
        self.businessProblem = businessProblem
        self.streaming = streaming

    def databaseModelPlanMaker(self, overallPlan):
        with open(self.businessProblem, 'r') as file:
            businessProblemContent = file.read()
        formattedDatabaseModelPlan = databaseSchemaMaker.format(business_problem = businessProblemContent, 
                                                                overallPlan = overallPlan)
        super().__init__(formattedDatabaseModelPlan, 
                         self.model, 
                         "Follow the instruction exactly as specified", 
                         self.streaming)
        modelOutput = super().generate()
        if self.streaming == False:
            outputText = modelOutput.choices[0].message.content
        else:
            outputText = modelOutput
        return outputText
    
    def backendLogicPlanMaker(self, overallPlan, databaseSchema):
        with open(self.businessProblem, 'r') as file:
            businessProblemContent = file.read()
        formattedBackendLogicPlan = backendLogicPlanner.format(business_problem = businessProblemContent, 
                                                               overallPlan = overallPlan,
                                                               databaseSchema = databaseSchema)
        super().__init__(formattedBackendLogicPlan, 
                         self.model, 
                         "Follow the instruction exactly as specified", 
                         self.streaming)
        modelOutput = super().generate()
        if self.streaming == False:
            outputText = modelOutput.choices[0].message.content
        else:
            outputText = modelOutput
        return outputText

    
#Testing 
# testObject = InitialPlanner("problem.txt", "gpt-4o", True)
# databaseSchema = testObject.databaseModelPlanMaker(pagebyPagePlan)
# backendLogicPlan = testObject.backendLogicPlanMaker(pagebyPagePlan, databaseSchema)