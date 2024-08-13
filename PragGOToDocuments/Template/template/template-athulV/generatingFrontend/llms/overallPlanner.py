import sys
import os
import re

# Add the directory containing 'mainClasses' to the system path
sys.path.append(os.path.abspath('/Users/pragalvhasharma/Downloads/PragGOToDocuments/Template/template/template-athulV'))

from mainClasses.plannerClientRequest import PlannerClientRequest
from prompts.combinedPrompt import overallPlanner

class InitialPlanner(PlannerClientRequest):
    def __init__(self, businessProblem, model, streaming):
        self.model = model
        self.businessProblem = businessProblem
        self.streaming = streaming
        self.output = ""
    
    def create_OverallPlan(self):
        with open(self.businessProblem, 'r') as file:
            businessProblemContent = file.read()
        formattedFrontendPlan = overallPlanner.format(businessProblem = businessProblemContent)
        super().__init__(formattedFrontendPlan, 
                         self.model, 
                         "Follow the instruction exactly as specified. DO NOT CREATE HEADERS OR FOOTERS OR DRAWERS. NO MATTER WHAT. ", 
                         self.streaming)
        self.output = super().generate()
        if self.streaming == False:
            self.output = self.output.choices[0].message.content
        return self.output
    
    def get_each_module(self):
        return parse_MODULE_PLAN(self.output)

import re

def parse_MODULE_PLAN(text):
    pages_list = []
    
    # Split the text by pages accounting for spaces before '### PAGE'
    pages = re.split(r'(?=### PAGE: .+)', text)
    
    # Remove any leading/trailing whitespace and filter out empty strings
    pages = [page.strip() for page in pages if page.strip()]
    
    # Add each page to the list
    for page in pages:
        pages_list.append(page)
        
    return pages_list




# TESTING
# testObject = InitialPlanner("sampleProblem.txt", "gpt-4o", True)
# testObject.create_OverallPlan()
# moduleList = testObject.get_each_module()
# print(moduleList)
