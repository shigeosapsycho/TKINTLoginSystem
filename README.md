# TKINTLoginSystem

## 📄 Project Overview
``TKINTLoginSystem`` is a graphical user interface (GUI) login system built using Python and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). It simulates a login interface with features like:
- Username and password validation from a GitHub-hosted text file.
- "Remember Me" functionality for user convenience.
- A clean and simple user interface with custom widgets.

## ✨Features
- Dark Theme: Built with CustomTkinter to provide a modern dark appearance.
- Username/Password Authentication: Fetches credentials from GitHub for validation.
- "Remember Me" Option: Offers the ability to save the username for convenience.
- Cross-Platform Compatibility: Designed to run on Windows, Linux, and MacOS with minor tweaks.

### 🖼️ Screenshots
#### Login Screen
![Login Screen](https://owo.oooooooooooooo.ooo/i/x1zm6nbu.png)

#### Message Boxes
![Message Box](https://owo.oooooooooooooo.ooo/i/q18yc1qy.png)
![Login Successesful](https://owo.oooooooooooooo.ooo/i/m6zzy738.png)
![Fill in all fields](https://owo.oooooooooooooo.ooo/i/iqo2sx48.png)

### 🎥 Videos
#### Login was successful
![Login Example](https://owo.oooooooooooooo.ooo/i/gdnkevl4.gif)
#### You are required to fill in all fields
![Fill in fields](https://owo.oooooooooooooo.ooo/i/8uyh3u2y.gif)
#### Login was unsuccessful
![Login Unsuccessful](https://owo.oooooooooooooo.ooo/i/yo2qaqda.gif)
#### Remember me checkbox
![Remember Me](https://owo.oooooooooooooo.ooo/i/8p6x41kr.gif)

## ▶ Usage
After installing the required dependencies, you can run the application using:
```
python main.py
```

1. Enter your username and password to log in
2. You will receive a welcome screen if your credentials are correct.
3. Check the "Remember Me" box to save your username for future sessions.

## ⚙️ Technical Details
- **Code Structure:** The project is organized around the ``UserInterface`` class, which manages the GUI layout, event handling, and interaction logic
- **Login Logic:** The ``LogInService()`` method handles user authentication by fetching data from GitHub-hosted files. It fetches the .txt files and breaks them into lines and indices. The indices must match the username and password, and their lengths can not exceed one another.
- **Cross-Platform Challenges:** Special care was taken to address issues that arise due to differences in Windows and MacOS memory access policies

## 🐞 Known Issues
- **MacOS Memory Access:** On MacOS, the application might raise a "memory access" error. This is likely caused by how Python handles GUI memory allocation differently on MacOS. Running with high-level permissions may mitigate this.
- **Admin Rights Needed on Windows:** If using an IDE on Windows, run it as an administrator to avoid permission-related errors.

## 🙏 Acknowledgments
- **CustomTkinter Library:** I want to express my gratitude to the developers of CustomTkinter for providing a modern and user-friendly extension to Tkinter.
- **CTkMessagebox Library:** Another special thanks to the developers who made [CTkMessageboxes](https://github.com/Akascape/CTkMessagebox) possible.

## 📜 License
This project is licensed under The Unlicense - see the [LICENSE](https://github.com/shigeosapsycho/TKINTLoginSystem/blob/main/LICENSE) file for details.
