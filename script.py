# -*- coding: utf-8 -*-

import base64
import json
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts

# Adresse de l'API de Solana
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(SOLANA_RPC_URL)

def get_token_accounts_by_owner(owner_address):
    # Convertir l'adresse de l'utilisateur en Pubkey
    owner_public_key = Pubkey.from_string(owner_address)
    
    # Définir les options pour récupérer les comptes de tokens
    opts = TokenAccountOpts(
        program_id=Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
    )
    
    # Récupérer les comptes de token détenus par l'adresse
    response = client.get_token_accounts_by_owner(
        owner_public_key,
        opts
    )
    
    # Accéder à la valeur de la réponse
    token_accounts = response.value
    
    if token_accounts:
        return token_accounts
    else:
        return None

def decode_account_data(data):
    if isinstance(data, list) and len(data) > 0:
        # Vérifier que les données sont une chaîne encodée en base64
        decoded_data = base64.b64decode(data[0])
        return decoded_data
    return None

def main():
    owner_address = "2onYZHxdPK1fyUJpyfmctJZQKFS5ncHVWgYzLXLb4DsG"  # Remplacez par l'adresse réelle
    token_accounts = get_token_accounts_by_owner(owner_address)
    
    if token_accounts:
        for account in token_accounts:
            print("Token Account: {}".format(account.pubkey))
            account_info = decode_account_data(account.account.data)
            if account_info:
                print("Account Info: {}".format(account_info))
            else:
                print("Failed to decode account data.")
            print()
    else:
        print("Aucun compte de token trouvé pour cette adresse.")

if __name__ == "__main__":
    main()
