from twilio.rest import Client


def make_call(to, from_, audio_file):
    account_sid = 'actual_account_sid'
    auth_token = 'actual_auth_token'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=to, 
        from_=from_,
        url='http://yourserver.com/path_to_audio_file'
    )
    print(call.sid)