class node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class PrefixCodeTree():
    def __init__(self):
        self.root = node("")

    def insert(self, codeword, symbol):
        tmp = self.root
        # 1 nằm bên nhánh phải
        # 0 nằm bên nhánh trái
        for i in range(0, len(codeword)):
            if i == len(codeword) - 1:
                if codeword[i] == 0:
                    tmp.left = node(symbol)
                elif codeword[i] == 1:
                    tmp.right = node(symbol)
            else:
                if codeword[i] == 0:
                    if tmp.left is None:
                        tmp.left = node("")
                    tmp = tmp.left
                elif codeword[i] == 1:
                    if tmp.right is None:
                        tmp.right = node("")
                    tmp = tmp.right

    def decode(self, encodedData, datalen):
        # Duyệt cây
        bitstring = "".join(f"{byte:0>8b}" for byte in encodedData)[:datalen]
        message = ""
        tmp = self.root
        for bit in bitstring:
            if int(bit) == 0:
                tmp = tmp.left
            elif int(bit) == 1:
                tmp = tmp.right

            if tmp.name != "":
                message += tmp.name
                tmp = self.root
        return message
