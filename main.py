import requests

def get_balance_from_explorer(address):
    try:
        url = f"https://explorer-test.haust.network/api/v2/addresses/{address}/coin-balance-history-by-day"
        response = requests.get(url)
        response.raise_for_status()  # Check for successful response

        # Parse the response JSON
        data = response.json()
        
        # Extract the balance value
        balance_wei = int(data['items'][0]['value'])
        
        # Convert Wei to HAUST
        balance_haust = balance_wei / 1e18
        
        print(f"🔍 Current Balance for {address}: {balance_haust:.7f} HAUST")
        return balance_haust
    except Exception as e:
        print(f"❌ Failed to fetch balance for {address}: {e}")
        return None

def main():
    wallet_addresses = []

    print("Enter wallet addresses one by one. Type 'done' when you are finished:")
    while True:
        wallet_address = input("Enter wallet address: ").strip()
        if wallet_address.lower() == 'done':
            break
        wallet_addresses.append(wallet_address)
    
    # Save addresses to list.txt
    with open("list.txt", "w") as file:
        for address in wallet_addresses:
            file.write(address + "\n")
    print("✅ Wallet addresses saved to list.txt.")

    # Check balance for each address
    print("\n🔍 Checking balances:")
    for address in wallet_addresses:
        get_balance_from_explorer(address)

if __name__ == "__main__":
    main()
