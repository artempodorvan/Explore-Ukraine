from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

# urls for each region on site
url = 'https://www.zagorodna.com/uk/regioni-ukrajni/dnipropetrovska-oblast'
url1 = 'https://www.zagorodna.com/uk/regioni-ukrajni/avtonomna-respublika-krim'
url2 = 'https://www.zagorodna.com/uk/regioni-ukrajni/donecka-oblast'
url3 = 'https://www.zagorodna.com/uk/regioni-ukrajni/zhitomirska-oblast'
url4 = 'https://www.zagorodna.com/uk/regioni-ukrajni/zakarpatska-oblast'
url5 = 'https://www.zagorodna.com/uk/regioni-ukrajni/zaporizka-oblast'
url6 = 'https://www.zagorodna.com/uk/regioni-ukrajni/ivanofrankivska-oblast'
url7 = 'https://www.zagorodna.com/uk/regioni-ukrajni/kijvska-oblast'
url8 = 'https://www.zagorodna.com/uk/regioni-ukrajni/vinnicka-oblast'
url9 = 'https://www.zagorodna.com/uk/regioni-ukrajni/volinska-oblast'
url10 = 'https://www.zagorodna.com/uk/regioni-ukrajni/kirovogradska-oblast'
url11 = 'https://www.zagorodna.com/uk/regioni-ukrajni/luganska-oblast'
url12 = 'https://www.zagorodna.com/uk/regioni-ukrajni/lvivska-oblast'
url13 = 'https://www.zagorodna.com/uk/regioni-ukrajni/mikolajvska-oblast'
url14 = 'https://www.zagorodna.com/uk/regioni-ukrajni/odeska-oblast'
url15 = 'https://www.zagorodna.com/uk/regioni-ukrajni/poltavska-oblast'
url16 = 'https://www.zagorodna.com/uk/regioni-ukrajni/rivnenska-oblast'
url17 = 'https://www.zagorodna.com/uk/regioni-ukrajni/sumska-oblast'
url18 = 'https://www.zagorodna.com/uk/regioni-ukrajni/khmelnicka-oblast'
url19 = 'https://www.zagorodna.com/uk/regioni-ukrajni/cherkaska-oblast'
url20 = 'https://www.zagorodna.com/uk/regioni-ukrajni/chernivecka-oblast'
url21 = 'https://www.zagorodna.com/uk/regioni-ukrajni/chernigivska-oblast'
url22 = 'https://www.zagorodna.com/uk/regioni-ukrajni/ternopilska-oblast'
url23 = 'https://www.zagorodna.com/uk/regioni-ukrajni/kharkivska-oblast'
url24 = 'https://www.zagorodna.com/uk/regioni-ukrajni/khersonska-oblast'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

app = Flask(__name__)

