"""Script to add __init__.py files to all directories in the project."""

import os
from pathlib import Path


def should_skip_directory(dir_path: Path, root_dir: Path) -> bool:
    """
    Check if directory should be skipped.
    
    Args:
        dir_path: Path to the directory
        root_dir: Root directory of the project
        
    Returns:
        True if directory should be skipped, False otherwise
    """
    skip_patterns = [
        "__pycache__",
        ".git",
        ".venv",
        "venv",
        "env",
        ".env",
        "node_modules",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
    ]
    
    dir_name = dir_path.name
    
    if dir_name in skip_patterns:
        return True
    
    if dir_name.startswith("."):
        return True
    
    relative_path = dir_path.relative_to(root_dir)
    path_parts = relative_path.parts
    
    if ".git" in path_parts or ".venv" in path_parts or "venv" in path_parts:
        return True
    
    return False


def add_init_files(root_dir: Path) -> None:
    """
    Add __init__.py files to all directories that don't have them.
    
    Args:
        root_dir: Root directory to start scanning from
    """
    init_files_added = []
    
    for dir_path, dirs, files in os.walk(root_dir):
        dir_path_obj = Path(dir_path)
        
        if should_skip_directory(dir_path_obj, root_dir):
            continue
        
        init_file_path = dir_path_obj / "__init__.py"
        
        if not init_file_path.exists():
            init_file_path.touch()
            init_files_added.append(str(dir_path_obj.relative_to(root_dir)))
            print(f"Added: {init_file_path.relative_to(root_dir)}")
    
    if init_files_added:
        print(f"\nTotal __init__.py files added: {len(init_files_added)}")
    else:
        print("\nAll directories already have __init__.py files.")


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    print(f"Scanning project root: {project_root}")
    print("Adding __init__.py files to directories...\n")
    add_init_files(project_root)

