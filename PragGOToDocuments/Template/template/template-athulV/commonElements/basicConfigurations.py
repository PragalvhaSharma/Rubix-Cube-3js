import os
import subprocess
import psycopg2
import shutil
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class CreatingDirectory:

    # Constructor
    def __init__(self, projectName):
        self.current_directory = os.getcwd()
        self.backend_path = ""
        self.backend_project_path = ""
        self.overallFolderName = projectName
        self.djangoMainProjectName = self.overallFolderName + "project_files"
        self.overallProjectpath = ""
        self.appName = "erp"
        self.backend_app_path = ""
    
    # Creates the project folder
    def createProjectFolder(self):
        try:
            project_path = os.path.join(self.current_directory, self.overallFolderName)
            if not os.path.exists(project_path):
                os.makedirs(project_path)
                print(f"Project '{self.overallFolderName}' has been created.")
                self.overallProjectpath = project_path
            else:
                print(f"Project '{self.overallFolderName}' already exists.")
                self.overallProjectpath = project_path
            return self.overallProjectpath
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    # Makes a React project
    def makeReactProject(self):
        if self.overallProjectpath is None:
            print("Project folder has not been created.")
            return None
        
        try:
            frontend_path = os.path.join(self.overallProjectpath, 'frontend')
            if os.path.exists(frontend_path):
                shutil.rmtree(frontend_path)  # Delete the existing frontend folder
                print(f"Existing frontend directory '{frontend_path}' has been deleted.")
            
            os.makedirs(frontend_path)
            os.chdir(frontend_path)
           
            subprocess.check_call('npx create-react-app . --yes', shell=True)
         
            print("React project has been created in the frontend directory.")
            return frontend_path
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while creating the React project: {e}")
            return None
        except FileNotFoundError as e:
            print(f"Command not found: {e}")
            return None
        finally:
            os.chdir(self.current_directory)
    
    # Makes a Django project
    def makeDjangoProject(self):
        if self.overallProjectpath is None:
            print("Project folder has not been created.")
            return None
        
        try:
            # Create backend directory
            self.backend_path = os.path.join(self.overallProjectpath, 'backend')
            if os.path.exists(self.backend_path):
                shutil.rmtree(self.backend_path)  # Delete the existing backend folder
                print(f"Existing backend directory '{self.backend_path}' has been deleted.")
                      
            os.makedirs(self.backend_path, exist_ok=True)
            self.setupDjangoProject()
            return self.backend_project_path, self.backend_app_path, self.backend_path
        finally:
            os.chdir(self.current_directory)
    
    # Sets up the Django project
    def setupDjangoProject(self):
        try:
            os.chdir(self.backend_path)
            subprocess.check_call(['pip', 'install', 'django'])
            subprocess.check_call(['pip', 'install', 'djangorestframework'])
            subprocess.check_call(['django-admin', 'startproject', self.djangoMainProjectName, '.'])
            subprocess.check_call(['django-admin', 'startapp', self.appName])
            print(f"Django project {self.djangoMainProjectName} has been created in the backend directory.")
            print(f"Django app {self.appName} has been created in the backend directory.")

            self.backend_project_path = os.path.join(self.backend_path, self.djangoMainProjectName)
            self.backend_app_path = os.path.join(self.backend_path, self.appName)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while setting up projects: {e}")
            return None
        finally:
            os.chdir(self.current_directory)
        
    def basic_backendSetup(self, db_name, db_user, db_password):
        settingsPath = os.path.join(self.backend_project_path, 'settings.py')
        self.update_settings(settingsPath, db_name, db_user, db_password)
        self.create_database(db_name, 'localhost', '5432', db_user, db_password)
    
    def update_settings(self, settingsPath, db_name, db_user, db_password, db_host='localhost', db_port='5432'):
        try:
            with open(settingsPath, 'r') as file:
                lines = file.readlines()

            new_lines = []
            db_settings_section = False
            for line in lines:
                if line.strip().startswith('DATABASES = {'):
                    db_settings_section = True
                    new_lines.append("DATABASES = {\n")
                    new_lines.append("    'default': {\n")
                    new_lines.append("        'ENGINE': 'django.db.backends.postgresql',\n")
                    new_lines.append(f"        'NAME': '{db_name}',\n")
                    new_lines.append(f"        'USER': '{db_user}',\n")
                    new_lines.append(f"        'PASSWORD': '{db_password}',\n")
                    new_lines.append(f"        'HOST': '{db_host}',\n")
                    new_lines.append(f"        'PORT': '{db_port}',\n")
                    new_lines.append("    }\n")
                elif db_settings_section and line.strip() == '}':
                    db_settings_section = False
                elif not db_settings_section:
                    if line.strip().startswith('INSTALLED_APPS = ['):
                        new_lines.append(line)
                        new_lines.append(f"    '{self.djangoMainProjectName}',\n")
                        new_lines.append(f"    '{self.appName}',\n")
                        new_lines.append(f"    'rest_framework',\n")
                    else:
                        new_lines.append(line)

            with open(settingsPath, 'w') as file:
                file.writelines(new_lines)

            print(f"Updated settings in {settingsPath}")

        except Exception as e:
            print(f"An error occurred while updating the settings: {e}")
    
    def create_database(self, db_name, db_host, db_port, postgres_user, postgres_password):
        try:
            # Connect to PostgreSQL as the postgres user
            conn = psycopg2.connect(
                dbname="postgres",  # Connect to the default 'postgres' database
                user=postgres_user,
                password=postgres_password,
                host=db_host,
                port=db_port
            )
            print("Connected to the PostgreSQL server.")

            # Set isolation level to autocommit
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # Create a cursor object
            cursor = conn.cursor()

            # Check if the database exists
            cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
            exists = cursor.fetchone()

            if exists:
                # Terminate all connections to the database
                cursor.execute(f"""
                    SELECT pg_terminate_backend(pg_stat_activity.pid)
                    FROM pg_stat_activity
                    WHERE pg_stat_activity.datname = '{db_name}'
                    AND pid <> pg_backend_pid();
                """)
                print(f"Terminated all connections to the database '{db_name}'.")

                # Drop the existing database
                cursor.execute(f"DROP DATABASE {db_name};")
                print(f"Database '{db_name}' was deleted successfully as it already existed.")
                print()

            # Create the database
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"Database '{db_name}' created successfully.")

            # Close cursor and connection
            cursor.close()
            conn.close()

        except psycopg2.OperationalError as e:
            print(f"Operational error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 
            
############################################################################################################
############################################################################################################
# TEST
 
 
