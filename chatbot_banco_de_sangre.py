import os
import time

class ChatbotBancoSangre:
    def __init__(self):
        self.idioma = None
        self.textos = {
            'es': {
                'bienvenida': '🩸 SISTEMA DE BANCO DE SANGRE - PUERTO RICO 🩸',
                'seleccionar_idioma': 'Por favor selecciona tu idioma / Please select your language:',
                'opcion_1': '1. Español',
                'opcion_2': '2. English',
                'idioma_invalido': 'Opción inválida. Por favor selecciona 1 o 2.',
                'saludo': '¡Hola! Soy tu asistente virtual del Sistema de Banco de Sangre.',
                'menu_principal': '''
¿En qué puedo ayudarte hoy?

1. 📋 Información sobre donación de sangre
2. 🔍 Consultar inventario de sangre
3. 👥 Registrar nuevo donante
4. 📊 Ver estadísticas del laboratorio
5. ❓ Ayuda y soporte
6. 🌐 Cambiar idioma
7. 🚪 Salir del sistema

Escribe el número de tu opción:''',
                'opcion_1_resp': 'La donación de sangre es un acto voluntario que salva vidas. Requisitos básicos:\n- Edad: 18-65 años\n- Peso mínimo: 110 libras\n- Buena salud general',
                'opcion_2_resp': 'Consultando inventario... Esta función se conectará con la base de datos del laboratorio.',
                'opcion_3_resp': 'Iniciando proceso de registro de donante... Será dirigido al formulario correspondiente.',
                'opcion_4_resp': 'Mostrando estadísticas del laboratorio... Esta sección mostrará gráficos y reportes.',
                'opcion_5_resp': 'Para ayuda técnica, contacte al administrador del sistema o consulte el manual de usuario.',
                'despedida': '¡Gracias por usar nuestro sistema! Que tengas un excelente día.',
                'opcion_invalida': 'Opción no válida. Por favor selecciona un número del 1 al 7.',
                'continuar': 'Presiona Enter para continuar...',
                'cambiar_idioma': 'Idioma cambiado exitosamente.',
                'volver_menu': '\n0. ← Volver al menú principal\n9. 🌐 Cambiar idioma\n'
            },
            'en': {
                'bienvenida': '🩸 BLOOD BANK SYSTEM - PUERTO RICO 🩸',
                'seleccionar_idioma': 'Por favor selecciona tu idioma / Please select your language:',
                'opcion_1': '1. Español',
                'opcion_2': '2. English',
                'idioma_invalido': 'Invalid option. Please select 1 or 2.',
                'saludo': 'Hello! I am your virtual assistant for the Blood Bank System.',
                'menu_principal': '''
How can I help you today?

1. 📋 Blood donation information
2. 🔍 Check blood inventory
3. 👥 Register new donor
4. 📊 View laboratory statistics
5. ❓ Help and support
6. 🌐 Change language
7. 🚪 Exit system

Enter your option number:''',
                'opcion_1_resp': 'Blood donation is a voluntary act that saves lives. Basic requirements:\n- Age: 18-65 years\n- Minimum weight: 110 pounds\n- Good general health',
                'opcion_2_resp': 'Checking inventory... This function will connect to the laboratory database.',
                'opcion_3_resp': 'Starting donor registration process... You will be directed to the corresponding form.',
                'opcion_4_resp': 'Displaying laboratory statistics... This section will show charts and reports.',
                'opcion_5_resp': 'For technical help, contact the system administrator or check the user manual.',
                'despedida': 'Thank you for using our system! Have a great day.',
                'opcion_invalida': 'Invalid option. Please select a number from 1 to 7.',
                'continuar': 'Press Enter to continue...',
                'cambiar_idioma': 'Language changed successfully.',
                'volver_menu': '\n0. ← Back to main menu\n9. 🌐 Change language\n'
            }
        }
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_bienvenida(self):
        """Muestra la pantalla de bienvenida"""
        self.limpiar_pantalla()
        print("=" * 60)
        print(self.textos['es']['bienvenida'].center(60))
        print("=" * 60)
        print()
    
    def seleccionar_idioma(self):
        """Permite al usuario seleccionar el idioma"""
        while True:
            print(self.textos['es']['seleccionar_idioma'])
            print()
            print(self.textos['es']['opcion_1'])
            print(self.textos['es']['opcion_2'])
            print()
            
            opcion = input("Opción / Option: ").strip()
            
            if opcion == '1':
                self.idioma = 'es'
                break
            elif opcion == '2':
                self.idioma = 'en'
                break
            else:
                print()
                print(self.textos['es']['idioma_invalido'])
                print()
                time.sleep(2)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del chatbot"""
        while True:
            self.limpiar_pantalla()
            print("=" * 60)
            print(self.textos[self.idioma]['bienvenida'].center(60))
            print("=" * 60)
            print()
            print(self.textos[self.idioma]['saludo'])
            print(self.textos[self.idioma]['menu_principal'])
            
            opcion = input().strip()
            
            if opcion == '1':
                self.mostrar_info_donacion()
            elif opcion == '2':
                self.consultar_inventario()
            elif opcion == '3':
                self.registrar_donante()
            elif opcion == '4':
                self.ver_estadisticas()
            elif opcion == '5':
                self.mostrar_ayuda()
            elif opcion == '6':
                self.cambiar_idioma_menu()
            elif opcion == '7':
                self.despedirse()
                break
            else:
                print()
                print(self.textos[self.idioma]['opcion_invalida'])
                input(self.textos[self.idioma]['continuar'])
    
    def cambiar_idioma_menu(self):
        """Cambia el idioma desde el menú principal"""
        print()
        print("-" * 50)
        self.seleccionar_idioma()
        print()
        print(self.textos[self.idioma]['cambiar_idioma'])
        time.sleep(1)
    
    def mostrar_opciones_navegacion(self):
        """Muestra opciones para volver al menú o cambiar idioma"""
        print(self.textos[self.idioma]['volver_menu'])
        
        while True:
            opcion = input("Opción: ").strip()
            if opcion == '0':
                return 'menu'
            elif opcion == '9':
                return 'idioma'
            else:
                print(self.textos[self.idioma]['opcion_invalida'])
    
    def mostrar_info_donacion(self):
        """Muestra información sobre donación de sangre"""
        while True:
            print()
            print("-" * 50)
            print(self.textos[self.idioma]['opcion_1_resp'])
            print("-" * 50)
            
            accion = self.mostrar_opciones_navegacion()
            if accion == 'menu':
                break
            elif accion == 'idioma':
                self.cambiar_idioma_modulo()
    
    def consultar_inventario(self):
        """Función para consultar inventario (placeholder)"""
        while True:
            print()
            print("-" * 50)
            print(self.textos[self.idioma]['opcion_2_resp'])
            print("-" * 50)
            
            accion = self.mostrar_opciones_navegacion()
            if accion == 'menu':
                break
            elif accion == 'idioma':
                self.cambiar_idioma_modulo()
    
    def registrar_donante(self):
        """Función para registrar donante (placeholder)"""
        while True:
            print()
            print("-" * 50)
            print(self.textos[self.idioma]['opcion_3_resp'])
            print("-" * 50)
            
            accion = self.mostrar_opciones_navegacion()
            if accion == 'menu':
                break
            elif accion == 'idioma':
                self.cambiar_idioma_modulo()
    
    def ver_estadisticas(self):
        """Función para ver estadísticas (placeholder)"""
        while True:
            print()
            print("-" * 50)
            print(self.textos[self.idioma]['opcion_4_resp'])
            print("-" * 50)
            
            accion = self.mostrar_opciones_navegacion()
            if accion == 'menu':
                break
            elif accion == 'idioma':
                self.cambiar_idioma_modulo()
    
    def mostrar_ayuda(self):
        """Muestra información de ayuda"""
        while True:
            print()
            print("-" * 50)
            print(self.textos[self.idioma]['opcion_5_resp'])
            print("-" * 50)
            
            accion = self.mostrar_opciones_navegacion()
            if accion == 'menu':
                break
            elif accion == 'idioma':
                self.cambiar_idioma_modulo()
    
    def cambiar_idioma_modulo(self):
        """Cambia el idioma desde cualquier módulo"""
        print()
        print("-" * 50)
        self.seleccionar_idioma()
        print()
        print(self.textos[self.idioma]['cambiar_idioma'])
        time.sleep(1)
    
    def despedirse(self):
        """Muestra mensaje de despedida"""
        print()
        print(self.textos[self.idioma]['despedida'])
        time.sleep(2)
    
    def iniciar(self):
        """Función principal que inicia el chatbot"""
        self.mostrar_bienvenida()
        self.seleccionar_idioma()
        self.mostrar_menu_principal()

# Función principal para ejecutar el programa
def main():
    chatbot = ChatbotBancoSangre()
    chatbot.iniciar()

# Ejecutar el programa si se llama directamente
if __name__ == "__main__":
    main()
