#!/usr/bin/env python3
import connexion
from connexion import request

import Data.data_accounts
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml',
                arguments={'title': 'Получение информации о счете клиента третьей стороной'},
                pythonic_params=True)

    @app.route('/open-banking/v1.3/aisp/vrp-payments', methods=['POST', ])
    def vrp_payments():
        js = request.json
        debtor_id = js['debtor_id']
        creditor_id = js['creditor_id']
        amount = js['amount']
        print(debtor_id)
        for n in Data.data_accounts.list_balance.data.balance:
            print(n.amount)
            if str(n.account_id) == str(debtor_id):
                print(n.amount.amount, amount)
                if n.amount.amount < float(amount):
                    print('return')
                    return 'money not sufficient', 403
                n.amount.amount -= amount
                break
        else:
            return 'debtor not found', 400

        for j in Data.data_accounts.list_balance.data.balance:
            if str(j.account_id) == str(creditor_id):
                j.amount.amount += float(amount)
                return 'OK', 200
        else:
            return 'creditor not found', 400

    app.run(port=8080)


if __name__ == '__main__':
    main()
