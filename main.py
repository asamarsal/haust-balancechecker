import requests
import time

def load_display():
    try:
        with open('exluminate.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Welcome to Haust Multi Wallet Balance Checker!"

def get_balance_from_explorer(address):
    try:
        url = f"https://explorer-test.haust.network/api/v2/addresses/{address}/coin-balance-history-by-day"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        balance_wei = int(data['items'][0]['value'])
        balance_haust = balance_wei / 1e18

        print(f"🔍 Current Balance for {address}: {balance_haust:.7f} HAUST")
        print("=" * 67)
        return balance_haust
    except Exception as e:
        print(f"❌ Failed to fetch balance for {address}: {e}")
        print("=" * 67)
        return None

def main():
    print(load_display())
    print("\nEnter your wallet address, type 'done' if finished:")

    wallet_addresses = []
    count = 1

    while True:
        address = input(f"Wallet {count}: ").strip()
        if address.lower() == 'done':
            break
        wallet_addresses.append(address)
        count += 1

    # Save wallet addresses to a file
    with open('list.txt', 'w', encoding='utf-8') as file:
        for addr in wallet_addresses:
            file.write(addr + '\n')

    # Repeat balance checking every 20 seconds
    while True:
        print("\nChecking balances for saved wallet addresses...\n")
        for addr in wallet_addresses:
            get_balance_from_explorer(addr)
        print("⏳ Waiting for 20 seconds before the next check...\n")
        time.sleep(20)

if __name__ == "__main__":
    main()
