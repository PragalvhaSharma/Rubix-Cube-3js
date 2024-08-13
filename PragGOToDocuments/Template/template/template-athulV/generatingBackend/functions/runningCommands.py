import os
import subprocess

class RunCommand:
    #running just one cli command
    @staticmethod
    def run_cli_command(command: str):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error executing {command}: {result.stderr}")
    
    #running multiple cli commands
    @staticmethod
    def run_combined_commands(commands: list):
        combined_command = " && ".join(commands)
        RunCommand.run_cli_command(combined_command)
    
    #Creating django superuser
    @staticmethod
    def create_django_superuser(project_path, username, email, password):
        """
        Creates a Django superuser with the given credentials.

        Parameters:
        - project_path: str - The path to the Django project
        - username: str - The username for the superuser
        - email: str - The email address for the superuser
        - password: str - The password for the superuser
        """
        manage_py = os.path.join(project_path, 'manage.py')

        # Create superuser command
        command = (
            f'python3 {manage_py} createsuperuser '
            f'--username {username} '
            f'--email {email} '
            f'--noinput'
        )

        # Set the environment variable for password
        env_command = f'export DJANGO_SUPERUSER_PASSWORD={password}'

        # Combine commands
        combined_command = f'{env_command} && {command}'

        # Execute the combined command
        RunCommand.run_cli_command(combined_command)

# Example usage:
# create_django_superuser('/path/to/your/project', 'admin', 'admin@example.com', 'securepassword123')