from commonElements.basicConfigurations import CreatingDirectory
from generatingFrontend.llms.overallPlanner import InitialPlanner
from generatingFrontend.llms.frontendCoder import CodingAssistant
from generatingFrontend.llms.planner import PageByPagePlanner
from generatingFrontend.functions.parsingJavascript import ParseAndAdd
from commonElements.clearingTextFile import clear_file_if_not_empty
from commonElements.writingToOutputFiles import WritingToOutputFiles
from generatingBackend.llms.planner import BackendPlanner
from generatingBackend.llms.coder import Coder
from generatingBackend.functions.parseAndMakeFiles import ParsingAndAddingFiles
from generatingBackend.functions.runningCommands import RunCommand
import threading

#Creatign the directory
applicationName = input("Enter your application name: ")
if applicationName:
    directoryObject = CreatingDirectory(applicationName)
    directoryObject.createProjectFolder()
    print('here')
    frontendPath = directoryObject.makeReactProject()
    backend_project_path, backend_app_path, backend_path = directoryObject.makeDjangoProject()
    directoryObject.basic_backendSetup(applicationName + "db", "postgres", "984138o35o")
else:
    print("Please enter a valid application name")

filePath = 'sampleProblem.txt'
planner = InitialPlanner(filePath, "gpt-4o", True)
modulePlan = planner.create_OverallPlan()
eachIndividualModule = planner.get_each_module()
WritingToOutputFiles.writeToOutputFILE(modulePlan, "modelOutputs/overallPlannerOUTPUT.txt")

def runFrontend(eachIndividualModule, frontendPath):
    planOutputFile = "modelOutputs/frontendOutputs/plannerOutput.txt"
    codeOutputFile = "modelOutputs/frontendOutputs/codeOutput.txt"

    # Check both files
    clear_file_if_not_empty(planOutputFile)
    clear_file_if_not_empty(codeOutputFile)

    # This is problem.txt
    moduleInDepthPlanner = PageByPagePlanner(eachIndividualModule, "gpt-4o")
    moduleDetailedPlanLIST = moduleInDepthPlanner.plannerOutput()
    WritingToOutputFiles.writeToOutputFILE("\n" + moduleDetailedPlanLIST, planOutputFile)

    codingAssistant = CodingAssistant(moduleDetailedPlanLIST, "gpt-4o", True)
    generatedPage_By_Page_Code = codingAssistant.generate_code_by_Thread()
    WritingToOutputFiles.writeToOutputFILE("\n" + generatedPage_By_Page_Code, codeOutputFile)

    modifyingExistingCode = ParseAndAdd(generatedPage_By_Page_Code, frontendPath)
    modifyingExistingCode.add_or_updateFiles()

# def runBackend(overallPlan, backend_project_path, backend_app_path, backend_path):
#     planOutputFile = "modelOutputs/backendOutputs/plannerOutput.txt"
#     codeOutputFile = "modelOutputs/backendOutputs/codeOutput.txt"

#     # Check both files
#     clear_file_if_not_empty(planOutputFile)
#     clear_file_if_not_empty(codeOutputFile)

#     #Create database schema
#     BackendPlannerObject = BackendPlanner(filePath, "gpt-4o", True)
#     databaseSchema = BackendPlannerObject.databaseModelPlanMaker(overallPlan)
#     WritingToOutputFiles.writeToOutputFILE("\n" + databaseSchema, planOutputFile)

#     #Creating backend logic plan
#     backendLogicPlan = BackendPlannerObject.backendLogicPlanMaker(overallPlan, databaseSchema)
#     WritingToOutputFiles.writeToOutputFILE("\n" + backendLogicPlan, planOutputFile)

#     #GeneratingCode for models.py
#     coderObject = Coder("gpt-4o", backend_project_path, True)
#     modelCode = coderObject.generateModelCode(databaseSchema)
#     WritingToOutputFiles.writeToOutputFILE("\n" + modelCode, codeOutputFile)

#     #pushing models.py to the code File
#     codeDict = ParsingAndAddingFiles.parse_python_code(modelCode)
#     ParsingAndAddingFiles.create_codeFiles(backend_app_path, codeDict)
#     commands = [
#     f"cd {backend_path}",
#     "python manage.py makemigrations",
#     "python manage.py migrate"
#     ]
#     RunCommand.run_combined_commands(commands)
#     print(" - - - - - -  - - - -  - - - - - - ")
#     print(" Tables have been created ")
#     print(" - - - - - -  - - - -  - - - - - - ")

#     #Generating serealizer code 
#     serealizerCode = coderObject.generateSerealizerCode(databaseSchema, modelCode)
#     WritingToOutputFiles.writeToOutputFILE("\n" + serealizerCode, codeOutputFile)
#     codeDict = ParsingAndAddingFiles.parse_python_code(serealizerCode)
#     ParsingAndAddingFiles.create_codeFiles(backend_app_path, codeDict)

#     #Generating views code 
#     viewCode = coderObject.generateViewsCode(databaseSchema, modelCode, serealizerCode, backendLogicPlan)
#     WritingToOutputFiles.writeToOutputFILE("\n" + viewCode, codeOutputFile)
#     codeDict = ParsingAndAddingFiles.parse_python_code(viewCode)
#     ParsingAndAddingFiles.create_codeFiles(backend_app_path, codeDict)

#     #writing and making urls
#     urlCode = coderObject.generateUlsCode(viewCode)
#     WritingToOutputFiles.writeToOutputFILE("\n" + urlCode, codeOutputFile)
#     codeDict = ParsingAndAddingFiles.parse_python_code(urlCode)
#     ParsingAndAddingFiles.create_codeFiles(backend_app_path, codeDict)

#     #MAIN PROJECT URL
#     ParsingAndAddingFiles.generate_urls_py(backend_project_path, "erp")

#     RunCommand.create_django_superuser(backend_path, "infin8", "i8@gmail.com", "password123" )


# def run_concurrently(overallPlan, frontendPath, backend_project_path, backend_app_path, backend_path):
#     frontend_thread = threading.Thread(target=runFrontend, args=(overallPlan, frontendPath))
#     backend_thread = threading.Thread(target=runBackend, args=(overallPlan, backend_project_path, backend_app_path, backend_path))

#     frontend_thread.start()
#     backend_thread.start()

#     frontend_thread.join()
#     backend_thread.join()

#     print("Both frontend and backend processes have completed.")



# # REUNNING THE CODE

# # # RUNNING INDIVIDUALLY
runFrontend(eachIndividualModule, frontendPath)

# # # RUNNING Backend
# # runBackend(overallPlan, backend_project_path, backend_app_path, backend_path)

# # RUNNING CONCURRENTLY
# #run_concurrently(overallPlan, frontendPath, backend_project_path, backend_app_path, backend_path)
 