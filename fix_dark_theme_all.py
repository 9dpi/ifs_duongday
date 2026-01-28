import os

target_dir = r"d:\Dropbox\Project\UX UI Thermal\Layouts\ifs_duongday"

def fix_theme():
    files = [f for f in os.listdir(target_dir) if f.endswith('.html') or f.endswith('.htm')]
    
    for filename in files:
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace simple <html lang="vi"> with <html lang="vi" data-theme="dark">
        # Be careful not to replace if it already has data-theme, but the search string prevents that
        
        if '<html lang="vi">' in content:
            new_content = content.replace('<html lang="vi">', '<html lang="vi" data-theme="dark">')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added dark theme to {filename}")
        else:
            print(f"Skipped {filename} (already has theme or diff lang tag)")

if __name__ == "__main__":
    fix_theme()
