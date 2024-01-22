"""PROBLEM STATEMENT : write a program that converts given number of days into year,, weeks and days
"""

def convert_days(days):
  """Converts a given number of days into years, months, weeks, and days.

  Args:
    days: An integer representing the number of days.

  Returns:
    A dictionary containing the number of years, months, weeks, and remaining days.
  """

  years = days // 365
  remaining_days = days % 365

  months = remaining_days // 30
  remaining_days = remaining_days % 30

  weeks = remaining_days // 7
  remaining_days = remaining_days % 7

  return {
      "years": years,
      "months": months,
      "weeks": weeks,
      "days": remaining_days,
  }

# Example usage
days = int(input("Enter Number of days : "))
converted_time = convert_days(days)

print(f"Number of days: {days}")
print(f"Years: {converted_time['years']}")
print(f"Months: {converted_time['months']}")
print(f"Weeks: {converted_time['weeks']}")
print(f"Remaining days: {converted_time['days']}")
