from data_access.data_access import create_accounts_table, insert_account, get_all_accounts

create_accounts_table()

insert_account("Alice", 1000.0)
insert_account("Bob", 1500.0)

accounts = get_all_accounts()
for acc in accounts:
    print(f"ID: {acc[0]}, Name: {acc[1]}, Balance: ${acc[2]:.2f}")
