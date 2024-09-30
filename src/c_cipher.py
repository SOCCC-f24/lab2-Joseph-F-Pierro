import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email="abc012"):
    """
    TODO: What is the objective? 
                                        # what's expected and returned with arguments and variables (Joe)
    Args:
        TODO: what arguments and data types are expected? (i.e., email)
                                       # the arguments would be a string and not a float (Joe)
    Returns:
        TODO: what varibale and data types are being returned?   # The return that would be out putted would be a string (Joe)
    """
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals # i tried to fix the line below with isalpha etc.(Joe)
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = email[:3] != 'abc' or  email[3:] != '012'
    if anum_flag.isalpha():
        print(f"Is '{anum_flag}' an alpha? {anum_flag.isalpha()}")
    elif anum_flag.isdecimal():
        print(f"Is '{anum_flag}' a decimal? {anum_flag.isdecimal()}")

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    email_lst = ["a", "b", "c", "0", "1", "2"]
    sep = ','
    email_list = sep.join(email_lst)  # i used join to turn our list into a string (Joe)
        
    # TODO: complete line(s) below, convert EACH new element into a string
    new_ascii = ord(email_lst[0]) + 3    # NOTE: here we extract and update element at 0 
    email_lst[0] = chr(new_ascii)        # NOTE: here we convert our ASCII into string
        
    # TODO: fix line below, convert list into a string
    email_str = "dbc012"
    email_str = sep.join(email_str)  #I converted a list into a string using join (Joe)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = email[:3] != 'def' or email[3:] != '345' 
  if anum_flag.isalpha():
        print(f"Is '{anum_flag}' an alpha? {anum_flag.isalpha()}")
    elif anum_flag.isdecimal():
        print(f"Is '{anum_flag}' a decimal? {anum_flag.isdecimal()}")
        
    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO: apply the encrypt pseudocode but shift down 3
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = "aef345"
    return retVal
