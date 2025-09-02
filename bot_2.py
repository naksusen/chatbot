import re
import random

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    
    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    
    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))
    
    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {} # dictionary/map declaration for storing the probability
    
    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
# Responses CREATE RESPONSES HERE -------------------------------------------------------------------------------
    response(RESPONSE_GREET(), ['hello', 
                                'hi', 
                                'hey', 
                                'sup', 
                                'heyo', 
                                'wassup', 
                                'yo', 
                                'ciao'], single_response = True)
    
    response(RESPONSE_GREET_END(), ["goodbye", 
                                    "bye", 
                                    "byebye", 
                                    "farewell",
                                    "gotta go", 
                                    "gtg", 
                                    "cya", 
                                    "see you", 
                                    "later", 
                                    "see ya"], single_response = True)
    
    response(RESPONSE_STATUS_BOT(), ["how", 
                                     "are", 
                                     "you", 
                                     "doing", 
                                     "status",
                                     "kamusta",
                                     "kumusta"], single_response = True) # required_words=['how']
    
    response(RESPONSE_GRATITUDE(), ["thank", 
                                    "thanks", 
                                    "ty", 
                                    "thx", 
                                    "appreciate it", 
                                    "thankies", 
                                    "salamat", 
                                    "lamats",
                                    "tyty",
                                    "you"], single_response = True)
    
    response(RESPONSE_IDENTIFY_BOT(), ["who", 
                                       "name", 
                                       "thyself", 
                                       "yourself",
                                       "are"], single_response = True)
    
    response(RESPONSE_BUSINESS(),["how", 
                                 "to", 
                                 "obtain",
                                 "get",
                                 "steps",
                                 "know",
                                 "requirements",
                                 "permit"
                                ], required_words=["business"])
    
    response(RESPONSE_POSTALID(),["id", 
                                 "what", 
                                 "ano",
                                 "is"
                                ], required_words=["postal"])
    
    response(RESPONSE_POSTALID_APPLY(),["id", 
                                 "what", 
                                 "ano",
                                 "is",
                                 "how",
                                 "apply",
                                 "renew"]
                                , required_words=["postal"])
    
    response(RESPONSE_POLICE(), ["id", 
                                 "what", 
                                 "ano",
                                 "is",
                                 "how",
                                 "apply",
                                 "renew", 
                                 "clearance"]
                                , required_words=["police"])
    
    response(RESPONSE_CEDULA(), ["id", 
                                 "what", 
                                 "ano",
                                 "is",
                                 "how",
                                 "apply",
                                 "tax", 
                                 "clearance",
                                 "to",
                                 "get"]
                                , required_words=["cedula"])
    
    response(RESPONSE_SENIOR(), ["citizen", 
                                 "what", 
                                 "ano",
                                 "is",
                                 "how",
                                 "id",
                                 "to",
                                 "get"]
                                , required_words=["senior"])
    
    response(RESPONSE_CIVREG(), ["registration", 
                                 "what", 
                                 "ano",
                                 "is",
                                 "how",
                                 "id",
                                 "to",
                                 "get"]
                                , required_words=["civil"])
    
    response(baksBot(), ["beshy", "ma'am", "please"]
                                , single_response = True, required_words=["baksbot"])
    
    best_match = max(highest_prob_list, key = highest_prob_list.get)
    
    
    
    # print("\n",highest_prob_list) # for debugging
    print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}\n') # for debugging
    
    # Undefined/default response
    return DEFAULT_UNKNOWN() if highest_prob_list[best_match] < 1 else best_match

# Used to get the responses
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower()) # discards punctuation marks and isolates eaach word possible
    response = check_all_messages(split_message) # calls check_all_messages function with a value
    return response


# FUNCTIONS HERE STORE BOT RESPONSES | TAKES ONLY ONE FROM A LIST
def baksBot():
        R_baksBot = ["Psst! one-fifty", 
                     "Ma'am kahit 1.5 lang.", 
                     "Ba't bagsak ang beshy ko?"][random.randrange(3)]
        return R_baksBot
    
def RESPONSE_GRATITUDE():
    R_GRATITUDE = ["Gladly!", 
                   "No problem.",
                   "That's what I'm here for."][random.randrange(2)]
    return R_GRATITUDE

def RESPONSE_GREET():
    R_GREET = ["Hi there! How can I help you today?", 
               "Hi! How can I help you today?",][random.randrange(2)]
    return R_GREET

