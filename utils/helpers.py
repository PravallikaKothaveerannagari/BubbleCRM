import string
import hashlib

## image url received from the frontend is //a1a38c43d0c31f6413020becb68e6712.cdn.bubble.io/f1718710950024x472409760984467100/bubble-exterior1718711097704.png
def process_image_urls(image_url: str) -> list:
    try:
        if "https:" in image_url:
            return image_url
        elif image_url:
            return ["https:" + url.strip().replace("\n", "") for url in image_url.split(",")]
    except Exception as e:
        print(f"Error processing Image Url {e}")
        return []


def process_carfax_url(carfax_url):
    try:
        if "https" in carfax_url or "http" in carfax_url:
            return carfax_url
        elif carfax_url:
            processed_url = "https:" + carfax_url.strip()
            return processed_url
        else:
            return None
    except Exception as e:
        return None


def process_main_img(img_url : str) ->str:
    print(img_url)
    try:
        if "https:" in img_url:
            main_image_url = img_url.strip()
        else:
            main_image_url = "https:" + img_url.strip()
        return main_image_url
    except Exception as e:
        print(f"Error processing Main Image {e}")
        return ''

def process_numerical_data(Mileage, Number_of_Cylinders, Price, Number_of_Passengers, Number_of_Doors, Carfax):

    Mileage = Mileage.replace("km", "").replace("mi", "").strip() if Mileage else None

    Number_of_Cylinders = int(Number_of_Cylinders) if Number_of_Cylinders else None

    Price = int(str(Price).strip()) if Price else None

    Number_of_Passengers = int(Number_of_Passengers) if Number_of_Passengers else None

    Number_of_Doors = int(Number_of_Doors) if Number_of_Doors else None

    Carfax = int(Carfax) if Carfax else None

    return Mileage, Number_of_Cylinders, Price, Number_of_Passengers, Number_of_Doors, Carfax



def generate_unique_id(text,other=''):
        # Remove brackets and punctuation
    text = text.translate(str.maketrans('', '', string.punctuation)) ## remove punctuations
    other = other.translate(str.maketrans('', '', string.punctuation))
    # Combine company name and address
    unique_string = f"{text}{other}"
    unique_string.replace(",",'').replace(" ",'').replace("'",'').replace('"','').replace(".",'')
    
    # Create an MD5 hash object
    hash_object = hashlib.md5(unique_string.encode())
    
    # Generate the hexadecimal representation of the hash
    unique_id = hash_object.hexdigest()
    
    return unique_id


