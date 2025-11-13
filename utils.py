import os
import pandas as pd

def save_uploaded_file(uploaded_file, folder_path):
    """
    Save the uploaded file to the specified folder and return the full path.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def read_file_content(file_path):
    """
    Read the content of a TXT or CSV file and return as a string.
    """
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    elif ext == ".csv":
        try:
            df = pd.read_csv(file_path)
            # Convert dataframe to a readable string
            content = df.to_string(index=False)
            return content
        except Exception as e:
            return f"Error reading CSV: {str(e)}"

    else:
        return f"Unsupported file type: {ext}"
