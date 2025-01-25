from datetime import datetime  
# Importing datetime module to fetch real date and time
# changes done by shweta

class DateTimeInfo:
    def get_time(self):
        """Returns the current time in HH:MM:SS format."""

        return datetime.now().strftime("%H:%M:%S")
    
    def get_date(self):
        """Returns the current date in YYYY-MM-DD format."""
        return datetime.now().strftime("%Y-%m-%d")
    
    def get_day(self):
        """Returns the current day of the week."""
        return datetime.now().strftime("%A")
    
    def get_month(self):
        """Returns the current month."""
        return datetime.now().strftime("%B")
    
    def get_year(self):
        """Returns the current year."""
        return datetime.now().year

dt_info = DateTimeInfo()
print("Time:", dt_info.get_time())
print("Date:", dt_info.get_date())
print("Day:", dt_info.get_day())
print("Month:", dt_info.get_month())
print("Year:", dt_info.get_year())
#comment added by Sarang