def RESPONSE_GREET_END():
    R_GREET_END = ["Goodbye! 👋", 
                   "Glad I could help.",
                   "Remember I'm available to help you 24 hours a day.\nThank you for contacting us. Goodbye."][random.randrange(3)]
    return R_GREET_END

def RESPONSE_STATUS_BOT():
    R_STATUS_BOT = ["I'm doing well, thank you. How can I help you today?", 
                    "I am good! Thank you for asking. 😀 How are you and how may I assist you today?",][random.randrange(2)]
    return R_STATUS_BOT

def RESPONSE_IDENTIFY_BOT():
    R_IDENTIFY_BOT = ["My name is BeA. I'm designed to help you.", 
                      "I'm BeA your virtual assistant. I can help you find different services that the Bacoor City provides!",][random.randrange(2)]
    return R_IDENTIFY_BOT

def RESPONSE_BUSINESS():
    R_BUSINESS = ["A business permit is an official document or license\n\
          granted by the government or local authority that \n\
          allows an individual or organization to legally \n\
          operate a business within a specific jurisdiction.\n\n\
   To obtain a Business Permit, you can follow these \n\
     general steps:\n\
   1. Find and Determine the location of the local Business \n\
       Permit and Licensing Office in Bacoor.\n\
   2. Obtain a copy of the application form for a business \n\
       permit and fill it out accurately.\n\
   3. Submit the application form along with the required \n\
       documents to the Business Permit and \n\
       Licensing Office.\n\
   4. After submitting the application form, it will be \n\
       reviewed by the appropriate authorities.\n\
   5. Once your application is approved, you may be \n\
       required to pay the business permit fee and \n\
       other required fees.\n\
   6. After fulfilling the necessary payments, you will \n\
       receive your business permit."
                      ][random.randrange(1)]
    return R_BUSINESS

def RESPONSE_POSTALID():
    R_POSTALID = ["A Postal ID, also known as a Postal Identification Card, is a government-issued identification card that serves as proof of identity and address. It is issued by the Philippine Postal Corporation (PhilPost).\n\n1. How to Apply for Postal ID\n2. How to Renew a Postal ID." 
                      ][random.randrange(1)]
    return R_POSTALID

def RESPONSE_POSTALID_APPLY():
    R_POSTALID = ["To obtain a Postal ID in the Philippines, you typically need to follow these steps:\n\n1. Prepare the necessary documents: Bring originals and photocopies of supporting documents, such as a birth certificate, proof of address, and a valid ID.\n2. Accomplish the application form: Visit the nearest Philippine Postal Corporation (PhilPost) office and fill out the Postal ID application form. You may also need to provide personal information and have your photo taken.\n3. Pay the required fees: Fees vary; inquire at the PhilPost office for the updated schedule.\n4. Submit your application: Submit the accomplished form, required documents, and payment to the designated PhilPost personnel.\n5. Claim your Postal ID: Processing time varies. Once ready, you will be notified and can claim it at the PhilPost office by presenting your receipt or claim stub."][random.randrange(1)]
    return R_POSTALID

def RESPONSE_POLICE():
    R_POLICE = ["To obtain a Police Clearance in the Philippines, \n\
          you typically need to comply with the following \n\
          requirements: \n\n\
       • Valid ID: You must present a valid goverment-issued\n\
          identification document, such as a passport, driver's\n\
          license, or postal ID. The ID should have \n\
          your photo and signature. \n\n\
       • Accomplished Application Form: You will need to fill\n\
          out an application form provided by the police \n\
          station or online depending on the local requirement.\n\
          the form will require your personal information, \n\
          including your full name, address, contact details,\n\
          and purpose for obtaining the clearance. \n\n\
       • Proof of Residency: You may need to provide proof\n\
          of residency, such as a utility bill or\n\
          barangay certificate, to establish your address. \n\n\
       • Application Fee: Police Clearance applicatios often\n\
          require a fee, which varies depeding on the\n\
          local goverment unit. The fee is usually paid at \n\
          the Treasure's Office or a designated payment \n\
          center within the police station. \n\n\
       • Recent ID Photos: Prepare two (2) recent passport-\n\
          sized ID photos with a white background.\n\
          The specific size and format may vary, so \n\
          it's best to inquire at the police station \n\
          beforehand. \n\n\
       • Fingerprinting: You will be required to have \n\
          your fingerprints taken at the police station.\n\
          This step is usually done digitally using a\n\
          fingerprint scanner. \n\n\
       • Personal Appearance: In most cases, you must \n\
          personally appear at the police station to \n\
          submit your application form, present your \n\
          identification, and undergo the necessary \n\
          processes, such as fingerprinting and \n\
          verification."][random.randrange(1)]
    return R_POLICE

