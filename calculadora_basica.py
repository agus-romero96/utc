import wx

class CalculadoraBasica(wx.Frame):
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
        
        # Botones para cada operación
        suma_btn = wx.Button(panel, label="&Sumar")
        suma_btn.Bind(wx.EVT_BUTTON, self.sumar)
        
        resta_btn = wx.Button(panel, label="&Restar")
        resta_btn.Bind(wx.EVT_BUTTON, self.restar)
        
        multiplicar_btn = wx.Button(panel, label="&Multiplicar")
        multiplicar_btn.Bind(wx.EVT_BUTTON, self.multiplicar)
        
        dividir_btn = wx.Button(panel, label="&Dividir")
        dividir_btn.Bind(wx.EVT_BUTTON, self.dividir)
        
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
        
        panel.SetSizer(sizer)
        
    def obtener_valores(self):
        try:
            num1 = float(self.num1_text.GetValue())
            num2 = float(self.num2_text.GetValue())
            return num1, num2
        except ValueError:
            self.result_text.SetValue("Error: Por favor ingresa números válidos.")
            self.result_text.SetFocus()  # Enfoca el cuadro de resultado en caso de error
            return None, None
    
    def sumar(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 + num2
            self.result_text.SetValue(f"Suma: {resultado}")
            self.result_text.SetFocus()  # Enfoca el cuadro de resultado
    
    def restar(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 - num2
            self.result_text.SetValue(f"Resta: {resultado}")
            self.result_text.SetFocus()  # Enfoca el cuadro de resultado
    
    def multiplicar(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            resultado = num1 * num2
            self.result_text.SetValue(f"Multiplicación: {resultado}")
            self.result_text.SetFocus()  # Enfoca el cuadro de resultado
    
    def dividir(self, event):
        num1, num2 = self.obtener_valores()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                self.result_text.SetValue("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                self.result_text.SetValue(f"División: {resultado}")
            self.result_text.SetFocus()  # Enfoca el cuadro de resultado

app = wx.App()
frame = CalculadoraBasica()
frame.Show()
app.MainLoop()
