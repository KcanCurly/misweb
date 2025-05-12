from urllib.parse import urljoin

def extract_forms(soup, base_url):
    forms = soup.find_all('form')
    for i, form in enumerate(forms, 1):
        action = form.get('action')
        method = form.get('method', 'GET').upper()
        full_action = urljoin(base_url, action)
        inputs = form.find_all('input')
        input_details = []
        for inp in inputs:
            name = inp.get('name', '')
            input_type = inp.get('type', 'text').lower()
            is_hidden = input_type == 'hidden'
            input_details.append({'name': name, 'type': input_type, 'hidden': is_hidden})


        print(f"\n[FORM {i}]")
        print(f"  Action: {full_action}")
        print(f"  Method: {method}")
        print(f"  Inputs:")
        for inp in input_details:
            hidden_mark = " [HIDDEN]" if inp['hidden'] else ""
            print(f"    - {inp['name']} [type={inp['type']}{hidden_mark}]")