class Frame:
    def __init__(self,seqno,data):
        self.seqno=seqno
        self.data=data

def sort(frames):
    n = len(frames)
    for i in range(n-1):
        for j in range(n-i-1):
            if frames[j].seqno > frames[j+1].seqno:
                frames[j], frames[j+1] = frames[j+1], frames[j]

n=int(input("Enter the number of frames: "))

frames = []

for i in range(n):
    seqno=int(input("Enter the sequence number: "))
    data=int(input("Enter the data: "))
    frames.append(Frame(seqno,data))

sort(frames)

print("The sorted frame order is ")
for i in range(n):
    print("Seqno {} : Data {} ".format(frames[i].seqno,frames[i].data))
