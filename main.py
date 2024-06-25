from extract import extract
from transform import transform
from load import load 


def main():
    raw = extract()
    
    td = transform(raw)
    
    load(td)
    
    print("Success")