import streamlit as st
import africastalking


username = "simalert"  # Replace with your Africa's Talking username
api_key = "atsk_f9dfcfd1e127a88bcf97eb6a16081e0e74585e49df6032e5fc41daf4e7a771105b73ad00"  # Replace with your Africa's Talking API key
africastalking.initialize(username, api_key)

# Get the Airtime service
airtime = africastalking.Airtime

def send_airtime(phone_number, amount, currency_code="TZS"):
    """
    Sends airtime to a phone number.

    :param phone_number: Recipient's phone number (e.g., +255711XXXYYY)
    :param amount: Amount of airtime to send
    :param currency_code: Currency code (e.g., TZS)
    """
    try:
        response = airtime.send(recipients=[{
            "phoneNumber": phone_number,
            "currencyCode": currency_code,
            "amount": amount
        }])
        return response
    except Exception as e:
        return str(e)

# Streamlit App
st.title("Survey and Reward App")

# Collect user phone number
phone_number = st.text_input("Enter your phone number (e.g., +255694021848):")

# Survey questions
st.subheader("Survey Questions")
question_1 = st.radio("Do you like using mobile apps?", ["Yes", "No"])
question_2 = st.radio("Would you recommend this app to others?", ["Yes", "No"])

# Submit button
if st.button("Submit"):
    if phone_number:
        # Reward the user with 1 TZS
        reward_amount = 1  # Amount to send
        response = send_airtime(phone_number, reward_amount)
        if "errorMessage" not in response:
            st.success(f"Thank you for completing the survey! 1 TZS has been sent to {phone_number}.")
        else:
            st.error(f"Failed to send airtime: {response}")
    else:
        st.error("Please enter a valid phone number.")