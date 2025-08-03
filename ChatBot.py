import pandas as pd

# Load the financial data
df = pd.read_csv("C:\\Users\\Aadarsh\\Desktop\\Book1.csv")

# Convert company names and columns to lowercase for consistency
df['company'] = df['company'].str.lower()
df.columns = [col.lower() for col in df.columns]

# Chatbot function
def simple_chatbot(user_query):
    user_query = user_query.lower()

    if "exit" in user_query:
        return "Exiting chatbot. Goodbye!"

    if "apple" in user_query:
        company = "apple"
    elif "microsoft" in user_query:
        company = "microsoft"
    elif "tesla" in user_query:
        company = "tesla"
    else:
        return "❌ Please mention a valid company name (Apple, Microsoft, Tesla)."

    company_data = df[df['company'] == company]

    if "total revenue" in user_query:
        return f"📊 Total revenue for {company.title()}:\n{company_data['total revenue'].values}"
    
    elif "net income" in user_query:
        return f"💰 Net income for {company.title()}:\n{company_data['net income'].values}"
    
    elif "total assets" in user_query:
        return f"🏢 Total assets for {company.title()}:\n{company_data['total assets'].values}"
    
    elif "total liabilities" in user_query:
        return f"📉 Total liabilities for {company.title()}:\n{company_data['total liabilities'].values}"
    
    elif "operating cash flow" in user_query or "cash flow from operations" in user_query:
        return f"💵 Operating cash flow for {company.title()}:\n{company_data['operating cash flow'].values}"
    
    else:
        return "❌ Sorry, I can only answer predefined questions about revenue, net income, assets, liabilities, or operating cash flow."

# Run chatbot in loop
print("🧠 Welcome to the Financial Chatbot (Type 'exit' to quit)")
while True:
    user_input = input("\nYou: ")
    response = simple_chatbot(user_input)
    print("Bot:", response)
    if "exit" in user_input.lower():
        break