def RESPONSE_CEDULA():
    R_CEDULA = ["Cedula refers to a community tax certificate it is a \n\
          goverment-issued identification document. \n\
          Follow these steps below to get a Cedula in the \n\
          Philippines: \n\n\
       1. Visit the municipal hall, city hall, or barangay hall \n\
           within your area of residence. \n\n\
       2. Present your valid ID. \n\n\
       3. Fill out the application slip with the required \n\
           information. \n\n\
       4. Submit the form for checking and computation. \n\n\
       5. Pay the applicable fees."][random.randrange(1)]
    return R_CEDULA

def RESPONSE_SENIOR():
    R_SENIOR = ["The Senior Citizen ID is a type of identification given\n\
          to individuals who are 60 years old and above\n\
          to prove their status as senior citizens. It is \n\
          commonly used to avail privileges and benefits \n\
          provided by the government and establishments \n\
          for senior citizens.\n\n\
          The Senior Citizen ID can be used as proof of age \n\
          and senior citizen status in the following situations:\n\
       • Discounts on public transportation.\n\
       • Discounts at stores and establishments.\n\
       • Free health benefits.\n\
       • Privileges for government and local services.\n\n\
          To obtain a Senior Citizen ID, you can follow \n\
          these general steps:\n\n\
       1. Check your local government and determine the \n\
           needed requirements.\n\n\
       2. Prepare the following:\n\
            • Proof of age, citizenship and identification \n\
              (e.g PSA, Passport, Valid ID.\n\
            • Proof of Recedency (e.g barangay certificate, \n\
              Utility Bill).\n\
            • Provide an updated 2x2 ID photo, white \n\
              background with formal attire.\n\n\
       3. Visit the designated office responsible for \n\
           processing Senior Citizen IDs in your area.\n\n\
       4. Fill out the application form for the Senior Citizen ID \n\
           accurately and completely. Attach the required \n\
           documents and submit them to the office.\n\n\
       5. The office will process your application. \n\
           Once your application is approved, you \n\
           will be notified to pick up your \n\
           Senior Citizen ID."][random.randrange(1)]
    return R_SENIOR

def RESPONSE_CIVREG():
    R_CIVREG = ["Civil registration is the process of registering civil \n\
          events that have legal effects on an individual or \n\
          family. It is a system of recording and registering \n\
          significant life events of individuals.\n\
          Civil registration records are required in many legal \n\
          transactions, such as obtaining a passport, applying \n\
          for a job, changing surnames, property ownership, \n\
          and more.\n\n\
       Here are the general steps that can be followed to \n\
        obtain civil registration:\n\
       1. Prepare the following required documents: birth \n\
          certificates, identification documents, marriage \n\
          certs, death certs, and other required documents \n\
          that the agency may request.\n\n\
       2. Go to your local civil registration agency, such as \n\
          the Civil Registrar's Office, where you reside make \n\
          sure to bring all the required documents.\n\n\
       3. Submit the required documents and application \n\
          form for civil registration.\n\n\
       4. Pay the necessary fees required for obtaining civil \n\
          registration records.\n\n\
       5. After submitting the application and payment, \n\
          you will receive the necessary documents."][random.randrange(1)]
    return R_CIVREG

def DEFAULT_UNKNOWN():
    default_response = ["Could you please rephrase that? Try keywords like \n\
          'Civil Registration' or 'Business Permit'.",
                        "I am not positive that I understand what you're \n\
          asking. Please try rewording your question. Try \n\
          keywords like 'Civil Registration' or 'Senior ID'.",
                        "Oh! It appears you wrote something I don't \n\
          understand yet. Try keywords like 'Civil Registration'\n\
          or 'Business Permit'.", 
                        "I'm terribly sorry. I didn't quite catch that. Try \n\
          rephrasing your question. Try keywords like \n\
          'Civil Registration' or 'Business Permit'.", 
                        "What does that mean? Try keywords like 'Civil \n\
          Registration' or 'Business Permit'."][random.randrange(5)]
    return default_response
BOT_NAME = "BeA"
