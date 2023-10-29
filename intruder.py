import smtplib
def intruder():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('miniproject101w@gmail.com', 'wdeqibddrbedxzxv')
    server.sendmail('miniproject101w@gmail.com', 'miniproject101w@gmail.com', 'Intruder detected')
    timestr = now.strftime('%H:%M')
    f.writelines(f'\n{name},{timestr}')
    print("mail sent")



intruder()