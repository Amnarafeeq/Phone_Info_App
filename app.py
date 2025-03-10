# ye glowing ha
import streamlit as st
import phonenumbers
from phonenumbers import timezone, geocoder, carrier, region_code_for_number
import pytz
import datetime
import random

# Set Page Config
st.set_page_config(page_title="Advanced Phone Info", page_icon="📞", layout="centered")

# Custom CSS for Cyberpunk Look with Left-Aligned Text
st.markdown(
    """
    <style>
        .stApp {
            background-color: #000000;
            color: #FFFFFF;
        }
        label {
            color: #00E5FF !important;
            font-weight: bold;
            font-size: 16px;
            text-shadow: 0px 0px 10px #00E5FF;
            text-align: left !important;
            display: block;
        }
        .stTextInput > div > div > input {
            background-color: #000000;
            color: #FFFFFF;
            border: 2px solid #FF9100;
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
            text-align: left !important;
        }
        .stButton > button {
            background: linear-gradient(90deg, #00E5FF, #FF9100);
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            transition: 0.3s;
            text-align: left !important;
            display: block;
        }
        .stButton > button:hover {
            transform: scale(1.1);
            box-shadow: 0px 0px 15px #FF9100;
            color:white;
        }
        .stButton > button:focus{
             color:white !important;
        }
        .glow-text {
            text-shadow: 0px 0px 15px #00E5FF;
            text-align: center !important;
        }
        .glowing-box {
            animation: glow 3s infinite alternate;
            padding: 20px;
            border-radius: 15px;
            text-align: left !important;
            display: block;
            margin-bottom:30px;
            box-shadow: 0 0 10px #00E5FF, 0 0 20px #FF9100
        }
         .stAlert {
            background-color: #111 !important; /* Dark Background */
            border-left: 5px solid #00E5FF !important; /* Neon Cyan Border */
            color: #FFFFFF !important; /* White Text */
            font-size: 18px !important;
            font-weight: bold !important;
            padding: 15px !important;
            margin: 30px !important;
            text-shadow: 0px 0px 10px #00E5FF;
            text-align:center !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='glow-text'>📞 Advanced Phone Number Info</h1>", unsafe_allow_html=True)

number = st.text_input("Enter your number with country code (e.g., +923001234567):")

# Function to predict number type (AI-like fun feature)
def predict_number_type(phone):
    if phone.startswith("+1") or phone.startswith("+44") or phone.startswith("+61"):
        return "📞 Business Number (Mostly Used for Official Work)"
    elif phone.startswith("+92") or phone.startswith("+91"):
        return "📱 Personal Number (Mostly Used for Social & Daily Use)"
    elif "000" in phone:
        return "⚠️ High Risk! Possible Spam or Fake Number"
    else:
        return "🔍 Unknown Type (Could be Personal or Business)"

# Function to get a random fun phone fact
def get_random_fact():
    facts = [
        "📌 The first mobile phone call was made in 1973!",
        "📌 The world’s most expensive phone number sold for $2.7 million!",
        "📌 China has the most mobile phone users in the world!",
        "📌 The first-ever SMS was sent in 1992 and it said 'Merry Christmas'!",
        "📌 The Nokia 1100 was the best-selling phone in history!"
    ]
    return random.choice(facts)

if st.button("Find Details"):
    if number:
        try:
            phone = phonenumbers.parse(number)

            if not phonenumbers.is_valid_number(phone):
                st.error("❌ Invalid phone number! Please check the format.")
            else:
                time_zones = timezone.time_zones_for_number(phone)
                car = carrier.name_for_number(phone, "en")
                reg = geocoder.description_for_number(phone, "en")
                country_code = region_code_for_number(phone)
                
                country_flag = f":flag-{country_code.lower()}:" if country_code else "🏳️"

                try:
                    tz = pytz.timezone(time_zones[0])
                    local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                except:
                    local_time = "Time Zone Not Available"

                number_type = predict_number_type(number)

                phone_fact = get_random_fact()

                st.markdown("<div class='stAlert'>✅ <b>Phone Number Details</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='glowing-box'>📞 **Parsed Number:** {phone} </div>", unsafe_allow_html=True)
                st.markdown(f"<div class='glowing-box'>{country_flag} **Country Code:** {country_code}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='glowing-box'>⏳ **Timezone:** {', '.join(time_zones)}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='glowing-box'>⏰ **Current Time in Region:** {local_time}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='glowing-box'>📡 **Carrier:** {car if car else 'Not Available'}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='glowing-box'>📍 **Region:** {reg if reg else 'Not Available'}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='glowing-box'>🤖 **AI Prediction:** {number_type}</div>", unsafe_allow_html=True)
                
                st.markdown(f"<div class='glowing-box'>💡 **Did You Know?** {phone_fact}</div>", unsafe_allow_html=True)

        except phonenumbers.NumberParseException:
            st.error("❌ Invalid phone number format! Make sure to include '+' and country code.")
    else:
        st.warning("⚠️ Please enter a phone number before clicking the button.")
