from setuptools import setup,findpackages
import os
def get_requirements(filename):
    requirement_list = []
    try:
        with open(filename, "r") as f:
            file_content = f.readlines()
            for line in file_content:
                requirement = line.strip()
                if requirement and not requirement.startswith("-e"):
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. No dependencies will be installed.")
    except Exception as e:
        print("An error occurred : {}".format(e))
    finally:
        print("code ran ")
    return requirement_list

setup(
    name="Research_project_using_CNN_to_predict_steel_microstructure_features",
    version="0.0.1",
    author="Govind Chandra Mohanty",
    author_email="govindmohanty4@gmail.com",
    packages=findpackages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.7",
    license="MIT",
    description="A package for predicting steel microstructure features using CNN",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="pass"
)
