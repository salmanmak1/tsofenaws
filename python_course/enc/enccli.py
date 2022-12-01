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
            commands[cmd[0]](*cmd[1:])
        else:
            print(f"The command: {cmd[0]} is not existed")

def enc_save(*params):
    print('_____save', *params)
    enckey.do_save(enc_dec_keys, params[0])
    print(f"The current key {enc_dec_keys['key_name']} is saved into {params[0]} file")

def enc_load(*params):
    print('_____load', *params)
    enc_dec_keys = enckey.do_load(params[0])
    print(f"The current key is replaced to {enc_dec_keys['key_name']} which is loaded from {params[0]} file")

def enc_newkey(*params):
    print('_____newkey', *params)
    dict_enc,dict_dec = enckey.new_enc_key()
    global enc_dec_keys
    enc_dec_keys = {'key_name':''.join(params[0]),'enc_key':dict_enc,'dec_key':dict_dec}
    print(f"A new key: {params[0]} is created")

def enc_info(*params):
    print('____info', *params)
    enckey.do_info(enc_dec_keys)

def enc_enc(*params):
    print('____enc', *params)
    enckey.do_enc(enc_dec_keys['enc_key'], ''.join(params[0]), ''.join(params[1]))
    print(f"The file {params[0]} is encrypted into {params[1]}")

def enc_dec(*params):
    print('____dec', *params)
    enckey.do_dec(enc_dec_keys['dec_key'], ''.join(params[0]), ''.join(params[1]))
    print(f"The file {params[0]} is decrypted into {params[1]}")

main_cli()