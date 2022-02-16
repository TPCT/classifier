class arrangement:
    def __del__(self):
        try:
            self.file_descriptor.close()
        except:
            pass
        
    def __init__(self, text_file_path):
        try:
            print("[+] trying to open the required file in reading mode.")
            self.file_descriptor = open(text_file_path, "r")
            print("[+] the required file has been open successfully")
        except Exception as e:
            print(f"[-] an error occurred while trying to open the required file.\n\t [+] error: {e}")
            self.file_descriptor = None    
        self.json_content = []
            
    def convert_to_json(self):
        print("[+] trying to convert the file to json.")
        if not self.file_descriptor:
            print("[-] an error occurred while trying to read from the file descriptor.\n\t [+] error: can't read data from None {self.file_descriptor is None}")
            return False
        print("[+] trying to parse the file to be classified.")
        for line in self.file_descriptor:
            line = line.strip()
            if line:
                line = line.split(" ")
                try:
                    print(f"\t[+] trying to parse {line}")
                    json_dict = {
                        'text': line[0],
                        'x': float(line[1]),
                        'y': float(line[2])
                    }
                    print(f"\t[+] the required line has been parsed successfully. -> {json_dict}")
                    self.json_content.append(json_dict)
                except Exception as e:
                    print(f"\t[-] an error occurred while trying to parse the line -> {line}.\n\t [+] error: {e}")
        print("[+] done parsing the file.")
    
    def arrange(self):
        json_content_length = self.json_content.__len__()
        # arrangement according to y.
        print("[+] trying arrange the according to y.")
        for i in range(json_content_length):
            min_scalar = self.json_content[i]
            for j in range(i+1, json_content_length):
                if min_scalar['y'] > self.json_content[j]['y']:
                    self.json_content[i] = self.json_content[j]
                    self.json_content[j] = min_scalar
                    min_scalar = self.json_content[i]
        
        # arrangement according to x.
        print("[+] trying arrange the according to x.")
        for i in range(json_content_length):
            min_scalar = self.json_content[i]
            for j in range(i+1, json_content_length):
                if min_scalar['y'] >= self.json_content[j]['y'] and min_scalar['x'] > self.json_content[j]['x']:
                    self.json_content[i] = self.json_content[j]
                    self.json_content[j] = min_scalar
                    min_scalar = self.json_content[i]            

        return self.json_content        
    
    
if __name__ == "__main__":
    classifier = arrangement('./out2.txt')
    classifier.convert_to_json()
    print(classifier.arrange())
