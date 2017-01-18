from Tkinter import *
from tkFileDialog   import askopenfilename,asksaveasfile
from DNA_sequence import *
from global_align import *


root = Tk()
root.title("Sequence Alignment Program")



# First text widget for sequence1 to align
LabelSequence1 = Label(root, text="Enter a First DNA or Protein sequence").grid(row=0,column=0, sticky=W,pady=5)

Sequence1=Text(root)
scroll1L = Scrollbar(root,command=Sequence1.yview)
scroll1B = Scrollbar(root,orient=HORIZONTAL,command=Sequence1.xview)
scroll1L.grid(row=1,column=2, sticky=N+S+E)
scroll1B.grid(row=2,column=0,columnspan=2, sticky=W+E+S)

Sequence1.config( wrap=NONE, xscrollcommand=scroll1B.set, yscrollcommand=scroll1L.set)
Sequence1.grid(row=1,column=0,columnspan=2)

quote = """>Example
ATGC"""
Sequence1.insert(END, quote)



# Second text widget for sequence2  to align
LabelSequence2 = Label(root, text="Enter a Second DNA or Protein sequence").grid(row=3,column=0, sticky=W,pady=5)
Sequence2 = Text(root)

scroll2L = Scrollbar(root,command=Sequence2.yview)
scroll2B = Scrollbar(root,orient=HORIZONTAL,command=Sequence2.xview)
scroll2L.grid(row=4,column=2, sticky=N+S+E)
scroll2B.grid(row=5,column=0,columnspan=2, sticky=W+E+S)

Sequence2.config( wrap=NONE, xscrollcommand=scroll2B.set, yscrollcommand=scroll2L.set)
Sequence2.grid(row=4,column=0,columnspan=2)



# Third text widget to display the result
LabelSequence3 = Label(root, text="Result of the Alignment").grid(row=0,column=3, sticky=W,pady=5)
Sequence3=Text(root, width=60)

scroll3L = Scrollbar(root,command=Sequence3.yview)
scroll3L.grid(row=1,column=4, sticky=N+S+E)
Sequence3.config(yscrollcommand=scroll3L.set)
Sequence3.grid(row=1,column=3,pady=5)



# HERE IS THE COMMAND FOR SUBMIT BUTTON
# THE ONE WHO DOES THE ALIGNMENT
def submission():
	root.config(cursor="watch")
	root.update()
	SequenceA=FastaDNA(Sequence1.get("1.0",END).rstrip()).sequence
	SequenceB=FastaDNA(Sequence2.get("1.0",END).rstrip()).sequence
	Result=Alignment(SequenceA,SequenceB)
	Sequence3.insert(END, Result)
	return root.config(cursor="")

# Clear function to remove all text from text_widgets
def clear():
	Sequence1.delete('1.0', END)
	Sequence2.delete('1.0', END)
	Sequence3.delete('1.0', END)

# Allow to upload a sequence from a text file with FASTA format
def upload1():
	file_name= askopenfilename()
	fasta=open(file_name,'r').read()
	Sequence1.delete('1.0', END)
	Sequence1.insert(END, fasta)

def upload2():
	file_name= askopenfilename()
	fasta=open(file_name,'r').read()
	Sequence2.insert(END, fasta)

# Allow to export the alignment in a text file.
def export():
    name=asksaveasfile(mode='w',defaultextension=".txt")
    text2save=str(Sequence3.get('1.0',END))
    name.write(text2save)
    name.close()


# Submit button
submit=Button(root, text="submit",bg="lightblue",command=submission).grid(row=6,column=0,sticky=S)

# Clear button
clear=Button(root, text="clear",bg="lightblue",command=clear).grid(row=6,column=1)

# Save alignment as a file
LabelSave = Label(root, text="Export result as a text file").grid(row=3,column=3,pady=5)
save=Button(root, text="export",bg="lightblue",command=export).grid(row=4,column=3,sticky=N)

# Upload sequence1
upload1=Button(root, text="upload sequence",command=upload1).grid(row=0,column=1)
# Upload sequence2
upload2=Button(root, text="upload sequence",command=upload2).grid(row=3,column=1)


root.mainloop()