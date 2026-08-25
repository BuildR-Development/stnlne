import random
import time
import os
import platform

def typewrite(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

os.system("cls" if os.name == "nt" else "clear")

system_names = [
    "NEXUS",
    "STNLNE",
    "BUILD-R",
    "VOID",
    "ORBIT",
    "CASCADE",
    "MIRAGE"
]

modules = [
    "Memory Controller",
    "Audio Subsystem",
    "Graphics Pipeline",
    "Network Interface",
    "Temporal Engine",
    "Filesystem",
    "Reality Renderer"
]

name = random.choice(system_names)

typewrite("INITIALIZING...")
time.sleep(0.4)

typewrite(f"System designation: {name}")
typewrite(f"Host OS: {platform.system()} {platform.release()}")
typewrite(f"Architecture: {platform.machine()}")
print()

for module in modules:
    time.sleep(random.uniform(0.1, 0.4))

    status = random.choices(
        ["OK", "OK", "OK", "WARN"],
        weights=[40, 30, 20, 10]
    )[0]

    print(f"[{status:4}] {module}")

print()
time.sleep(0.5)

messages = [
    "No anomalies detected.",
    "Everything appears normal.",
    "System integrity verified.",
    "All modules responding.",
    "Nothing unusual detected."
]

typewrite(random.choice(messages))
print()

time.sleep(0.8)
typewrite(f"\nWelcome to {name}.")
