# Utility konversi format akun - NM.CDX
import json


def convert_accounts(input_file, output_file):
    """Konversi format list akun ke format dict"""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            accounts_list = json.load(f)

        accounts_dict = {}
        for account in accounts_list:
            uid = str(account.get("uid"))
            password = account.get("password")
            if uid and password:
                accounts_dict[uid] = password

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(accounts_dict, f, indent=2, ensure_ascii=False)

        print(f"✅ JSON hasil konversi disimpan ke '{output_file}'")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    input_file = "accounts_list.json"
    output_file = "accs.json"
    convert_accounts(input_file, output_file)