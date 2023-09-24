import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))


def predict_Phishing_Website(having_IP_Address,having_Sub_Domain,HTTPS_token,Submitting_to_email,Abnormal_URL,Redirect):
    input=np.array([[having_IP_Address,having_Sub_Domain,HTTPS_token,Submitting_to_email,Abnormal_URL,Redirect]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("Phishing Website")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Phishing Website Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    having_IP_Address = st.text_input("having_IP_Address  (Have IP = 1 or Not Having IP = -1)","Type Here")
    having_Sub_Domain = st.text_input("having_Sub_Domain  (Have subDomain = 1 or Not Having subDomain = -1 or Don't know = 0)","Type Here")
    HTTPS_token = st.text_input("HTTPS_token  (Have HTTPS_Token = 1 or Not Having HTTPS_Token = -1)","Type Here")
    Submitting_to_email = st.text_input("Submitting_to_email  (Submitting_to_email = 1 or Not Submitting_to_email = -1)","Type Here")
    Abnormal_URL = st.text_input("Abnormal_URL  (Abnormal_URL = 1 or Not Abnormal_URL = -1)","Type Here")
    Redirect = st.text_input("Redirect  (Redirecting = 1 or Not Redirecting = 0)","Type Here")
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> This Website is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> This Website is danger</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_Phishing_Website(having_IP_Address,having_Sub_Domain,HTTPS_token,Submitting_to_email,Abnormal_URL,Redirect)
        st.success('The probability of the Website is Phishing {}'.format(output))

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()