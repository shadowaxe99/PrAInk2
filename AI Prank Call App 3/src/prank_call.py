import voice_synthesis
import twilio_api


def generate_prank_conversation(custom_text=None):
    if custom_text:
        return custom_text
    else:
        return 'This is a prank call!'

def prank_call(phone_number, pricing_plan, voice, custom_text=None):
    if pricing_plan == 'free':
        print('Free plan selected. Limited to 1 call per day.')
    elif pricing_plan == 'premium':
        print('Premium plan selected. Unlimited calls.')
    else:
        print('Invalid pricing plan. Please select either free or premium.')
        return

    conversation = generate_prank_conversation(custom_text)
    audio_file = voice_synthesis.synthesize_text(conversation, voice)
    twilio_api.make_call(phone_number, 'actual_twilio_number', audio_file)
