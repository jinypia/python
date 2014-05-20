import datetime
def elapsed_time(sdate):
    e = datetime.datetime.now()
    if not sdate or len(sdate) < 14: return 0,0,0,0
    s = datetime.datetime(int(sdate[:4]), int(sdate[4:6]), int(sdate[6:8]), 
        int(sdate[8:10]), int(sdate[10:12]), int(sdate[12:14]))
    days = (e-s).days
    sec = (e-s).seconds
    hour, sec = divmod(sec, 3600)
    minute, sec = divmod(sec, 60)
    return days, hour, minute, sec

print ((datetime.datetime.now() - datetime.timedelta(7)).strftime("%Y%m%d"))
