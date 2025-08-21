import PyInstaller.__main__
import os
import shutil

def build_exe():
    print("Building RegexExplorer executable...")
    
    PyInstaller.__main__.run([
        'regexExplorer.py',
        '--onefile',
        '--windowed',
        '--name=RegexExplorer',
        '--icon=icon.ico',
        '--add-data=README.md;.',
        '--clean',
        '--noconfirm'
    ])
    
    print("Build completed!")
    print("Executable location: dist/RegexExplorer.exe")
    
    if not os.path.exists('releases'):
        os.makedirs('releases')
    
    if os.path.exists('dist/RegexExplorer.exe'):
        shutil.copy2('dist/RegexExplorer.exe', 'releases/RegexExplorer.exe')
        print("Executable copied to releases/ folder")

if __name__ == "__main__":
    build_exe()
