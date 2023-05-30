from googletrans import Translator

destination_translation = input('Enter code for destination translation (refer README file for the same): ')

# Open the file in read mode
intput_file = open('app_en.arb', 'r')

# Create a translator object
translator = Translator()
# Define the text to translate

# Translate the text from English to French
def translate_text(text):
    try:
        return translator.translate(text, dest=destination_translation).text
    except:
        print('Enables to translate file')

def format_lines_to_list(original_text):
    #  ex: "appName" : "Demo app",
    # split on basis of :
    ls = original_text.split(":")
    result = []
    for item in ls:
        st = item.strip().replace('"', '')
        comma = ','
        index = st.rfind(comma)
        if index != -1:
            st = st[:index] + '' + st[index+1:]
        result.append(st)
    return result

# Open a file in write mode
output_file = open(f"app_{destination_translation}.arb", "w")

print("Translating code...")

for line in intput_file:
    fl = format_lines_to_list(line)
    for item in fl:
        if '{' in item or '}' in item:
            output_file.write(item + '\n')
            break
        elif '@@' in item:
            output_file.write(f'  "@@locale": "{destination_translation}",\n')
            break
        else:
            output_file.write(f'  "{fl[0]}": "{translate_text(fl[1])}",\n')
            break


print("Translating complete :)")

# Close the file
intput_file.close()
output_file.close()
