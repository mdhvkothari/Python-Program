import sys
from day9 import send_mail

mgs_template = """ Hello {name} Thanks you for joining {website}. We are very happy to have with you with us. """

def format_msg(my_name="Madhav", my_website="cfe.com"):
    my_msg = mgs_template.format(name = my_name,website = my_website)
    
    return my_msg


if __name__ == "__main__":
    #this will take argument from the command line
    print(sys.argv)
    msg = format_msg(sys.argv[1],sys.argv[2])
    send_mail(text=msg,to_emails=sys.argv[3])
    print(msg)
