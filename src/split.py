from sklearn.model_selection import train_test_split

def train_test_val_split(df,ratio_train,ratio_test,ratio_val):
    train, middle = train_test_split(df,test_size=1-ratio_train)
    ratio=ratio_val/(1-ratio_train)
    test,validation =train_test_split(middle,test_size=ratio)
    return train,test,validation

train,test,val=train_test_val_split(df,0.6,0.2,0.2)