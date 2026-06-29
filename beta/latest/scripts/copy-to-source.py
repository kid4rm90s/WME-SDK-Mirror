import os
import shutil

subfolders = [
    'classes', 'documents', 'functions',
    'interfaces', 'modules', 'types', 'variables'
]

base_dir = os.getcwd()
source_dir = os.path.join(base_dir, '..', 'source')

copied_files = []

for folder in subfolders:
    src_folder = os.path.join(base_dir, folder)
    dst_folder = os.path.join(source_dir, folder)

    if not os.path.isdir(src_folder):
        print(f"Skipping {folder}: source directory not found")
        continue

    if not os.path.isdir(dst_folder):
        os.makedirs(dst_folder, exist_ok=True)
        print(f"Created destination: {dst_folder}")

    for filename in os.listdir(src_folder):
        if filename.endswith('.md'):
            src_file = os.path.join(src_folder, filename)
            dst_file = os.path.join(dst_folder, filename)
            try:
                shutil.copy2(src_file, dst_file)
                copied_files.append(dst_file)
                print(f"Copied: {dst_file}")
            except Exception as e:
                print(f"Could not copy {src_file}: {e}")

if not copied_files:
    print("No .md files to copy.")
else:
    print(f"\nCopied {len(copied_files)} files to ../source/")