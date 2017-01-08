import sys
import os
#additional_path = os.path.join(sys.path[0], "third_party_code")
additional_path = os.path.join(os.path.dirname( __file__ ), '..', '..', '..', "third_party_code")
sys.path.append(additional_path)
import stripe as payment_provider
