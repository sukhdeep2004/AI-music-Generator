from google import genai
# from google.genai import types

def numbers_to_strings(argument):
    if(argument==1):
        return "give me random jazz music notes and no other information"
    
    elif(argument==2):  
        return"give me random classical notes and no other information"
    

    # get() method of dictionary data type returns 
    # value of passed argument if it is present 
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return "Invalid choice"


if __name__ == "__main__":
    print("Options")
    print("1. Jazz Music Notes")
    print("2. Classical Music Notes")
    user_input = int(input("Enter your Choice "))
    choice = numbers_to_strings(user_input)+"""Use this JSON schema:
    Notes : str"""
    
    client = genai.Client(api_key="AIzaSyBM24O8IBcbrTMU9GY8Euu_y_E4YInKqkM")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=choice,
        config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1
    )
    )
    print(response.text)

