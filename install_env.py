import yaml
import subprocess

# Load environment.yml file
env_file = 'environment.yml'
with open(env_file, 'r') as f:
    env = yaml.safe_load(f)

# print(next((s for s in env['dependencies'] if s.startswith('python=')), None))

# try:
#     # Create the conda environment
#     subprocess.run(f"conda create --name {env['name']} {next((s for s in env['dependencies'] if s.startswith('python=')), None)}", shell=True)
#     print('Conda environment created successfully!')
# except subprocess.CalledProcessError as e:
#     print(f'Error creating conda environment: {e}')

for dep in env['dependencies'][1:]:
    try:
        # Install the dependencies
        subprocess.run(f"conda install --name {env['name']} {dep} -y", shell=True, check=True)
        print(f'{dep} installed successfully!')
    except subprocess.CalledProcessError as e:
        print(f'Error installing {dep}: {e}')
