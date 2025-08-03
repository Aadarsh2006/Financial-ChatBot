# **Financial Chatbot Prototype**



This project is a simple financial chatbot prototype designed to respond to predefined financial queries for Apple, Microsoft, and Tesla using real financial data extracted from their 10-K filings (last 3 fiscal years).



### **Project Structure**



Book1.csv — Financial data file (manually extracted from 10-K reports)



chatbot.py — Python script containing chatbot logic



README.md — Project documentation



Book1\_DataAnalysis.py - Data analysis and sorting by python





### **Technologies Used**



Python 3



pandas for data handling



Command-line interface (input function)





### **What It Can Do ?**



This chatbot can answer the following predefined queries:



1\. What is the total revenue of \[Company]?



2\. What is the net income of \[Company]?



3\. What are the total assets of \[Company]?



4\. What are the total liabilities of \[Company]?



5\. What is the operating cash flow of \[Company]?





You can replace \[Company] with Apple, Microsoft, or Tesla. The chatbot is not case sensitive.







### **How It Works**



Loads data from Book1.csv



Cleans and standardizes input and data



Uses if-elif statements to match user queries



Returns financial data as responses





**Example Queries**



You: What is the total revenue of Apple?

Bot: Total revenue for Apple:

\[394.33, 365.82, 274.51]



You: Tell me net income of Tesla

Bot: Net income for Tesla:

\[12.58, 5.52, 0.721]







### **How to Run ?**



1\. Make sure you have Python and pandas installed.



2\. Place your Book1.csv file in the same folder as chatbot.py.



3\. Run the chatbot script using terminal or IDLE:



python chatbot.py



4\. Type your queries in the terminal.



5\. To exit the chatbot, type: exit







### **Limitations**



Only responds to predefined queries.



Only works with Apple, Microsoft, and Tesla.



No natural language processing or AI is used.



Assumes Book1.csv is properly formatted and located at the correct path.





### **Future Ideas**



Add a Flask-based web interface



Use NLP models for smarter query handling



Connect to live financial APIs for real-time data

