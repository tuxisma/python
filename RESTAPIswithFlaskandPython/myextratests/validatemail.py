import re
def validateEmail(email):
    if len(email) > 7:
        #if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True

    return False

if validateEmail("igarcia@illumina.com"):
    print('it works!')
else:
    print('bad email')

