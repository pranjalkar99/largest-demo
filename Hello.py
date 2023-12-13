import streamlit as st

def find_largest_number(num1, num2, num3):
    numbers = [num1, num2, num3]
    return max(numbers)

def main():
    st.title("Largest Number Finder")
    
    st.markdown(
        """
        Welcome to the Largest Number Finder app for Week 8 TDS Assignment! 
        This simple app takes three numbers as input and finds the largest among them. 
        Give it a try by entering three numbers below and see if it helps with your assignment.
        """
    )

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest"):
        result = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()

