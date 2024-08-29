import yaml
import subprocess

# Load environment.yml file
env_file = 'environment.yml'
with open(env_file, 'r') as f:
    env = yaml.safe_load(f)

def create_conda_env(env_file):
    try:
        # Create the conda environment
        subprocess.run(f"conda create --name {env['name']} python={env['dependencies'][0]}", shell=True)
        print('Conda environment created successfully!')
    except subprocess.CalledProcessError as e:
        print(f'Error creating conda environment: {e}')

# Call the function to create the conda environment
create_conda_env(env_file)