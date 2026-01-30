import yaml


with open('configs/app-config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(f"Application Name: {config['app_name']}")
print(f"Environment: {config['environment']}")