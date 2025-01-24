from datetime  import datetime

class Time:
  def get_date(self):
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")
dt_info = Time()
print("Date:", dt_info.get_date())