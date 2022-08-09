import os
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import time
import win32con
import win32api

class win():
    def __init__(self):
        self.sal = []
        self.root = Tk()
        ancho_ventana = 600
        alto_ventana = 460

        x_ventana = self.root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root.geometry(posicion)

        self.root.title("URLocker V0.4.1")
        self.root.config(bg="#262335")
        x=open('rutas.txt','a+')
        x.close()
        with open('rutas.txt', 'r') as f:
            # with open('./preferencias.txt', 'r') as f:
            lineas = [linea.split() for linea in f]
        for linea in lineas:
            self.sal.append(linea)
        print (len(self.sal))
        if (len(self.sal))==0:
            messagebox.showwarning(message="Archivo Vacio")
            self.tl=Toplevel()
            self.tl.geometry("350x600")
            self.tl.config(bg="#262335")
            Label(self.tl,text="Inserta rutas",bg="#262335",fg="white",font=("Arial,18")).place(x=5,y=5)

            self.txop = scrolledtext.ScrolledText(self.tl, undo=True,width=35,height=25)
            self.txop['font'] = ('consolas', '12')
            self.txop.place(x=5,y=40)
            btng=Button(self.tl,text="Generar",command=self.llenado,bg="#129265",width=37,fg="white", font=("Arial,12"))
            btng.place(x=5,y=550)
            self.tl.mainloop()


        Label(self.root,bg="#262335",fg="white",text="_________________________________________________________________________________________________________________________").place(x=-5,y=40)

        Label(self.root,text="URL",bg="#262335",fg="white",font=("Arial,12"))
        self.url=Entry(self.root)
        add=Button(self.root,text="CREAR",command=self.agregar,bg="#7B88A1",width=14,fg="white", font=("Arial,12"))
        add.place(x=10,y=8)

        wd = Button(self.root, text="Desactivar Defender", command=self.wd, bg="#FFB92D", width=16, fg="white",
                     font=("Arial,12"))
        wd.place(x=160, y=8)

        wd2 = Button(self.root, text="Activar Defender", command=self.wd2, bg="#1BDB98", width=14, fg="white",
                    font=("Arial,12"))
        wd2.place(x=325, y=8)

        op=Button(self.root, text="Abrir ruta 🗀", command=self.abrut, bg="#FFD96A", width=12, fg="white",
                    font=("Arial,12"))
        op.place(x=475, y=8)




        posy=60
        posx=5
        c=0
        d=0
        for i in range(len(self.sal)):
            if i<26:
                if c>=13 and c<=25:
                    posx=150
                    if d==0:
                        posy=60
                        d=1
                Label(self.root, bg="#262335",justify=LEFT, fg="white",text=self.sal[i]).place(x=posx, y=posy)
                posy+=25
                c+=1

            if i==26:
                c = 0
                posx=300
                posy=60
            if i>26 and i<40:
                if c>=13 and c<=25:
                    posx=450
                    if d==1:
                        posy=60
                        d=2
                Label(self.root, bg="#262335",justify=LEFT, fg="white",text=self.sal[i]).place(x=posx, y=posy)
                posy+=25
                c+=1
            if i==40:
                c = 0
                posx=450
                posy=60
            if i>41 and i<54:
                if c>=13 and c<=25:
                    posx=600
                    if d==1:
                        posy=60
                        d=2
                Label(self.root, bg="#262335",justify=LEFT, fg="white",text=self.sal[i]).place(x=posx, y=posy)
                posy+=25
                c+=1
            if i==54:
                Label(self.root, bg="#262335",justify=LEFT, fg="white", text="...").place(x=posx, y=posy)



        Label(self.root,bg="#262335",fg="white",text="______________________________________________________________________________________________________________________").place(x=-5,y=380)
        self.btn=Button(self.root,state=DISABLED,text="BLOQUEAR URL's",command=self.comando,bg="#2B7CD3",fg="white",width=16, font=("Arial,12"))
        self.btn.place(x=10,y=410)

        rem = Button(self.root, text="Liberar archivo", command=self.abe, bg="#1ED760", width=12, fg="white",
                     font=("Arial,12"))
        rem.place(x=170,y=410)

        rem2 = Button(self.root, text="Ocultar 👁", command=self.abe2, bg="#57267E", width=8, fg="white",
                     font=("Arial,12"))
        rem2.place(x=295, y=410)

        rem3 = Button(self.root, text="Bloquear 🔐", command=self.abe3, bg="#FF2B2B", width=10, fg="white",
                      font=("Arial,12"))
        rem3.place(x=385, y=410)

        op2 = Button(self.root, text="Borrar 🗑️", command=self.borra, bg="#D92424", width=10, fg="white",
                    font=("Arial,12"))
        op2.place(x=490, y=410)



        self.root.mainloop()

    def abrut(self):
        RUTA_CARPETA = "C:/Windows/System32/drivers/etc/"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
    def abrarc(self):
        import subprocess

        # Abre el archivo 'hosts' con Notepad.
        NOTEPAD = ["C:/WINDOWS/system32/notepad.exe", "C:/Windows/System32/drivers/etc/hosts"]
        PROCESO_1 = subprocess.Popen(NOTEPAD, stdout=subprocess.PIPE)
    def abe2(self):
        try:
            file = "C:\Windows\System32\drivers\etc\hosts"
            win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_HIDDEN)
            messagebox.showinfo(message="El archivo HOST ha sido ocultado")
        except:
            messagebox.showerror(message="No pudimos ocultar el archivo, puede que no tengamos los permisos o el archivo no exista")

    def abe(self):

        try:
            file = "C:\Windows\System32\drivers\etc\hosts"
            win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_NORMAL)
            messagebox.showinfo(message="El archivo HOST ha sido desbloqueado, puede ser modificado y es visible")
        except:
            messagebox.showerror(message="No pudimos desbloquear el archivo, puede que no tengamos los permisos o el archivo no exista")
    def abe3(self):

        try:
            file = "C:\Windows\System32\drivers\etc\hosts"
            win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_READONLY)
            messagebox.showinfo(message="El archivo HOST ha sido bloqueado")
        except:
            messagebox.showerror(message="No pudimos bloquear el archivo, puede que no tengamos los permisos o el archivo no exista")
        #keyboard.press_and_release('alt+f4')


    def borra(self):
        answer = messagebox.askyesno(message='Seguro que deseas eliminar el archivo HOST?')
        if answer:
            try:
                os.remove("C:\Windows\System32\drivers\etc\hosts")
                messagebox.showinfo(message="El archivo host ha sido eliminado")
            except:
                messagebox.showerror(message="No se pudo eliminar el archivo HOST")
        else:
            messagebox.showinfo(message="El archivo no fue eliminado")
    def wd(self):
        import subprocess
        try:
            subprocess.check_call('netsh.exe advfirewall set publicprofile state off')
            messagebox.showinfo(message="Windows Defender ha sido desactivado")


        except:
            messagebox.showerror(message="Windows Defender no realizó el cambio")

    def wd2(self):
        import subprocess
        try:
            subprocess.check_call('netsh.exe advfirewall set publicprofile state on')
            messagebox.showinfo(message="Windows Defender ha sido Activado")


        except:
            messagebox.showerror(message="Windows Defender no realizó el cambio")

    def comando(self):
        try:
            os.startfile(r"bloqueo.vbs")
            time.sleep(1)
            os.remove("bloqueo.vbs")
            self.btn.config(state=DISABLED)
        except:
            messagebox.showerror(message="No se pudo realizar la accion, asegura apagar tu antivirus o liberar el archivo")
    def comando2(self):
        os.startfile(r"desbloqueo.vbs")
        time.sleep(1)
        os.remove("desbloqueo.vbs")
        messagebox.showinfo(title="OK",message="DIRECCIONES DESBLOQUEADAS")
        exit()

    def agregar(self):
        self.generar()

    def generar2(self):
        nombre_archivo = "desbloqueo.vbs"
        cod='''
        Set obj = createobject("Scripting.FileSystemObject")
        Dim filename1
        filename1="C:\WINDOWS\system32\drivers\etc\hosts"
        obj.DeleteFile filename1
        Set obj=Nothing
        '''
        with open(nombre_archivo, "w") as archivo:
            archivo.write(cod)
        # No olvides cerrar el archivo
        archivo.close()

        self.comando2()


    def generar(self):
        nombre_archivo = "bloqueo.vbs"
        pl2=""
        pl=""

        for i in self.sal:
            pl2='"'+str(i)+'",'
            pl+=pl2
        pl=pl[:-1]
        pl=pl.replace("['","")
        pl=pl.replace("']","")
        p1="WebsitesToBlock = Array("+pl+")"
        p2='''If WScript.Arguments.length =0 Then
	Set objShell = CreateObject("Shell.Application")
	objShell.ShellExecute "wscript.exe", Chr(34) & WScript.ScriptFullName & Chr(34) & " RunAsAdministrator", "", "runas", 1
Else
	Const ForReading = 1, ForWriting = 2	
	Set shell = CreateObject("WScript.Shell")    
	root = shell.ExpandEnvironmentStrings("%systemroot%")     
	hostFile = root & "\system32\drivers\etc\hosts"
	tempFile = hostFile & ".bak"
	blocked = 0
	towrite = false
	Set fso = CreateObject("Scripting.FileSystemObject")
	Set f1 = fso.OpenTextFile(hostFile, ForReading, True)
	Set f2 = fso.OpenTextFile(tempFile, ForWriting, True)
	Do Until f1.AtEndOfStream
		line = f1.Readline
		towrite = true
		For Each URL in WebsitesToBlock
			If instr(line, URL) Then
				If blocked = 0 Then 
					If left(line, 1) = "#" Then blocked = 1 Else blocked = 2
				End If
			towrite = false
			End If
		Next	
		If towrite Then f2.WriteLine line
	Loop
	For Each URL in WebsitesToBlock
		If blocked <> 2 Then
			f2.WriteLine "127.0.0.1" & vbTab & vbTab & URL 
		End If
	Next
	fso.Copyfile root & "\system32\drivers\etc\hosts.bak", root & "\system32\drivers\etc\hosts" , True
	f1.Close
	f2.Close

	If blocked = 2 Then 
	WScript.echo "Ningún dominio esta bloqueado" 
	Else
	WScript.echo "Los dominios especificados ahora se han bloqueado" 
	End If
End If'''
        with open(nombre_archivo, "w") as archivo:
            archivo.write(p1+"\n")
            archivo.write(p2)
        # No olvides cerrar el archivo
        archivo.close()

        self.btn.config(state=NORMAL)
        messagebox.showinfo(message="Archivo generado")

    def llenado(self):
        tx=self.txop.get(1.0, END)
        with open("rutas.txt", "w+") as archivo:
            archivo.write(tx)
        # No olvides cerrar el archivo
        archivo.close()
        self.tl.destroy()
        self.root.destroy()

        win()