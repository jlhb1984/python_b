class Joins:    

    def __init__(self,df01,df02):
        self.df01=df01
        self.df02=df02
    
    def joins_df(df01,df02):
        print("df01:")
        print(df01)
        print("\ndf02:")
        print(df02)
        print("\n")      
        inner_join=df01.join(df02,how='inner')
        print("Inner join: ")
        print(inner_join)
        outer_join=df01.join(df02,how='outer')
        print("\nOuter join: ")
        print(outer_join)        