import json_manager
import click


@click.group()
def cli():
    pass

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")
        
@cli.command()
@click.argument('id', type=int)
def user(_id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == _id), None)
    if user is None:
        print(f'User with id {id} not found.')
    else:
        print(f"User: {user['id']} - {user['name']} - {user['lastname']}")
        
@cli.command()
@click.argument('id', type=int)
def delete(_id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == _id), None)
    if user is None:
        print(f'User with id {_id} not found.')
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User: {user['id']} - {user['name']} - {user['lastname']} delated successfuly.")
    
@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='Name of the user')    
@click.option('--lastname', help='Lastname of the user')    
def update(_id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == _id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    json_manager.write_json(data)
    print(f'User with {_id} updated successefuly.')
    

@cli.command()
@click.option('--name', required=True, help='Name of the user')
@click.option('--lastname', required=True, help='Lastname of the user')
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('The name and last name are required')
    else:
        data = json_manager.read_json()
        ids = [_id['id'] for _id in data]
        new_id = max(ids) + 1
        new_user = {
            'id' : new_id,
            'name' : name,
            'lastname' : lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f'User with id {new_id} - {name} {lastname} created successfuly.')

if __name__ == '__main__':
    cli()
