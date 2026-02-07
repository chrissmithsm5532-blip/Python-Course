import FreeSimpleGUI as Sg

label1 =Sg.Text("Select File to Compress")
label2 =Sg.Text("Select Destination Folder")
input_box1 = Sg.InputText(tooltip = "Select File")
input_box2 = Sg.InputText(tooltip = "Destination Folder")
add_button1 =  Sg.Button("Choose")
add_button2 =  Sg.Button("Choose")
compress_button = Sg.Button("Compress")

window = Sg.Window("File Zipper",layout= [[label1,input_box1,add_button1],[label2,input_box2,add_button2],[compress_button]])
window.read()
window.close()