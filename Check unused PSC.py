import os
import glob

def check_unused_psc_files(scripts_dir, esp_dir, output_file):
    # Get a list of all .psc files in the scripts directory
    psc_files = glob.glob(os.path.join(scripts_dir, '*.psc'))
    psc_file_names = {os.path.splitext(os.path.basename(file))[0] for file in psc_files}

    # Get a list of all .yaml files in the esp directory
    yaml_files = glob.glob(os.path.join(esp_dir, '**', '*.yaml'), recursive=True)

    # Set to store names of psc files found in yaml files
    found_psc_files = set()

    # Check each yaml file for psc file names
    for yaml_file in yaml_files:
        with open(yaml_file, 'r') as file:
            content = file.read()
            for psc_name in psc_file_names:
                if psc_name in content:
                    found_psc_files.add(psc_name)

    # Determine unused psc files
    unused_psc_files = psc_file_names - found_psc_files

    # Write unused psc files to the output file
    with open(output_file, 'w') as file:
        for psc_name in unused_psc_files:
            file.write(f"{psc_name}\n")

scripts_directory = 'Source/Scripts'
esp_directory = 'Source/ESP'
output_filename = 'unused_psc_files.txt'

check_unused_psc_files(scripts_directory, esp_directory, output_filename)
