import tkinter as tk
import os
import importlib.util

MODULES_DIR = 'modules'

def run_module(module_name):
    module_path = os.path.join(MODULES_DIR, f"{module_name}.py")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, 'main'):
        module.main()
    else:
        print(f"No main() in {module_name}")

def list_modules():
    files = os.listdir(MODULES_DIR)
    return [f[:-3] for f in files if f.endswith('.py') and f != '__init__.py']

root = tk.Tk()
root.title("Module Menu")

tk.Label(root, text="Select a module to run:").pack(pady=10)

for module_name in list_modules():
    tk.Button(root, text=module_name, width=30,
              command=lambda mn=module_name: run_module(mn)).pack(pady=2)

root.mainloop()