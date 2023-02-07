class Frame:
    def __init__(self,seqno,data):
        self.seqno=seqno
        self.data=data

def sort(frames):
    n=len(frames)
    for i in range(n-1):
        if(frames[i].seqno>frames[i+1].seqno):
            frames[i],frames[i+1]=frames[i+1],frames[i]

n=int(input("Enter the number of frames: "))

frames = []

for i in range(n):
    seqno=int(input("Enter the sequence of Frame no {}: ".format(i+1)))
    data=int(input("Enter the data: "))
    frames.append(Frame(seqno,data))

sort(frames)

print("The sorted frames is: ")
for i in range(n):
    print("Seq no {} : Data {} ".format(frames[i].seqno,frames[i].data))