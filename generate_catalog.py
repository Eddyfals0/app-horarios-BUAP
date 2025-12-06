import os
import json

def generate_catalog():
    base_dir = "Carreras"
    catalog = {}

    if not os.path.exists(base_dir):
        print(f"Error: Directory '{base_dir}' not found.")
        return

    print("Scanning directories and reading files...")
    
    # Walk through the directory structure
    for root, dirs, files in os.walk(base_dir):
        rel_path = os.path.relpath(root, base_dir)
        
        if rel_path == ".":
            continue
            
        path_parts = rel_path.split(os.sep)
        career_name = path_parts[0]
        
        if career_name not in catalog:
            catalog[career_name] = []
            
        for file in files:
            if file.lower().endswith(".csv"):
                full_path = os.path.join(root, file)
                try:
                    # Read the CONTENT of the CSV
                    # Try UTF-8 first, fallback to latin-1 if needed
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            content = f.read()
                    except UnicodeDecodeError:
                         with open(full_path, "r", encoding="latin-1") as f:
                            content = f.read()

                    catalog[career_name].append({
                        "name": file,
                        "content": content
                    })
                except Exception as e:
                    print(f"Error reading {file}: {e}")

    # Sort results
    sorted_catalog = {k: sorted(v, key=lambda x: x['name']) for k, v in sorted(catalog.items())}

    # Output as a JavaScript variable assignment
    js_content = f"window.CARRERAS_DATA = {json.dumps(sorted_catalog, ensure_ascii=False)};"

    with open("carreras.js", "w", encoding="utf-8") as f:
        f.write(js_content)
        print(f"Successfully created 'carreras.js' with {len(sorted_catalog)} careers.")

if __name__ == "__main__":
    generate_catalog()
