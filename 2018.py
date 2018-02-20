import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("manjunathiyer892@gmail.com","srrajesh113")
msg="hi how are you"
s.sendmail("manjunathiyer892@gmail.com","manjunath.17cs@cmr.edu.in",msg)
print ("sent msg successfully")
s.quit()
