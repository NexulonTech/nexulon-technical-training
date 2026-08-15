import os
import json
import requests

BASE_URL = os.getenv("ODOO_BASE_URL", "https://edu-test4620.odoo.com")
DATABASE = os.getenv("ODOO_DATABASE", "edu-test4620")
API_KEY = os.getenv("ODOO_API_KEY")
CONTACT_ID = int(os.getenv("ODOO_CONTACT_ID", "8"))

if not API_KEY:
    raise RuntimeError(
        "Missing ODOO_API_KEY. Set it as an environment variable before running."
    )

HEADERS = {
    "Authorization": f"bearer {API_KEY}",
    "Content-Type": "application/json; charset=utf-8",
    "X-Odoo-Database": DATABASE,
}


def call_odoo(model: str, method: str, payload: dict):
    url = f"{BASE_URL}/json/2/{model}/{method}"
    response = requests.post(url, headers=HEADERS, json=payload, timeout=30)

    print(f"\nPOST {url}")
    print(f"Status: {response.status_code}")

    response.raise_for_status()

    try:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return data
    except ValueError:
        print(response.text)
        return response.text


def read_contacts():
    payload = {
        "context": {"lang": "en_US"},
        "domain": [],
        "fields": ["id", "name", "email", "phone", "city"],
        "limit": 10,
    }
    return call_odoo("res.partner", "search_read", payload)


def create_contact():
    payload = {
        "context": {"lang": "en_US"},
        "vals_list": {
            "name": "API Test Contact - Enjy",
            "email": "api.test.enjy@nexulon.com",
            "phone": "+201000000000",
            "city": "Cairo",
        },
    }
    return call_odoo("res.partner", "create", payload)


def update_contact(contact_id: int):
    payload = {
        "ids": [contact_id],
        "context": {"lang": "en_US"},
        "vals": {
            "phone": "+201000000001",
            "city": "Alex",
        },
    }
    return call_odoo("res.partner", "write", payload)


def verify_updated_contact(contact_id: int):
    payload = {
        "context": {"lang": "en_US"},
        "domain": [["id", "=", contact_id]],
        "fields": ["id", "name", "email", "phone", "city"],
        "limit": 1,
    }
    return call_odoo("res.partner", "search_read", payload)


def delete_contact(contact_id: int):
    payload = {
        "ids": [contact_id],
        "context": {"lang": "en_US"},
    }
    return call_odoo("res.partner", "unlink", payload)


def verify_deleted_contact(contact_id: int):
    payload = {
        "context": {"lang": "en_US"},
        "domain": [["id", "=", contact_id]],
        "fields": ["id", "name", "email", "phone", "city"],
        "limit": 1,
    }
    return call_odoo("res.partner", "search_read", payload)


def main():
    print("=== Odoo Contacts CRUD Evidence Script ===")

    print("\n1) READ CONTACTS")
    read_contacts()

    print("\n2) CREATE CONTACT")
    create_contact()

    print(
        "\nNOTE: The remaining steps mirror the Postman evidence and use "
        f"CONTACT_ID={CONTACT_ID}."
    )

    print("\n3) UPDATE CONTACT")
    update_contact(CONTACT_ID)

    print("\n4) VERIFY UPDATED CONTACT")
    verify_updated_contact(CONTACT_ID)

    print("\n5) DELETE CONTACT")
    delete_contact(CONTACT_ID)

    print("\n6) VERIFY DELETED CONTACT")
    verify_deleted_contact(CONTACT_ID)


if __name__ == "__main__":
    main()