class ParseRegions():
    def __init__(self, tag, tag1, tag2, button_id):
        self.tag = tag
        self.tag1 = tag1
        self.tag2 = tag2
        self.button_id = button_id
        self.url = url


    def ParseInfo(self, tag, tag1, tag2, button_id):
        tag = tag
        tag1 = tag1
        tag2 = tag2
        button_id = button_id

        if button_id == 'Krim':
            try:
                response = requests.get(url1, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Dnipro':
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Doneck':
            try:
                response = requests.get(url2, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Zitomer':
            try:
                response = requests.get(url3, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Karpaty':
            try:
                response = requests.get(url4, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Zaporiza':
            try:
                response = requests.get(url5, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Frankifsk':
            try:
                response = requests.get(url6, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Kyiv':
            try:
                response = requests.get(url7, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Vinitsa':
            try:
                response = requests.get(url8, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Volin':
            try:
                response = requests.get(url9, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Kirovograd':
            try:
                response = requests.get(url10, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Luhansk':
            try:
                response = requests.get(url11, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Lviv':
            try:
                response = requests.get(url12, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Mikolaiv':
            try:
                response = requests.get(url13, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Odessa':
            try:
                response = requests.get(url14, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Poltava':
            try:
                response = requests.get(url15, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Rivne':
            try:
                response = requests.get(url16, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Sumy':
            try:
                response = requests.get(url17, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Hmelnickii':
            try:
                response = requests.get(url18, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Cherkasi':
            try:
                response = requests.get(url19, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Chernivci':
            try:
                response = requests.get(url20, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Chernigiv':
            try:
                response = requests.get(url21, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Ternopil':
            try:
                response = requests.get(url22, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Kharkiv':
            try:
                response = requests.get(url23, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


        elif button_id == 'Herson':
            try:
                response = requests.get(url24, headers=headers)
                response.raise_for_status()  # Raise an error for 4XX or 5XX status codes

                soup = BeautifulSoup(response.text, 'html.parser')
                div = soup.find('div', class_='article-main__body')
                # first tag will be p
                content = div.find_all(tag)

                # to find a strong tag in content
                region_name = ''
                for p_tag in content:
                    strong_tag = p_tag.find(tag1)

                    if strong_tag:
                        region_name += strong_tag.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_name += p_tag.text + '/n'
                        break

                # to find a br tag in content
                region_info = ''
                for p_tag in content:
                    br_tags = p_tag.find(tag2)

                    if br_tags:
                        region_info += br_tags.text + '/n'
                        break

                    elif p_tag.text.strip():  # Check if the <p> tag contains text
                        region_info += p_tag.text + '/n'
                        break

                return region_name, region_info

            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error occurred while processing the request."


class ParseDatas():
    def __init__(self, tag, tag1, tag2, url):
        self.tag = tag
        self.tag1 = tag1
        self.tag2 = tag2
        self.url = url

    def ParseInfo(self):
        try:
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            elements = soup.find_all(self.tag, class_='gold')

            for element in elements:
                day = element.find(self.tag1)
                if day:
                    day_numbers = day.text.strip()
                    element_div = element.find_next(self.tag2, class_='casualties')
                    if element_div:
                        element_text = element_div.text.strip()
                        if element_text:
                            return day_numbers, element_text

        except Exception as e:
            print(f'Something went wrong with datas: {e}')
            return 'Something went wrong with datas: ' + str(e)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/meals')
def meals():
   return render_template('meals.html')

@app.route('/map')
def map():
    parseDatas = ParseDatas(tag='li', tag1='span', tag2='div', url='https://index.minfin.com.ua/ua/russian-invading/casualties/')
    parseDatas.ParseInfo()
    day_numbers, element_text = parseDatas.ParseInfo()
    return render_template('map.html', day_numbers=day_numbers, element_text=element_text)

@app.route('/region', methods=['POST'])
def process_button_click():
    button_id = request.form.get('buttonId')
    print(button_id)

    # These conditions to check real global id of region but in class ParseRegions just we check this exists id
    if button_id == 'Dnipro':
        list_dnipro = ['static/img/dnipro.jpg', 'static/img/dnipro1.jpg', 'static/img/dnipro2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2, parseRegions.button_id)
        return render_template('region.html', img_src=list_dnipro, region_name=region_name, region_info=region_info)


    elif button_id == 'Krim':
        list_krim = ['static/img/first.jpg', 'static/img/second.jpg', 'static/img/third.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_krim, region_name=region_name, region_info=region_info)


    elif button_id == 'Doneck':
        list_doneck = ['static/img/first.jpg', 'static/img/second.jpg', 'static/img/third.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_doneck, region_name=region_name, region_info=region_info)


    elif button_id == 'Zitomer':
        list_zitomer = ['static/img/zhytomer.jpg', 'static/img/zhytomer1.jpg', 'static/img/zhytomer2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_zitomer, region_name=region_name, region_info=region_info)


    elif button_id == 'Karpaty':
        list_karpaty = ['static/img/karpaty.jpg', 'static/img/karpaty1.jpg', 'static/img/karpaty2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_karpaty, region_name=region_name, region_info=region_info)


    elif button_id == 'Zaporiza':
        list_zaporiza = ['static/img/zapor.jpg', 'static/img/zapor1.jpg', 'static/img/zapor2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_zaporiza, region_name=region_name, region_info=region_info)


    elif button_id == 'Frankifsk':
        list_frankifsk = ['static/img/frankifsk.jpg', 'static/img/frankifsk1.jpg', 'static/img/frankifsk2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_frankifsk, region_name=region_name, region_info=region_info)


    elif button_id == 'Kyiv':
        list_kyiv = ['static/img/kyiv.jpg', 'static/img/kyiv1.jpg', 'static/img/kyiv2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_kyiv, region_name=region_name, region_info=region_info)


    elif button_id == 'Vinitsa':
        list_vinitsa = ['static/img/vinitsa.jpg', 'static/img/vinitsa1.jpg', 'static/img/vinitsa2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_vinitsa, region_name=region_name, region_info=region_info)


    elif button_id == 'Volin':
        list_volin = ['static/img/volin.jpg', 'static/img/volin1.jpg', 'static/img/volin2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_volin, region_name=region_name, region_info=region_info)


    elif button_id == 'Kirovograd':
        list_kirovograd = ['static/img/kirovograd.jpg', 'static/img/kirovograd1.jpg', 'static/img/kirovograd2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_kirovograd, region_name=region_name, region_info=region_info)


    elif button_id == 'Luhansk':
        list_luhansk = ['static/img/first.jpg', 'static/img/second.jpg', 'static/img/third.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_luhansk, region_name=region_name, region_info=region_info)


    elif button_id == 'Lviv':
        list_lviv = ['static/img/lviv.jpg', 'static/img/lviv1.jpg', 'static/img/lviv2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_lviv, region_name=region_name, region_info=region_info)


    elif button_id == 'Mikolaiv':
        list_mikolaiv = ['static/img/mikolaiv.jpg', 'static/img/mikolaiv1.jpg', 'static/img/mikolaiv2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_mikolaiv, region_name=region_name, region_info=region_info)


    elif button_id == 'Odessa':
        list_odessa = ['static/img/odessa.jpg', 'static/img/odessa1.jpg', 'static/img/odessa2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_odessa, region_name=region_name, region_info=region_info)


    elif button_id == 'Poltava':
        list_poltava = ['static/img/poltava.jpg', 'static/img/poltava1.jpg', 'static/img/poltava2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_poltava, region_name=region_name, region_info=region_info)


    elif button_id == 'Rivne':
        list_rivne = ['static/img/rivne.jpg', 'static/img/rivne1.jpg', 'static/img/rivne2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_rivne, region_name=region_name, region_info=region_info)


    elif button_id == 'Sumy':
        list_sumy = ['static/img/sumy.jpg', 'static/img/sumy1.jpg', 'static/img/sumy2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_sumy, region_name=region_name, region_info=region_info)


    elif button_id == 'Hmelnickii':
        list_hmelnickii = ['static/img/hmelnickii.jpg', 'static/img/hmelnickii1.jpg', 'static/img/hmelnickii2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_hmelnickii, region_name=region_name, region_info=region_info)


    elif button_id == 'Cherkasi':
        list_cherkasi = ['static/img/cherkasy.jpg', 'static/img/cherkasy1.jpg', 'static/img/cherkasy2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_cherkasi, region_name=region_name, region_info=region_info)


    elif button_id == 'Chernivci':
        list_chernivci = ['static/img/chernivci.jpg', 'static/img/chernivci1.jpg', 'static/img/chernivci2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_chernivci, region_name=region_name, region_info=region_info)


    elif button_id == 'Chernigiv':
        list_chernigiv = ['static/img/chernigiv.jpg', 'static/img/chernigiv1.jpg', 'static/img/chernigiv2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_chernigiv, region_name=region_name, region_info=region_info)


    elif button_id == 'Ternopil':
        list_ternopil = ['static/img/ternopil.jpg', 'static/img/ternopil1.jpg', 'static/img/ternopil2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_ternopil, region_name=region_name, region_info=region_info)


    elif button_id == 'Kharkiv':
        list_kharkiv = ['static/img/harkiv.jpg', 'static/img/harkiv1.jpg', 'static/img/harkiv2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_kharkiv, region_name=region_name, region_info=region_info)


    elif button_id == 'Herson':
        list_herson = ['static/img/herson.jpg', 'static/img/herson1.jpg', 'static/img/herson2.jpg']
        parseRegions = ParseRegions(tag='p', tag1='strong', tag2='br', button_id=button_id)
        region_name, region_info = parseRegions.ParseInfo(parseRegions.tag, parseRegions.tag1, parseRegions.tag2,
                                                          parseRegions.button_id)
        return render_template('region.html', img_src=list_herson, region_name=region_name, region_info=region_info)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
