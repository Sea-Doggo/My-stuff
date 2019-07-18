import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "66274b30-a980-11e9-a84b-951c0154684a07460e62-6534-4eae-9373-5690df895093"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
        
    def anwser_question():
        question = input(">")
        anwser = classifyPy(question)
        anwserclass = answer["class_name"]
        confidence = answer["confidence"]
        if confidence < 75%:
            print("I am not quite sure , ask another question")
        elif answerclass == "Doggos":
            print("Use a doggo that is between 29-35 killometers long, idealy 32 killometers, is on the thicker side, and is comfy.")
        elif answerclass == "shapes":
            print("A Googolplex kilometers long Parallelepiped") 
            
    print("Lets talk about long bois.")
    while True:
        anwser_question()