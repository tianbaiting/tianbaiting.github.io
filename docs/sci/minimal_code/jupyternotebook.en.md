---
title: Jupyter Notebook
tag:
    - ipynb
    - jupyter
---

## Programming Languages Supported by Jupyter Notebook

Jupyter Notebook, formerly known as IPython Notebook, has expanded to support multiple programming languages, including but not limited to:

- Python
- R
- Julia
- Scala
- Ruby
- JavaScript
- Bash
- C++
- Go
- Kotlin

This multi-language support makes Jupyter Notebook a powerful tool in data science, machine learning, and education.

## Installing Jupyter Notebook

It is recommended to install Jupyter Notebook using pip. Run the following command in the terminal:
```bash
pip install jupyter metakernel
```

After installation, test if it works correctly by running:
```bash
jupyter-notebook
```

If using ROOT, add the following to your `.bashrc` file in your home directory:
```bash
source (pathof)thisroot.sh
```

Then, navigate to your project directory and run:
```bash
root --notebook
```

## Steps to Add a Kernel

To add a new kernel in Jupyter Notebook, follow these steps:

1. **Install the Required Programming Language Environment**  
   Ensure the runtime environment for the target programming language is installed, such as Python, R, or Julia.

2. **Install the Jupyter Kernel**  
   Install the corresponding Jupyter kernel for the target language. For example:  
   - For Python, use `ipykernel`:  
     ```bash
     pip install ipykernel
     ```  
   - For R, use `IRkernel`:  
     ```R
     install.packages("IRkernel")
     IRkernel::installspec()
     ```  
   - For Julia, use `IJulia`:  
     ```julia
     using Pkg
     Pkg.add("IJulia")
     ```  
   - For C#, use `dotnet-interactive`:  
     ```bash
     dotnet tool install -g Microsoft.dotnet-interactive
     dotnet interactive jupyter install
     ```  
     Or `clingkernel`:  
     ```bash
     pip install clingkernel
     clingkernel install --sys-prefix
     ```

3. **Register the Kernel**  
   After installation, the kernel should automatically register with Jupyter Notebook. If not, you can manually register it using a command like:
   ```bash
   python -m ipykernel install --user --name=my_kernel_name
   ```

4. **Launch Jupyter Notebook**  
   Start Jupyter Notebook and select the newly added kernel when creating a new file.

By following these steps, you can add and use new kernels in Jupyter Notebook to support additional programming languages.

## Running Bash Scripts in Jupyter Notebook

You can run Bash scripts in Jupyter Notebook using the following methods:

1. **Using the `!` Command**  
   Run Bash commands or scripts directly in a code cell using `!`. For example:
   ```bash
   !sh script.sh
   ```

2. **Using the `subprocess` Module**  
   Use the `subprocess` module in Python to run Bash scripts. For example:
   ```python
   import subprocess
   subprocess.run(['sh', 'script.sh'])
   ```

3. **Using the `%%bash` Magic Command**  
   Use the `%%bash` magic command in a code cell to run Bash scripts. For example:
   ```bash
   %%bash
   # Bash script content
   sh script.sh
   ```

These methods allow you to easily run Bash scripts in Jupyter Notebook and interact with system commands.

## Using ROOT in Jupyter Notebook

[jupyroot](https://github.com/root-project/root/tree/master/bindings/jupyroot)

1. [Install ROOT6](https://root.cern.ch/building-root) (> 6.05)
2. Install dependencies: `pip install jupyter metakernel`

### Start Using ROOTbooks
Set up the ROOT environment (`. $ROOTSYS/bin/thisroot.[c]sh`) and type in your shell:
```shell
root --notebook
```
This will start a ROOT-flavored notebook server on your computer.

Alternatively, to use the Jupyter command directly:
```shell
jupyter kernelspec install $ROOTSYS/etc/root/notebook/kernels/root --user
```

Once the server is running, you can use ROOT with two kernels:

1. ROOT C++: A new kernel provided by ROOT.
2. Python: Already provided by Jupyter.

### C++ ROOTbook
ROOT offers a C++ kernel that transforms the notebook into a ROOT prompt. Features include embedded graphics, syntax highlighting, and tab completion.

Example of plotting a histogram in a C++ ROOTbook:
```cpp
TCanvas c;
TH1F h("h","ROOT Histo;X;Y",64,-4,4);
h.FillRandom("gaus");
h.Draw();
c.Draw();
```

### Python ROOTbook
To use Python, create a new Python kernel and import the ROOT libraries:
```python
import ROOT
```
Example:
```python
c = ROOT.TCanvas("c")
h = ROOT.TH1F("h","ROOT Histo;X;Y",64,-4,4)
```
You can also mix Python and C++ in the same notebook using the **%%cpp** magic:
```cpp
%%cpp
h->FillRandom("gaus");
h->Draw();
c->Draw();
```

## ipyplot

```python
video_paths = ["my_video.mp4"]
video_labels = ["My Video"]
ipyplot.plot_videos(video_paths, video_labels, width=320)
```

```python
import matplotlib.pyplot as plt
import numpy as np
import ipyplot
import tempfile
import os

# 1. Use matplotlib to create a plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Matplotlib Plot")

# 2. Save the matplotlib plot to a temporary file
with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
    temp_filename = tmp_file.name
    plt.savefig(temp_filename)

# 3. Display the temporary image file using ipyplot
ipyplot.plot_images([temp_filename], ["Matplotlib Plot"], img_width=400)

# 4. Clean up the temporary file
os.remove(temp_filename)
```
