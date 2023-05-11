import joblib
import sys
import pickle

def get_prediction_from_url(test_url):
    # Loading the vector and RF model    
    vectorizer = pickle.load(open('vector/vector_phish.pickle','rb'))    
    clf = joblib.load('classifier/random_forest_phishTank.pkl') 

    # Extracting features of the url
    features_test = vectorizer.transform([test_url]) 

    # Predicting the result using the loaded RF model   
    pred = clf.predict(features_test)
    return int(pred[0])

def main(arg):   
    url = arg

    # Calling the get_prediction_from_url() function
    prediction = get_prediction_from_url(url)  

    # Printing the message based on the result obtained
    if prediction == 0:        
        print("SAFE")
    elif prediction ==1:        
        print("PHISHING")

if __name__ == "__main__":
    main(sys.argv[1])







    