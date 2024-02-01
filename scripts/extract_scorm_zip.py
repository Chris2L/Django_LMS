import zipfile
import os
import shutil
from pathlib import Path
import shutil
from icecream import ic
import xml.etree.ElementTree as ET
import re

from scormplayer.models import Course, CourseFormatChoices


name_of_schema_folders = {"1.2": CourseFormatChoices.SCORM_12, "2004 4th Edition": CourseFormatChoices.SCORM_2004}

def make_valid_folder_name(name):
    # Remove leading and trailing whitespace
    name = name.strip()
    
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    
    # Remove the forward slash and null character, which are invalid in Linux file names
    name = re.sub(r'[\/\0]', '', name)

    return name


def run():
    folder = "./media/zips/"
    start_path = f"{folder}RuntimeBasicCalls_SCORM12"
    start_zip = start_path + ".zip"
    if os.path.exists(f"{start_path}/"):
        ic("Deleting old folder")
        shutil.rmtree(f"{start_path}")
    try:
        with zipfile.ZipFile(start_zip,"r") as zip_ref:
            zip_ref.extractall(f"{start_path}/")
        ic("extracted scorm")
        
    except:
        print(f"error with {start_zip}")

    manifestFile = ""
    for root, dirs, files in os.walk(start_path):
        for file in sorted(files):
            if file.endswith("imsmanifest.xml"):
                manifestFile = os.path.join(root, file)

    if manifestFile == "":
        print("Could not fine manifest file")

        return
    
    path = os.path.dirname(manifestFile)
    
    # Load and parse the XML file
    has_problem = False

    tree = ET.parse(manifestFile)
    root = tree.getroot()
    schema_version = ""

    namespaces = dict([node for _, node in ET.iterparse(manifestFile,
                                                        events=['start-ns'])])

    # Extracting metadata (if present)
    metadata_element = root.find('metadata', namespaces)
    if metadata_element is not None:
        # Process the metadata based on your requirements
        schema_element = metadata_element.find('schema', namespaces)
        if schema_element is not None:
            print(f"Schema is {schema_element.text}")
            if schema_element.text not in "ADL SCORM":
                ic(f"Could not find valid schema '{schema_element.text}'")
                has_problem = True

        schemaversion_element = metadata_element.find('schemaversion', namespaces)
        if schemaversion_element is not None:
            schema_version = schemaversion_element.text
            print(f"schemaversion is {schemaversion_element.text}")
            if schemaversion_element.text not in name_of_schema_folders:
                ic(f"Could not find valid schema version '{schemaversion_element.text}'")
                has_problem = True

    resources_required = {}

    # To iterate through organizations
    organizations = root.find('organizations', namespaces)
    for organization in organizations.findall('organization', namespaces):
        # Process the organization (based on how your SCORM packages are structured)

        # Typical organization processing might involve looking at items
        for item in organization.findall('item', namespaces):
            course = {}
            course["schema_version"] = schema_version
            course["title"] = item.find('title', namespaces).text

            identifierref = item.get('identifierref')
            course["resource_identifier"] = identifierref
            course["href"] = ""
            
            resources_required[identifierref] = False

            masteryscore_element = item.find('adlcp:masteryscore', namespaces)
            if masteryscore_element is not None:
                course["mastery_score"] = int(masteryscore_element.text)
            
            # You can now iterate through the XML structure.
            # For example, to iterate through resources:
            resources = root.find('resources', namespaces)
            for resource in resources:
                scormtype_str = '{' + namespaces["adlcp"] + '}'
                resource_type = resource.attrib.get(f'{scormtype_str}scormType')
                if resource_type is None:
                    # The spelling is case sensiv
                    resource_type = resource.attrib.get(f'{scormtype_str}scormtype')

                resource_identifier = resource.attrib['identifier']
                resources_required[resource_identifier] = True

                if resource_type == 'sco':
                    # print(f"SCO found: {resource_identifier}")
                    if course["resource_identifier"] == resource_identifier:
                        course["href"] = resource.attrib.get('href', '')
                else:
                    # print(f"Asset found: {resource_identifier}")
                    pass


                for dependency_element in resource.findall('dependency', namespaces):
                    identifierref = dependency_element.attrib.get("identifierref")
                    ic(f"This resource is dependent on {identifierref}")
                    resources_required[identifierref] = False


                # To get a list of files for each resource
                for file_element in resource.findall('file', namespaces):
                    filename = file_element.get('href')
                    file_exists = os.path.isfile(f"{path}/{filename}")
                    # print(f"  File: {filename} {'exists' if file_exists else 'not found'}")
                    if not file_exists:
                        ic(f"Could not find file {path}/{filename}")
                        has_problem = True

            if course["href"] == "":
                ic(f"Could not find a valid index.html")
                has_problem = True

            ic(resources_required)
            ic(course)

    if not has_problem:
        # Set the source directory where your files are located
        source_dir = os.path.dirname(manifestFile) + "/"

        # Set the destination directory where you want to copy the files
        scorm_folder_name = make_valid_folder_name(name_of_schema_folders[course["schema_version"]].label).replace(".","")
        course_folder_name = make_valid_folder_name(course["title"]).lower()
        dest_dir = f'./media/courses/{scorm_folder_name}/{course_folder_name}'

        if os.path.exists(f"{dest_dir}/"):
            ic("The dest folder where we are moving to already exists.  Removing it first")
            shutil.rmtree(f"{dest_dir}")

        # Create the destination directory if it doesn't exist
        Path(dest_dir).mkdir(parents=True, exist_ok=True)

        ic(source_dir, dest_dir)

        for root, dirs, files in os.walk(source_dir):
            dirs.sort()
            for file in sorted(files):
                # ic(f"move from {os.path.join(root, file)} to {os.path.join(dest_dir, file)}")
                shutil.move(os.path.join(root, file), os.path.join(dest_dir, file))

            for dir in dirs:
                shutil.move(os.path.join(root, dir), dest_dir)

        if os.path.exists(f"{start_path}/"):
            ic("Deleting extracted folder")
            shutil.rmtree(f"{start_path}")
        # os.remove(start_zip)

        course_obj = Course.objects.filter(name=course["title"]).first()
        if course_obj is None:
            course_obj = Course(name=course["title"], format=name_of_schema_folders[course["schema_version"]])
            course_obj.index.name = dest_dir[1:] + '/' + course["href"]
            course_obj.save()


        print('Files copied successfully.')