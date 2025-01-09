from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days)
  return future_date

def main():
  display_current_datetime()

  while True:
    try:
      days = int(input("Enter the number of days to add to the current date: "))
      future_date = calculate_future_date(days)
      formatted_future_date = future_date.strftime("%Y-%m-%d")
      print(f"Future date: {formatted_future_date}")
      break
    except ValueError:
      print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
  main()