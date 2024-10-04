import customtkinter
import requests
from CTkMessagebox import CTkMessagebox

class UserInterface:
    def __init__(self):
        # Set appearance and theme
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        
        # Create main window
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.root.title("Login System")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)
        
        # Variable to remember the username if the username box is checked
        self.remembered_username = None
        
        self.create_ui()
        
        self.root.mainloop()

    def create_ui(self):
        # Create frame inside the main window
        self.frame = customtkinter.CTkFrame(master=self.root) 
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Create label for the login system
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login System", font=("Impact", 24))
        self.label.pack(padx=10, pady=12)

        # Create entry for username
        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        if self.remembered_username:
            self.entry1.insert(0, self.remembered_username)
        self.entry1.pack(pady=12, padx=10)

        # Create entry for password
        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.entry2.bind("<Return>", self.password_shortcut)
        self.entry2.pack(pady=12, padx=10)

        # Create login button
        self.button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.LogInService)
        self.button.pack(pady=12, padx=10)

        # Create "Remember me" checkbox
        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Remember me")
        self.checkbox.pack(pady=12, padx=10)
        
    def LogInService(self):
        # Get the username and password input from the user
        self.username = self.entry1.get().strip()
        self.password = self.entry2.get().strip()

        try:
            # Fetch usernames and passwords from GitHub
            usernames_response = requests.get('https://raw.githubusercontent.com/shigeosapsycho/csulbeetcode/refs/heads/main/tkinter/5%20-%20sample%20login%20system/usernames.txt')
            passwords_response = requests.get('https://raw.githubusercontent.com/shigeosapsycho/csulbeetcode/refs/heads/main/tkinter/5%20-%20sample%20login%20system/passwords.txt')

            # Check if responses were successful
            if usernames_response.status_code == 200 and passwords_response.status_code == 200:
                usernames = usernames_response.text.splitlines()
                passwords = passwords_response.text.splitlines()

                # Ensure the files have the same number of lines
                if len(usernames) != len(passwords):
                    print("Error: Username and password files do not match in length.")
                    return

                # Check if the provided credentials are correct
                for i in range(len(usernames)):
                    if self.username == usernames[i] and self.password == passwords[i]:
                        CTkMessagebox(title="Login Successful", message="Login successful")
                        if self.checkbox.get():
                            self.remembered_username = self.username
                        else:
                            self.remembered_username = None
                        self.next_scene()
                        return
                
                # If no match is found
                CTkMessagebox(title="Login Failed", message="Invalid username or password")
            else:
                print("Error fetching usernames or passwords from GitHub")

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

    def password_shortcut(self, event):
        if event.keysym == "Return":
            self.LogInService()

    def next_scene(self, width = 250, height = 150):
        self.frame.destroy()
        
        self.frame = customtkinter.CTkFrame(master=self.root, width=width, height=height)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Welcome", font=("Impact", 24))
        self.label.pack(padx=10, pady=12)

        self.button = customtkinter.CTkButton(master=self.frame, text="Logout", command=self.logout)
        self.button.pack(pady=12, padx=10)

        self.root.geometry(f"{width}x{height}")
        
    def logout(self):
        self.frame.destroy()
        
        self.root.geometry("500x350")
        self.create_ui()

# Initialize the interface
UserInterface()


# TODO:
# if null reject login
# if check mark for remember me is checked, always keep it checked
# self.check_state.set(1) no matter what after login and logout