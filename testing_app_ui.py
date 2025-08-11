import tkinter as tk  # Import the tkinter library for GUI
import subprocess  # Import subprocess to run external commands
import json

# Create the main window
root = tk.Tk()
root.title("UI for different setups")  # Set the window title
root.geometry("1280x720")   # Set the window size (width x height)

def on_button_click_open_habbit_website():
    try:
        subprocess.Popen([
            r"C:\\Program Files\\Mozilla Firefox\\firefox.exe", "https://habitica.com/"])

    except FileNotFoundError:
        print("Error: Program not found. Ensure the executable is in your PATH or provide the full path.")

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def on_button_click_open_streaming_setup():
    try:
        subprocess.Popen([
            r"C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\Resolve.exe"])
        subprocess.Popen([
            r"C:\\Program Files\\Mozilla Firefox\\firefox.exe", "https://www.youtube.com/@issasheep"])
        subprocess.Popen([
            r"C:\\Program Files\\Mozilla Firefox\\firefox.exe", "https://ssvid.net/en"])
        subprocess.Popen([
            r"C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"], cwd=r"C:\Program Files\obs-studio\bin\64bit")
    except FileNotFoundError:
        print("Error: Program not found. Ensure the executable is in your PATH or provide the full path.")

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def on_button_click_job_application_setup():
    try:
        subprocess.Popen([
            r"C:\\Program Files\\Mozilla Firefox\\firefox.exe", "https://www.linkedin.com/jobs/"])
        subprocess.Popen([
            r"C:\\Program Files\\Mozilla Firefox\\firefox.exe", "https://au.indeed.com/"])
        subprocess.Popen([
            r"C:\\Program Files\\Mozilla Firefox\\firefox.exe", "https://www.seek.com.au/"])
    except FileNotFoundError:
        print("Error: Program not found. Ensure the executable is in your PATH or provide the full path.")

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def on_button_click_davinchi_resolve_open():
    try:
        subprocess.Popen([
            r"C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\Resolve.exe"])
    except FileNotFoundError:
        print("Error: Program not found. Ensure the executable is in your PATH or provide the full path.")

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Arial", 12), bg="lightblue", fg="black", padx=10, pady=5)


#class CustomButtonCreation(tk.Button):


setup = {
    "habbit_website": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "editing_setup": [
        r"C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe",
        r"C:\Program Files\Mozilla Firefox\firefox.exe https://www.youtube.com/@issasheep",
        r"C:\Program Files\Mozilla Firefox\firefox.exe https://ssvid.net/en",
        r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
    ],
    "job_application_setup": [
        r"C:\Program Files\Mozilla Firefox\firefox.exe https://www.linkedin.com/jobs/",
        r"C:\Program Files\Mozilla Firefox\firefox.exe https://au.indeed.com/",
        r"C:\Program Files\Mozilla Firefox\firefox.exe https://www.seek.com.au/"
    ]
}

with open ("setup.json", "w") as f:
    json.dump(setup, f, indent=4)

with open("setup.json", "r") as f:
    loaded_setup = json.load(f)




# Create a label widget and add it to the window
label = tk.Label(text="open habbit website")
label.grid(row=0, column=0, padx= 20, pady=20)  # Add some vertical padding

# Create a button widget and add it to the window
button = tk.Button(text="Click Me", command=on_button_click_open_habbit_website)
button.grid(row=1, column=0, padx=20, pady=10)  # Place button below the label

label = tk.Label(root, text="open editing setup")
label.grid(row=0, column=1, padx= 20, pady=20) 

button = tk.Button(root, text="Click Me", command=on_button_click_open_streaming_setup)
button.grid(row=1, column=1, padx=20, pady=10) 

label = tk.Label(root, text="job appplication setup")
label.grid(row=0, column=2, padx= 20, pady=20) 

button = tk.Button(root, text="Click Me", command=on_button_click_job_application_setup)
button.grid(row=1, column=2, padx=20, pady=10) 

label = tk.Label(root, text="davinchi resolve setup")
label.grid(row=0, column=4, padx= 20, pady=20) 

button = tk.Button(root, text="Click Me", command=on_button_click_davinchi_resolve_open)
button.grid(row=1, column=4, padx=20, pady=10) 



CustomButton = CustomButton(root, text="Custom Button")
CustomButton.grid(row=2, column=0, padx=20, pady=10)

# Start the GUI e
# 
# 
# vent loop (keeps the window open)
label = tk.Label(root, text="Enter your name:")
button.grid(row=0, column=6, padx=20, pady=10)

root.mainloop()


# Note: The above code assumes that the specified paths to the executables are correct.
# If the paths are incorrect, you will need to update them to match your system's configuration.
# Also, ensure that the required applications are installed on your system.