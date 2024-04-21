import streamlit as st

def find_max(a, b, c):
    return max(a, b, c)

def main():
    st.title("Maximum Number Finder")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    if st.button("Find Maximum"):
        maximum = find_max(a, b, c)
        st.success(f"The maximum number is: {maximum}")

if __name__ == "__main__":
    main()
  
