import zipfile;
import os;

files_to_zip = ["fix.css", "manifest.json"];
zip_filename = 'build/extension.zip';

def build():
    try:
        os.mkdir("build");
        print(f"Folder 'build' created successfully");
    except FileExistsError:
        print(f"Folder 'build' already exists");

    print("Building:");
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            if os.path.isfile(file):
                zipf.write(file, arcname=os.path.basename(file));
                print(f"    Added '{file}' to '{zip_filename}'");
            else:
                print(f"    Warning: '{file}' does not exist and was skipped.");

    print(f"Created '{zip_filename}' successfully.");

if __name__ == '__main__':
    build();