import pickle

with open("model.pkl", 'wb') as p:
    pickle.dump(rfr,p)