import os

class ParseAndAdd:
    
    def __init__(self, llmOutputCode, directoryPath):
        if not directoryPath:
            raise ValueError("directoryPath cannot be None or empty")
        
        self.directoryPath = directoryPath
        self.llmOutputCode = llmOutputCode
        self.output = self.extract_files()
        self.existingFiles = []
        self.nonExistingFiles = []
        
        for key in self.output.keys():
            if self.check_file_exists(key):
                self.existingFiles.append(key)
            else:
                self.nonExistingFiles.append(key)
                
    def extract_files(self):
        # Split everything line by line
        lines = self.llmOutputCode.split('\n')
        
        # Dictionary to store filename and content
        files = {}
        current_file = None
        current_content = []
        in_code_block = False

        for line in lines:
            if line.strip().startswith('***File Name***:'):
                if current_file:
                    files[current_file] = "\n".join(current_content).strip()
                parts = line.split(':')
                if len(parts) > 1:
                    current_file = parts[1].strip().strip('`')
                else:
                    print(f"Error parsing file name in line: {line}")
                    current_file = None
                current_content = []
                in_code_block = False
            elif line.strip().startswith('```'):
                in_code_block = not in_code_block
            elif in_code_block:
                current_content.append(line)

        if current_file:
            files[current_file] = "\n".join(current_content).strip()
        
        updatedFiles = self.update_keys_with_prefix(files, self.directoryPath)
        return updatedFiles

    def check_file_exists(self, file_name):
        # Here we assume file_name is already a full path
        return os.path.exists(file_name)
    
    def add_and_writeContent(self, file_name, content):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"New file {file_name} has been created in the specified directory.")
    
    def add_or_updateFiles(self):
        # Update existing files
        for file_path in self.existingFiles:
            with open(file_path, 'w') as file:
                file.write(self.output[file_path])
            print(f"File {file_path} has been updated.")
    
        # Create new files
        for file_path in self.nonExistingFiles:
            self.add_and_writeContent(file_path, self.output[file_path])

    @staticmethod
    def update_keys_with_prefix(dictionary, prefix):
        updated_dict = {}
        for key, value in dictionary.items():
            if key:
                new_key = os.path.join(prefix, key)
                updated_dict[new_key] = value
        return updated_dict
