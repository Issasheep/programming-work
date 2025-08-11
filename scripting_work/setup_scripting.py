import subprocess

try:
    """
    # Open Firefox and search Google for "python subprocess"
    subprocess.run([
        r'C:\\Program Files\\Mozilla Firefox\\firefox.exe', "https://habitica.com/"
    ], check=True)
    """
    subprocess.call("C:\\Program Files\\obs-studio\\bin\64bit\\obs64.exe")
    subprocess.call("C:\\WINDOWS\\system32\\cmd.exe")
    subprocess.run(["C:\\WINDOWS\\system32\\cmd.exe"], check=True)

except PermissionError:
    print("Error: Permission denied. Try running the script with elevated privileges.")

except FileNotFoundError:
    """
    subprocess.run([
        r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe", "https://habitica.com/"
    ])
    """

except subprocess.CalledProcessError as e:
    print(f"Error running command: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Note: Ensure that the paths to Firefox and OBS Studio are correct for your system.
# If you have different paths, update them accordingly.

