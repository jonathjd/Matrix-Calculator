###########################################################################################
# This calculator was created by Jonathan Dickinson
# This is meant to help students learn how to work with Matrices
#############################################################################################
import numpy as np
import streamlit as st
########################################################################################
# Page configuration
##########################################################################################
st.set_page_config(page_title="Linear Algebra Calculator", layout="wide")

############################################################################################
# Title and how to use the app
########################################################################################
with st.container():
    st.title("Linear Algebra Solver")
    st.write("###")
    st.subheader("How to use the web application:")
    st.write("Select the number of rows **(m)** and columns **(n)** that your matrix A is")
###########################################################################################
# Selection of the action the student wants to take
user_selection = st.selectbox(
    "What operation would you like to perform?",
    ("Scalar Multiplication", "Matrix Multiplication", "Matrix Addition", "Adjoint", "Dot (Scalar) Product")
)

if user_selection == "Scalar Multiplication":
     with st.container():
        st.write("---")
        left_col, right_col = st.columns(2)
        with left_col:
            st.header(user_selection)
            st.write("If X is a matrix and the lowercase Greek letter lambda (l) is a scalar, then lX is the matrix created via multiplication of lX.")
            st.write("An example is shown to the right")
        with right_col:
            X = np.array([[2, 1, 3], [4, 2, 1], [6, -3, 4]])
            st.write("[X] = ", X)

#########################################################################################
#################### Begin Calculations ##################################################
############################################################################################
