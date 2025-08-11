import subprocess

try:
    # Open Firefox and search Google for "python subprocess"
    subprocess.run([
        r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
    ])

except FileNotFoundError:
    print("Error: Program not found. Ensure the executable is in your PATH or provide the full path.")

except subprocess.CalledProcessError as e:
    print(f"Error running command: {e}")