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
        
        # Initalize variables
        self.remembered_username = None
        self.checkbox_state = False
        
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
        if self.checkbox_state:
            self.checkbox.select()
        self.checkbox.pack(pady=12, padx=10)
        
    def LogInService(self):
        # Get the username and password input from the user
        self.username = self.entry1.get().strip().lower()
        self.password = self.entry2.get().strip()

        try:
            if self.username == "" or self.password == "":
                CTkMessagebox(title="Fill in all fields", message="Please fill in all fields")
                return
            else:
                # Fetch usernames and passwords from GitHub
                usernames_response = requests.get('https://raw.githubusercontent.com/shigeosapsycho/TKINTLoginSystem/refs/heads/main/usernames.txt')
                passwords_response = requests.get('https://raw.githubusercontent.com/shigeosapsycho/TKINTLoginSystem/refs/heads/main/passwords.txt')
                # Check if the responses were successful
                if usernames_response.status_code == 200 and passwords_response.status_code == 200:
                    usernames = usernames_response.text.splitlines()
                    passwords = passwords_response.text.splitlines()
                    
                    # Ensure that the usernames and passwords are of the same length
                    if len(usernames) != len(passwords):
                        print("Error: Username and password files do not match in length.")
                        return
                    # Check if the username and password match
                    for i in range(len(usernames)):
                        if self.username == usernames[i] and self.password == passwords[i]:
                            CTkMessagebox(title="Login Successful", message="Login successful")
                            if self.checkbox.get():
                                self.remembered_username = self.username
                                self.checkbox_state = True
                            else:
                                self.remembered_username = None
                                self.checkbox_state = False
                            self.root.after(100, self.next_scene)
                            return
                    # If no match is found, display an error message
                    CTkMessagebox(title="Login Failed", message="Invalid username or password")
                else:
                    print("Error fetching usernames or passwords from GitHub")

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

    def password_shortcut(self, event):
        if event.keysym == "Return":
            self.LogInService()

    def next_scene(self, width=250, height=150):
        if self.frame is not None:
            self.frame.pack_forget() # Remove the frame from the window so that it can be destroyed and not cause an error
            self.frame.destroy()

        self.frame = customtkinter.CTkFrame(master=self.root, width=width, height=height)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Welcome", font=("Impact", 24))
        self.label.pack(padx=10, pady=12)

        self.button = customtkinter.CTkButton(master=self.frame, text="Logout", command=self.logout)
        self.button.pack(pady=12, padx=10)

        self.root.geometry(f"{width}x{height}")

    def logout(self):
        if self.frame is not None:
            self.frame.pack_forget()
            self.frame.destroy()

        self.root.geometry("500x350")
        self.create_ui()


# Initialize the interface
UserInterface()