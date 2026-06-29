import os

subfolders = [
    'classes', 'documents', 'functions', 
    'interfaces', 'modules', 'types', 'variables', 'NotebookLM'
]
base_dir = os.getcwd()
source_dir = os.path.join(base_dir, '..', 'source')

deleted_files = []

for folder in subfolders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        if filename.endswith('.md') or filename.endswith('-clean.html'):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Could not delete {file_path}: {e}")

# Clean ../source/ directory (version control archive)
for folder in subfolders:
    folder_path = os.path.join(source_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        if filename.endswith('.md') or filename.endswith('-clean.html'):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Could not delete {file_path}: {e}")

if not deleted_files:
    print("No .md or -clean.html files found.")
else:
    print(f"\nDeleted {len(deleted_files)} files.")