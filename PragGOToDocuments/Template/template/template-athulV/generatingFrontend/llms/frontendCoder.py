import sys
import os
import threading
import threading

# Get the absolute path of the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

# Add the root directory to the Python path
sys.path.append(project_root)

from mainClasses.coderClientRequest import CoderClientRequest

from prompts.frontendPrompts import coderAgent, generateAPPJs, UiEnhancer

class CodingAssistant(CoderClientRequest):
    def __init__(self, modulePlans, model, streaming):
        self.model = model
        self.modulePlans = modulePlans
        self.streaming = streaming 
        self.allTheCode = ""

    def generate(self):
        modelOutput = super().generate()
        if self.streaming == False:
            outputText = modelOutput.choices[0].message.content
        else:
            outputText = modelOutput
        return outputText
    
    def parse_modules(self):
        # Split the input string into modules based on the '### MODULE' delimiter
        modules = self.modulePlans.strip().split('### PAGE')

        # Remove any empty strings from the list and prepend 'MODULE' to each module
        modules = [f"MODULE{module.strip()}" for module in modules if module.strip()]

        return modules
    
    def generate_code_by_Thread(self):
        moduleList = self.parse_modules()
        threads = []
        results = [None] * len(moduleList)

        def worker(index, module):
            print(f"Processing module {index}")
            coderPrompt = coderAgent.format(moduleDescription=module)
            # Create an instance of the class that generates code
            code_generator = CoderClientRequest(coderPrompt, self.model, "You are an experienced frontend software developer with expertise in REACT. GIVE ME THE CODE AND ONLY THE CODE ALONE IN THE SPECIFIED FORMAT", self.streaming)
            results[index] = code_generator.generate()
            print(f"Module {index} finished")

        for index, module in enumerate(moduleList):
            thread = threading.Thread(target=worker, args=(index, module))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()

        # Concatenate all results into a single string
        self.allTheCode = "\n".join(result for result in results if result is not None)
        self.generateAPPJS()
        return self.allTheCode
    
    def generateAPPJS(self):
        appJsPrompt = generateAPPJs.format(GeneratedCode=self.allTheCode)
        super().__init__(appJsPrompt, self.model, "Please create simply the best App.js you can and simply that only. I only want the code in the specified format and nothing else.", True)
        generatedAppJs = self.generate()
        self.allTheCode += f"\n{generatedAppJs}"
        


        
          
# ## Testing

#Testing Coder
# coder = CodingAssistant(parseTester, "gpt-4o", True)
# output = coder.generate_code_by_Thread()
# print(output)