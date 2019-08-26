from student import *
from service import *


name = raw_input("Enter yor name")
st.set_name(name)

age = raw_input("Enter Your age")
st.set_age(age)

addr = raw_input("Enter Your age")
st.set_addr(addr)

print("-----------------------------")
print("Name\t:" +st.get_name())
print("Age\t:" +st.get_age())
print("Address\t:" +st.get_addr())
print("-----------------------------")
