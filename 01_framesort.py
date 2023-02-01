class Frame:
    def __init__(self,seqNo,data):
        self.seqNo=seqNo
        self.data=data


def bubblesort(frames,n):
    for i in range(0,n):
        for j in range(i, n-1):
            if(frames[j].seqNo > frames[j+1].seqNo):
                temp=frames[j]
                frames[j]=frames[j+1]
                frames[j+1]=temp

n=int(input("Enter the number of frames: "))
frames = []
for i in range(0,n):
    seqNo=int(input("Enter the sequence number {}: ".format(i+1)))
    data=int(input("Enter the frame data for sequence number {}: ".format(i+1)))
    frames.append(Frame(seqNo, data))


bubblesort(frames,n)

print("Sorted frames")
for i in range(n):
    print("{} : {}".format(frames[i].seqNo,frames[i].data))