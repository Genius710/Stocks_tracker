# Stocks_tracker
An experiment to build a stock price tracker for stocks traded in Revolut. The goal is to build an alarma system to notify me of stocks which are on a rise for a specified time frame.

The project consists of 3 main files:
1. Reader script, this script takes input of a csv file with a list of stock tickers to check. 
Output is a pandas array stored in memory consisting of extracted data.
2. Analizer script, this script takes the array loaded in memory from the 'Reader.py' script, ending day of test period, test period lenght.
Output is a list of stock tickers which should growth during all days of the test period.
3. Historical tester script.
The purpose of this script is to test the methods of selection used in analizer script. It takes a time period in the past and checks if the stocks previously selected have performed positvely in the future.
