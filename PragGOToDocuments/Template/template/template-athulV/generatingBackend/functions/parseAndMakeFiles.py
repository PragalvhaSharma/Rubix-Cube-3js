import os 

codeOutput = """
***File Name***: models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    supplier_name = models.CharField(max_length=255)
    item_description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Frame(models.Model):
    type = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WorkOrder(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, related_name='work_orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_orders')
    assembly_status = models.CharField(max_length=50)
    glazing_status = models.CharField(max_length=50)
    installation_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AssemblyLog(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='assembly_logs')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50)

class GlazingLog(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='glazing_logs')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50)

class InstallationLog(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='installation_logs')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50)

class Statistic(models.Model):
    metric_name = models.CharField(max_length=255)
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)
```
"""

import os

class ParsingAndAddingFiles:

    @staticmethod
    def parse_python_code(text):
        # Extracting the file name
        try:
            file_name_line = next(line for line in text.split('\n') if line.strip().startswith('***File Name***:'))
            file_name = file_name_line.split('***File Name***: ')[1]
        except (StopIteration, IndexError) as e:
            raise ValueError("File name line is missing or improperly formatted")

        # Extracting the code
        try:
            code_lines = text.split('```python\n')[1].rsplit('\n```')[0]
        except IndexError:
            raise ValueError("Code block is missing or improperly formatted")

        # Constructing the dictionary
        parsed_code = {file_name: code_lines}

        return parsed_code

    @staticmethod
    def create_codeFiles(directory_path, code_dict):
        # Ensure the directory exists
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        
        # Loop through the dictionary and create files with the corresponding code
        for file_name, code in code_dict.items():
            # Construct the file path
            file_path = os.path.join(directory_path, file_name)
            
            # Write the code to the file, clearing if the file exists
            with open(file_path, 'w') as file:
                file.write(code)
                file.write('\n')  # Optional: Add a newline for separation
    
    @staticmethod
    def generate_urls_py(folder_path, app_name):
        lines = []
        lines.append("from django.contrib import admin\n")
        lines.append("from django.urls import include, path\n")
        lines.append("urlpatterns = [\n")
        lines.append("    path('admin/', admin.site.urls),\n")
        lines.append(f"   path('', include('{app_name}.urls')),\n")
        lines.append("]\n")
        
        urls_file_path = os.path.join(folder_path, 'urls.py')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(urls_file_path, 'w') as file:
            file.writelines(lines)

        print("- - - - - - - - - - - - - - - - - - - - - -")
        print(f"urls.py file has been generated FOR THE MAIN PROJECT.")
        print("- - - - - - - - - - - - - - - - - - - - - -")

#Test the code
# dictMade = ParsingAndAddingFiles.parse_python_code(codeOutput)
# ParsingAndAddingFiles.create_codeFiles("/Users/pragalvhasharma/Downloads/PragGOToDocuments/Template/template/TemplateTogether/testFolder", dictMade)