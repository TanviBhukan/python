class TextProcessor:
    def Get_String(self):
        self.myStr = input("Enter any String: ")
    
    def Reverse_String(self):
        s = self.myStr
        cnt = len(s)
        i = cnt - 1
        revStr = ""
        while i >= 0:
            revStr += s[i]
            i -= 1
        print("String in Reverse:", revStr)

# main body
sniz = TextProcessor()
bliz = TextProcessor()

sniz.Get_String()
sniz.Reverse_String()

bliz.Get_String()
bliz.Reverse_String()
