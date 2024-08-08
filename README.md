# Llama-Lit

Llama-Lit is a streamlit page providing a front-end to interact with the Llama model. \
This is still in development and needs some adjustment to offer a good user experience. \
\
The backend was made using the [ollama](https://github.com/ollama/ollama-python) library. \
Please keep in mind, that this module uses the first module listed when executing the function ```ollama.list()``` from the library itself. \
Meaning, it is not guaranteed to use a Llama model. \
\
The frontend was made with [streamlit](https://streamlit.io). \
If one wants to host this application themselves, they would need to install all [requirements](https://github.com/Simoso68/llama-lit/blob/main/requirements.txt) and run the script via ```streamlit run app.py```.

## Using it

As this software is not available on the community cloud, one needs it to run on their own machine.

### Software needed

- [Python](https://www.python.org)
- [Ollama](https://ollama.com)
- [Git](https://git-scm.com)

### Instructions

**1. Install the AI model**

```sh
ollama pull llama3.1:latest
```

> [!NOTE]
> Always check for the newest model to install.

**2. Install the required packages**

```sh
pip install streamlit ollama
```

> [IMPORTANT]
> On Windows systems, pip comes automatically with python. \ On other systems such as the Linux family of systems, you need to install pip seperately.

**3. Download this repository**

Locate using the ```cd``` command to the parent folder, where the llama-lit folder with all the code should be stored at. \
Then execute the following command, to clone the repository onto your file system.

```sh
git clone https://github.com/Simoso68/llama-lit.git
```

After this, a new folder named 'llama-lit' should have been created in the parent directory, that you chose.

**4. Locate into the llama-lit directory**

After successfully cloning llama-lit onto your device, one should be able to locate into this folder from the chosen parent folder using:

```sh
cd llama-lit
```

**5. Running Llama-Lit**

From the llama-lit directory, you can just run the following command, to make the application start:

```sh
streamlit run app.py
```

### Installation complete.

Now, you should have a functioning copy of llama-lit. \
To start llama-lit in the future, locate into your llama-lit directory and run the same command as in step 5 of the installation. \
To stop the application, hit ```CTRL``` and ```C``` while you are in your terminal to shut it down.