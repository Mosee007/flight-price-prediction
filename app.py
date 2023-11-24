from types import MethodDescriptorType
from flask import Flask, request, render_template, session, redirect, url_for
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "my-secret-key"
model = pickle.load(open("c1_flight_rf.pkl", "rb"))

@app.route('/logout')
def logout():
    # Remove the username from the session if it exists
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # TODO: Validate the username and password
        # If they are valid, store the username in the session and redirect to the home page
        # Otherwise, show an error message
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('login.html')


# Define the home route
@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        # current date and time 
        now = datetime.now()

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        dep_datetime = pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M")

        #check if the departure is inthe future

        if dep_datetime < now:
            return "Invalid departure time: Please enter the future date and time"
        
        #extract other feature from input 
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)
        

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']
        if(airline=='Jet Airways'):
            AirKenya_Express = 1
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Kenya_Airways'):
            AirKenya_Express = 0
            Kenya_Airways = 1
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0 

        elif (airline=='Fly540'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 1
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 1
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='Safarilink_Aviation'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 1
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0 
            
        elif (airline=='African_Express_Airways'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 1
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0

        elif (airline=='Airlink'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 1
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 1
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0

        elif (airline=='Jet Airways Business'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 1
            African_Express_Airways_Premium_economy = 0
            Trujet = 0

        elif (airline=='African_Express_Airways Premium economy'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 1
            Trujet = 0
            
        elif (airline=='Trujet'):
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 1

        else:
            AirKenya_Express = 0
            Kenya_Airways = 0
            Fly540 = 0
            Jambo_Jet = 0
            Safarilink_Aviation = 0
            African_Express_Airways = 0
            Airlink = 0
            Jambo_Jet_Premium_economy = 0
            AirKenya_Express_Business = 0
            African_Express_Airways_Premium_economy = 0
            Trujet = 0

        # print(AirKenya_Express,
        #     Kenya_Airways,
        #     Fly540,
        #     Jambo_Jet,
        #     Safarilink_Aviation,
        #     African_Express_Airways,
        #     Airlink,
        #     Jambo_Jet_Premium_economy,
        #     AirKenya_Express_Business,
        #     African_Express_Airways_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Machakos'):
            s_Machakos = 1
            s_Naivasha = 0
            s_Lowdar = 0
            s_Eldoret = 0

        elif (Source == 'Naivasha'):
            s_Machakos = 0
            s_Naivasha = 1
            s_Lowdar = 0
            s_Eldoret = 0

        elif (Source == 'Lowdar'):
            s_Machakos = 0
            s_Naivasha = 0
            s_Lowdar = 1
            s_Eldoret = 0

        elif (Source == 'Eldoret'):
            s_Machakos = 0
            s_Naivasha = 0
            s_Lowdar = 0
            s_Eldoret = 1

        else:
            s_Machakos = 0
            s_Naivasha = 0
            s_Lowdar = 0
            s_Eldoret = 0

        # print(s_Machakos,
        #     s_Naivasha,
        #     s_Lowdar,
        #     s_Eldoret)

        # Destination
        # Kisumu = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Mombasa'):
            d_Mombasa = 1
            d_Machakos = 0
            d_Nairobi = 0
            d_Nanyuki = 0
            d_Naivasha = 0
        
        elif (Source == 'Machakos'):
            d_Mombasa = 0
            d_Machakos = 1
            d_Nairobi = 0
            d_Nanyuki = 0
            d_Naivasha = 0

        elif (Source == 'Nairobi'):
            d_Mombasa = 0
            d_Machakos = 0
            d_Nairobi = 1
            d_Nanyuki = 0
            d_Naivasha = 0

        elif (Source == 'Nanyuki'):
            d_Mombasa = 0
            d_Machakos = 0
            d_Nairobi = 0
            d_Nanyuki = 1
            d_Naivasha = 0

        elif (Source == 'Naivasha'):
            d_Mombasa = 0
            d_Machakos = 0
            d_Nairobi = 0
            d_Nanyuki = 0
            d_Naivasha = 1

        else:
            d_Mombasa = 0
            d_Machakos = 0
            d_Nairobi = 0
            d_Nanyuki = 0
            d_Naivasha = 0

        # print(
        #     d_Mombasa,
        #     d_Machakos,
        #     d_Nairobi,
        #     d_Nanyuki,
        #     d_Naivasha
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_Airlink', 'Airline_Kenya_Airways',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_Safarilink_Aviation',
    #    'Airline_Trujet', 'Airline_African_Express_Airways', 'Airline_African_Express_Airways Premium economy',
    #    'Source_Eldoret', 'Source_Machakos', 'Source_Naivasha', 'Source_Lowdar',
    #    'Destination_Mombasa', 'Destination_Machakos', 'Destination_Nanyuki',
    #    'Destination_Naivasha', 'Destination_New Machakos']
        #if (Source ==)
        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Fly540,
            Airlink,
            Kenya_Airways,
            AirKenya_Express,
            AirKenya_Express_Business,
            Jambo_Jet,
            Jambo_Jet_Premium_economy,
            Safarilink_Aviation,
            Trujet,
            African_Express_Airways,
            African_Express_Airways_Premium_economy,
            s_Eldoret,
            s_Machakos,
            s_Naivasha,
            s_Lowdar,
            d_Mombasa,
            d_Machakos,
            d_Nanyuki,
            d_Naivasha,
            d_Nairobi
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price in Ksh. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
