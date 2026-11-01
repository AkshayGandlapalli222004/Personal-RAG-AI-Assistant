from pathlib import Path
from typing import List, Tuple, Any
from langchain_community.document_loaders import PyMuPDFLoader, PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader


def load_all_documents(data_dir: str) -> List[Any]:
    """Load all Supported files frrom the data directory and convert them into Langchain Dcument Structure
    Supports: PDF, TXT, CSV, EXCEL, WORD, JSON
    """

    #Use Project root data folder

    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data Path: {data_path}")
    documents = []

    
    
    # PDF Files

    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] Found {len(pdf_files)} PDF Files: {[str(f) for f in pdf_files]}")

    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")

        try:
            loader = PyMuPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
            documents.extend(loaded)

        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file} : {e}")


    # TEXT Files

    txt_files = list(data_path.glob("**/*.txt"))
    print(f"[DEBUG] Found {len(txt_files)} TXT Files: {[str(i) for i in txt_files]}")


    for txt_file in txt_files:
        print(f"[DEBUG] Loading TXT : {txt_file}")


        try:
            loader = TextLoader(str(txt_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} TXT documents from {txt_file}")
            documents.extend(loaded)

        except Exception as e:
            print(f"[ERROR] Failed to load TXT {txt_file} : {e}")




    #CSV Files

    csv_files = list(data_path.glob("**/*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV Files: {[str(i) for i in csv_files]}")


    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV : {csv_file}")

        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} CSV documents from {csv_file}")
            documents.extend(loaded)

        except Exception as e:
            print(f"[ERROR] Failed to load CSV {csv_file} : {e}")




    #SQL Files

    sql_files = list(data_path.glob("**/*.sql"))
    print(f"[DEBUG] Found {len(sql_files)} SQL Files: {[str(i) for i in sql_files]}")


    for sql_file in sql_files:
        print(f"[DEBUG] Loading SQL : {sql_file}")

        try:
            loader = TextLoader(str(sql_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} SQL documents from {sql_file}")
            documents.extend(loaded)

        except Exception as e:
            print(f"[ERROR] Failed to load SQL {sql_file} : {e}")

    
    
    return documents
