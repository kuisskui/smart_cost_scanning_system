import os
import sys
import shutil
import platform
from pathlib import Path
import PyInstaller.__main__

def check_environment():
    """Check if the environment is suitable for building."""
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 7):
        raise RuntimeError("Python 3.7 or higher is required")
    
    # Check if running on Windows
    if platform.system() != 'Windows':
        print("Warning: Building on non-Windows system. The executable may not work on Windows.")
    
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")

def clean_build_directories():
    """Clean up build artifacts from previous builds."""
    directories_to_clean = ['build', 'dist']
    files_to_clean = ['*.spec']
    
    for directory in directories_to_clean:
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
                print(f"Cleaned {directory} directory")
            except Exception as e:
                print(f"Warning: Failed to clean {directory}: {e}")
    
    for pattern in files_to_clean:
        try:
            for file in Path('.').glob(pattern):
                file.unlink()
                print(f"Cleaned {file}")
        except Exception as e:
            print(f"Warning: Failed to clean {pattern} files: {e}")

def ensure_resources():
    """Ensure all necessary resources are available."""
    resources_dir = Path('app/resources')
    resources_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if icon exists
    icon_path = resources_dir / 'icon.ico'
    if not icon_path.exists():
        print("Warning: Application icon not found")
        return None
    
    return str(icon_path)

def build_executable():
    """Build the executable using PyInstaller."""
    try:
        print("\nStarting build process...")
        print("-" * 50)
        
        # Check environment
        check_environment()
        
        # Clean previous build artifacts
        clean_build_directories()
        
        # Ensure resources
        icon_path = ensure_resources()
        
        # Base PyInstaller arguments
        pyinstaller_args = [
            'main.py',  # Your main script
            '--name=ExcelProcessor',  # Name of the output executable
            '--onefile',  # Create a single executable file
            '--windowed',  # Don't show console window on Windows
            '--clean',  # Clean PyInstaller cache
            '--noconfirm',  # Replace output directory without confirmation
            # Add hidden imports
            '--hidden-import=pandas',
            '--hidden-import=openpyxl',
            '--hidden-import=PIL',
            '--hidden-import=customtkinter',
        ]
        
        # Add icon if available
        if icon_path:
            pyinstaller_args.extend(['--icon', icon_path])
        
        # Add data files
        pyinstaller_args.extend(['--add-data', f'app{os.pathsep}app'])
        
        # Run PyInstaller
        PyInstaller.__main__.run(pyinstaller_args)
        
        print("\nBuild completed successfully!")
        
        # Verify the executable was created
        exe_path = Path('dist/ExcelProcessor.exe')
        if exe_path.exists():
            print(f"\nExecutable size: {exe_path.stat().st_size / (1024*1024):.2f} MB")
            print(f"Executable location: {exe_path.absolute()}")
        else:
            print("\nWarning: Executable file not found in expected location")
        
    except Exception as e:
        print(f"\nError during build process: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    build_executable()
