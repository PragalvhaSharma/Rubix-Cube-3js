from commonElements.basicConfigurations import CreatingDirectory
from generatingFrontend.llms.overallPlanner import InitialPlanner
from generatingFrontend.llms.frontendCoder import CodingAssistant
from generatingFrontend.llms.planner import PageByPagePlanner
from generatingFrontend.functions.parsingJavascript import ParseAndAdd
from commonElements.clearingTextFile import clear_file_if_not_empty
from commonElements.writingToOutputFiles import WritingToOutputFiles
import threading
import os

# Creating the base directory
applicationName = input("Enter your application name: ")
base_directory = os.path.join(os.getcwd(), applicationName)
if applicationName:
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)
else:
    print("Please enter a valid application name")

filePath = 'sampleProblem.txt'
planner = InitialPlanner(filePath, "gpt-4o", True)
overallPlan = planner.create_OverallPlan()
WritingToOutputFiles.writeToOutputFILE(overallPlan, "modelOutputs/overallPlannerOUTPUT.txt")

def runFrontend(overallPlan, frontendPath, identifier):
    planOutputFile = f"C:/Users/ATHUL/OneDrive/Desktop/TEMPLATE-COMBINED/modelOutputs/frontendOutputs/plannerOutput_{identifier}.txt"
    codeOutputFile =  f"C:/Users/ATHUL/OneDrive/Desktop/TEMPLATE-COMBINED/modelOutputs/frontendOutputs/codeOutput_{identifier}.txt"

    # Check both files
    clear_file_if_not_empty(planOutputFile)
    clear_file_if_not_empty(codeOutputFile)

    # This is problem.txt
    initialPlanner = PageByPagePlanner(overallPlan, "gpt-4o")
    pageByPagePlan = initialPlanner.plannerOutput()
    WritingToOutputFiles.writeToOutputFILE("\n" + pageByPagePlan, planOutputFile)

    # Now passing page by page plan to the coder
    codingAssistant = CodingAssistant(pageByPagePlan, "gpt-4o", True)
    generatedPage_By_Page_Code = codingAssistant.generate_code_for_each_module()
    WritingToOutputFiles.writeToOutputFILE("\n" + generatedPage_By_Page_Code, codeOutputFile)

    modifyingExistingCode = ParseAndAdd(generatedPage_By_Page_Code, frontendPath)
    modifyingExistingCode.add_or_updateFiles()

def create_project_directory(base_directory, identifier):
    project_directory = os.path.join(base_directory, f"Project_{identifier}")
    os.makedirs(project_directory, exist_ok=True)
    # Create a React project in the new directory
    directoryObject = CreatingDirectory(project_directory)
    frontendPath = directoryObject.makeReactProject()
    return frontendPath

def runFrontendConcurrently(overallPlan, base_directory):
    frontend_threads = []
    for i in range(1, 4):
        frontendPath = create_project_directory(base_directory, i)
        thread = threading.Thread(target=runFrontend, args=(overallPlan, frontendPath, i))
        frontend_threads.append(thread)

    for thread in frontend_threads:
        thread.start()

    for thread in frontend_threads:
        thread.join()

    print("All frontend processes have completed.")

# Running the code
runFrontendConcurrently(overallPlan, base_directory)
