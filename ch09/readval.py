# 9.1 Handling Exceptions

# Repeatedly prompts user to enter a value until proper type
# has been entered, otherwise prints error message and prompts
# for input again.
# Note: polymorphic function (works for arguments of different types)
def read_val(val_type, request_msg, error_msg):
  while True:
      val = input(request_msg + ' ')
      try:
          return(val_type(val)) #convert str to val_typex
      except ValueError:
          print(val, error_msg)
          
if __name__ == "__main__":  
    val = read_val(int, 'Enter an integer:', 'is not an integer')
    print(f"val={val}")