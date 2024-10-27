import click
import jsonmanager
import json
import os
from tabulate import tabulate
from datetime import datetime

@click.group()
def hisabkitab():
    pass

@hisabkitab.command()
def hisab():
    data = jsonmanager.read_json()
    if len(data) <= 0:
        print('You don\'t have any Hisabs.')

    else:
        table = []
        table.append(['id','name','amount','status','created_at','updated_at'])
        for task in data:
            aux = [task['id'], task['name'], task['amount'], task['status'], task['created_at'], task['updated_at']]    
            table.append(aux)

        print(tabulate(table, headers="firstrow", tablefmt="heavy_grid"))


@hisabkitab.command()
@click.argument('status', type=str)
def list(status):
    list_status = ['paid','to_pay']
    if status not in list_status:
        print('Entered argument is not valid')

    data = jsonmanager.read_json()
    if len(data) <= 0:
        print('khatabook is empty')

    else:
        table = []
        table.append(['id','name','amount','status','created_at','updated_at'])
        for task in data:
            aux = [task['id'], task['name'], task['amount'], task['status'], task['created_at'], task['updated_at']]    
            table.append(aux)

        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))


@hisabkitab.command()
@click.argument('name', type=str)
@click.argument('amount', type=float)
def add(name, amount):
    data = jsonmanager.read_json()
    newid = len(data) + 1
    now = datetime.now()
    task = {
        'id': newid,
        'name': name,
        'amount': amount,
        'status': 'to_pay',
        'created_at': now.strftime("%d/%m/%Y %H:%M:%S"),
        'updated_at': ''
    }
    data.append(task)
    jsonmanager.write_json(data)
    print(f"Hisab added successfully (ID: {task['id']})")


@hisabkitab.command()
@click.argument('name', type=str)
@click.option('--paid', required=True, help="Paid Amount")
def update(name,paid):
    data = jsonmanager.read_json()
    item = next((t for t in data if t['name']==name),None)
    amount=item['amount']

    if not item:
        print(f"Hisab with {name} not found!")

    else:
        if paid is not None:
            item['amount'] = amount-int(paid)
            now = datetime.now()
            item['updated_at'] = now.strftime("%d/%m/%Y %H:%M:%S")
        jsonmanager.write_json(data)
        print(f"Hisab with {name} has been updated")


@hisabkitab.command()
@click.argument('name', type=str)
def delete(name):
    data = jsonmanager.read_json()
    for x in data:
        if x['name'] == name:
            hisab = x
        else:
            hisab = None
        break

    if hisab is not None:
        data.remove(hisab)
        jsonmanager.write_json(data)
        print(f'Hisab of \'{name}\' deleted.')
    else:
        print(f'Hisab of \'{name}\' not found.')


if __name__ == '__main__':
    hisabkitab()


