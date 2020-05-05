Option Explicit
Dim input1, input2, sign, x

x = MsgBox("Hi! I am Ronik...Here's my script to perform calculations between 2 numbers",0,"Calculator")
input1 = inputbox ("Type in your first number","Calculator(num1)")
sign = inputbox ("Type in the symbol for your equation","Calculator(operators: '+', '-', '*', '/', '^')")
input2 = inputbox ("Type in your second number","Calculator(num2)")


	If sign = "+" Then
	msgbox input1 -- input2

	ElseIf sign = "-" Then
	msgbox input1 - input2

	ElseIf sign = "*" Then
	msgbox input1 * input2

	ElseIf sign = "/" Then
	msgbox input1 / input2

	ElseIf sign = "^" Then
	msgbox input1 ^ input2

	Else
	msgBox "Make sure what you typed in the equation box is correct. You can use the symbols: + - * / ^"

End If