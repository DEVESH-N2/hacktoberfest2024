import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    rates = response.json().get("rates", {})
    if target_currency in rates:
        print(f"1 {base_currency} = {rates[target_currency]} {target_currency}")
    else:
        print("Currency not found.")

# Example usage
get_exchange_rate("USD", "EUR")
