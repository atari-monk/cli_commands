# Commands package

Let’s create a **commands package** that adds additional functionality to the CLI tool via `pip` installation. The commands package will follow the same modular design, enabling seamless integration with `cli_tool`.

---

### **Step 1: Create the Commands Package**

1. **Initialize the Commands Package**:
   Create a new directory for the commands package:

    ```bash
    mkdir cli_commands
    cd cli_commands
    git init
    ```

2. **Set Up the Project Structure**:
   Create the directory and file structure:

    ```bash
    mkdir -p cli_commands
    touch cli_commands/__init__.py cli_commands/custom_commands.py
    touch README.md setup.py pyproject.toml requirements.txt .gitignore
    ```

    Your structure will look like this:

    ```
    cli_commands/
    ├── cli_commands/
    │   ├── __init__.py
    │   ├── custom_commands.py
    ├── README.md
    ├── setup.py
    ├── pyproject.toml
    ├── requirements.txt
    └── .gitignore
    ```

3. **Add a Custom Command**:
   In `cli_commands/custom_commands.py`, define a `load()` function to provide commands:

    ```python
    # custom_commands.py

    def load():
        print("custom_commands.load() called")

        def greet():
            print("Hello from the custom commands package!")

        return {
            "greet": greet,
        }
    ```

---

### **Step 2: Configure the Package**

1. **Set Up `setup.py`**:
   Define the package metadata and entry points in `setup.py`:

    ```python
    from setuptools import setup, find_packages

    setup(
        name="cli_commands",
        version="0.1.0",
        packages=find_packages(),
        entry_points={
            "cli_tool.commands": [
                "custom_commands = cli_commands.custom_commands:load",
            ],
        },
        install_requires=[],
        description="A custom commands package for CLI Tool",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        author="atari monk",
        author_email="atari.monk1@gmail.com",
        url="https://github.com/atari-monk/cli_commands",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
        ],
        python_requires=">=3.12.0",
    )
    ```

2. **Set Up `pyproject.toml`**:
   Create a `pyproject.toml` file to define the build system:
    ```toml
    [build-system]
    requires = ["setuptools>=64", "wheel"]
    build-backend = "setuptools.build_meta"
    ```

---

### **Step 3: Install the Commands Package**

1. **Build and Install the Package Locally**:
   From the `cli_commands` directory, run:

    ```bash
    pip install .
    ```

2. **Verify Installation**:
   Ensure the commands are installed by running the CLI tool (`cli_tool` from the previous setup) and typing `help`. The new command `greet` should appear.

---

### **Step 4: Test the Custom Commands**

1. **Run the CLI Tool**:
   Start the CLI tool:

    ```bash
    cli_tool
    ```

2. **Test the New Command**:
   Enter the `greet` command in the CLI:
    ```
    cli_app> greet
    Hello from the custom commands package!
    ```

---

### **Step 5: Publish the Commands Package**

1. **Prepare the Package**:
   Create a distribution for the commands package:

    ```bash
    python setup.py sdist bdist_wheel
    ```

2. **Upload to PyPI**:
   Use `twine` to upload the package to PyPI:

    ```bash
    pip install twine
    twine upload dist/*
    ```

3. **Install from PyPI**:
   Once published, the package can be installed via `pip`:
    ```bash
    pip install cli_commands
    ```

---

### **Optional: Add More Commands**

To add additional commands:

1. Define them in `cli_commands/custom_commands.py`.
2. Return them in the `load()` function.

For example:

```python
def load():
    def greet():
        print("Hello from the custom commands package!")

    def farewell():
        print("Goodbye from the custom commands package!")

    return {
        "greet": greet,
        "farewell": farewell,
    }
```

---

This setup enables you to extend the functionality of `cli_tool` dynamically by creating, installing, and managing modular command packages!
