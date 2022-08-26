import enckey

enc_dec_keys = {}

def enc_init():
    commands = {'info': enc_info, 'load':enc_load, 'newkey':enc_newkey, 'save':enc_save, 'enc':enc_enc, 'dec':enc_dec}
    return commands

def main_cli():
    commands = enc_init()
    cli_end = False
    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if cmd and cmd[0] == 'done':
            cli_end = True
        elif cmd and cmd[0] in commands:
            commands[cmd[0]](cmd[1:])

def enc_save(*params):
    print('_____save')

def enc_load(*params):
    print('_____load')

def enc_newkey(*params):
    print('_____newkey', *params)
    dict_enc,dict_dec = enckey.new_enc_key()
    print(dict_enc)
    print(dict_dec)
    enc_dec_keys = {'key_name':''.join(params[0]),'enc_key':dict_enc,'dec_key':dict_dec}
    print(enc_dec_keys)

def enc_info(*params):
    print('____info')

def enc_enc(*params):
    print('____enc', *params)
    enckey.do_enc(enc_dec_keys['enc_key'], ''.join(params[0]), ''.join(params[1]))

def enc_dec(*params):
    print('____dec')

main_cli()