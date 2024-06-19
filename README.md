# Quick File Explorer
![version](https://img.shields.io/badge/Project_version-1.0.0-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![made with love](https://img.shields.io/badge/Made_with-Love-red)
 
Welcome to Quick File Explorer! This application allows you to explore your file system with a simple and intuitive graphical interface. Here's a step-by-step guide to help you navigate and use the various features of the application.

# Tutorial
## Run Locally
Clone the project

```
$ git clone https://github.com/anekobtw/file-explorer.git
```

Install dependencies

```bash
$ pip install -r requirements.txt
```

Run the program

```bash
$ python main.py
```

## Interface Overview
- Sidebar:
  - Located on the left side of the window.
  - Displays the application title, version, and appearance mode options.
  - Contains a button for accessing the tutorial.

- Main Frame:
  - Occupies the right side of the window.
  - Displays the contents of the selected directory or available drives.
  - Uses a scrollable frame to list files and folders.

## Navigation
- Drives:
    - When you first open the application, the main frame lists all available drives.
- Choosing a file or a folder:
    - Use the `Down` arrow key to move the selection down.
    - Use the `Up` arrow key to move the selection up.
    - The selected item will be highlighted in blue.
- Open Selected Item:
    - With keyboard:
        - Press the `Enter` key to open the selected file or folder.
        - Press the `o` button to open the current folder in Windows default explorer.
    - With mouse:
        - Click on a file to open it with the default application.
        - Click on a folder to view its contents.
- Go one directory back:
    - Press the `esc` key to go back to the previous directory.
    - If you're at the root directory, pressing `esc` will take you back to the drive selection screen.
- Open/Close Window:
    - Press `Win+Z` to toggle the visibility of the window.

## Example Usage
Here's an example of how to start using Quick File Explorer:

- Launch the Application:
```
python file_explorer.py
```

- **Select a Drive:**\
Click on a drive (e.g., C:/) to list its contents.

- **Navigate Folders:**\
Use the arrow keys or click on folders to navigate through the directory structure.

- **Open a File:**\
Select a file and press Enter to open it with the default application.

- **Change Appearance Mode:**\
Select a different appearance mode from the sidebar to see how the application looks in different themes.

- **Toggle Window Visibility:**\
Press Win+Z to hide or show the application window.

## Contributing
Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
## License
The project is [MIT](https://choosealicense.com/licenses/mit/) licensed
