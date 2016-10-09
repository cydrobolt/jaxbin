import random, string
from models import Bin

def generate_token(token_length):
    while True:
        # Find unused Bin token
        bin_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(token_length))
        if not Bin.select().where(Bin.p_id == bin_id).exists():
            # Break out of loop when an unused token is found
            break

    return bin_id
