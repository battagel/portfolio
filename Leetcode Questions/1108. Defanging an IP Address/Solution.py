class Solution(object):

	# Defanging is the process of removing potentially harmful links for example http:// changes to hxxp://

    def defangIPaddr(self, address):


        # Create blank variable
        new_address = ""
        
        # Search each char for a "."
        for char in address:
            if char == ".":
                # Replace with defanged char
                new_address += "[.]"
            
            # If char isnt "." then just append to string
            else:
                new_address += char
        return new_address