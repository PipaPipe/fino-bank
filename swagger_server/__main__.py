#!/usr/bin/env python3
import Data.data_accounts
import connexion

from connexion import request
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml',
                arguments={'title': 'Получение информации о счете клиента третьей стороной'},
                pythonic_params=True)

    @app.route('/open-banking/v1.3/aisp/vrp-payments')
    def vrp_payments():
        js = request.json
        debetor_id = js['debetor_id']
        creditor_id = js['creditor_id']
        amount = js['amount']

        flag = False
        for n in Data.data_accounts.list_balance.data.balance:
            if (str(n.account_id) == debetor_id and n.amount.amount >= amount):
                if (n.amount.amount < amount):
                    return 'money not sufficient', 400
                n.amount.amount -= amount
                break
        else:
            return 'DEBETOR NOT FOUND', 400
        for j in Data.data_accounts.list_balance.data.balance:
            if (str(n.account_id) == creditor_id):
                j.amount.amount += amount
                return 'OK', 200

    app.run(port=8080)


if __name__ == '__main__':
    main()
