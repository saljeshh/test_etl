import pandas as pd 

def transform():
    
    
    data = [
        {
            "name": "Avengers",
            "Rating": "8",
            "id": "568754",
            "year": 2022,
            "hawa": 'ajfkadsjfioadwjfoiadsjf',
            "desc": " "
        },
        {
            "name": "Ragini MMS",
            "Rating": "3",
            "id": "39393",
            "year": 2018,
            "hawa": 'ruy 9ew8ruiadshfasdhfjadsnfkjnadkj',
            "desc": " "
        }
    ]
    
    # conver to df
    df=pd.DataFrame(data)
    print(df.head())
    print('====================================')
    
    # todo: change datatype 
    
    
    # drop unwanted columns
    df = df.drop(['hawa'], axis=1)
    
    
    # todo: Null handle 
    df["desc"] = "No description"
    
    
    return df


if __name__ == '__main__':
    df = transform()
    print(df.head())