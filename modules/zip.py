import zipfile
import os
import shutil

def zip_folder(folder_path, output_zip):
    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)

        print(f'{folder_path} has been zipped to {output_zip}')
    except Exception as e:
        print(f'Error zipping {folder_path}: {str(e)}')
