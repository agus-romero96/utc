import wx

class Calculadora(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Calculadora Básica", size=(300, 300))
        
        panel = wx.Panel(self)
        
        # Campo de entrada para el primer número
        self.num1_label = wx.StaticText(panel, label="Número 1:")
        self.num1_text = wx.TextCtrl(panel)
        
        # Campo de entrada para el segundo número
        self.num2_label = wx.StaticText(panel, label="Número 2:")
        self.num2_text = wx.TextCtrl(panel)
        
        # Cuadro de solo lectura para mostrar el resultado
        self.result_text = wx.TextCtrl(panel, style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.result_text.SetLabel("Resultado:")
        
        # Botón de suma
        suma_btn = wx.Button(panel, label="Sumar")
        suma_btn.Bind(wx.EVT_BUTTON, self.sumar)

        # Botón de resta
        resta_btn = wx.Button(panel, label="Restar")
        resta_btn.Bind(wx.EVT_BUTTON, self.restar)
        
        # Botón de multiplicar
        multiplicar_btn = wx.Button(panel, label="Multiplicar")
        multiplicar_btn.Bind(wx.EVT_BUTTON, self.multiplicar)
        
        # Botón de dividir
        dividir_btn = wx.Button(panel, label="Dividir")
        dividir_btn.Bind(wx.EVT_BUTTON, self.dividir)
        #botón para limpiar los datos
        borrar = wx.Button(panel, label="Borrar")
        borrar.Bind(wx.EVT_BUTTON, self.limpiar)

        # Layout usando BoxSizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.num1_label, flag=wx.ALL, border=5)
        sizer.Add(self.num1_text, flag=wx.EXPAND | wx.ALL, border=5)
        sizer.Add(self.num2_label, flag=wx.ALL, border=5)
        sizer.Add(self.num2_text, flag=wx.EXPAND | wx.ALL, border=5)
        sizer.Add(wx.StaticText(panel, label="Resultado:"), flag=wx.ALL, border=5)
        sizer.Add(self.result_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        sizer.Add(suma_btn, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(resta_btn, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(multiplicar_btn, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(dividir_btn, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(borrar, flag=wx.ALL | wx.ALIGN_CENTER, border=5)
        sizer.Add(wx.StaticText(panel, label=""), flag=wx.ALL, border=5)  # Agrega un espacio en blanco
        panel.SetSizer(sizer)

        # Configuración del acelerador de teclado
        accel_tbl = wx.AcceleratorTable([
            (wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('S'), suma_btn.GetId()),
            (wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('R'), resta_btn.GetId()),
            (wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('M'), multiplicar_btn.GetId()),
            (wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('D'), dividir_btn.GetId()),
            (wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('B'), borrar.GetId())
        ])
        self.SetAcceleratorTable(accel_tbl)

    def obtener_valores(self):
        try:
            num1 = float(self.num1_text.GetValue())
            num2 = float(self.num2_text.GetValue())
            return num1, num2
        except ValueError:
            self.result_text.SetValue("Error: Por favor ingresa números válidos.")
            self.result_text.SetFocus()
            return None, None

    def sumar(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 + num2
            self.result_text.SetValue(f"Suma: {resultado}")
            self.result_text.SetFocus()

    def restar(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 - num2
            self.result_text.SetValue(f"Resta: {resultado}")
            self.result_text.SetFocus()

    # Función para multiplicar
    def multiplicar(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 * num2
            self.result_text.SetValue(f"Multiplicación: {resultado}")
            self.result_text.SetFocus()

    # Función para dividir
    def dividir(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                self.result_text.SetValue("Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
                self.result_text.SetValue(f"División: {resultado}")
            self.result_text.SetFocus()
    #función para limpiar los cuadros de edición y el cuadro de resultados
    def limpiar(self, event):
        self.num1_text.Clear()
        self.num2_text.Clear()
        self.result_text.Clear()
        #enfoca el cuadro de edición
        self.num1_text.SetFocus()
app = wx.App()
frame = Calculadora()
frame.Show()
app.MainLoop()
