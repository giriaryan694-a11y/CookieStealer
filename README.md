# 🍪CookieStealer
---

## ⚡ Overview
This project is a **demonstration tool** designed to **educate about the potential impact of XSS (Cross-Site Scripting) attacks on cookies**.  

This project is a demonstration tool designed to educate about the potential impact of XSS (Cross-Site Scripting) attacks on cookies. It can generate payloads that simulate stealing or revealing cookies in a controlled XSS-vulnerable environment.

> **Important:** This tool **does NOT target real users** or websites without permission. It is intended **only for educational labs and legal pentesting environments**.

With this tool, you can:  
- Understand how XSS vulnerabilities can **access cookie data**.  
- Learn why **proper input validation and cookie security flags** are critical.  
- Simulate XSS impact **safely in controlled environments** (e.g., [VulnWeb Labs](http://testphp.vulnweb.com/)).

---

## ⚠️ Legal Notice
Using this tool on websites **without explicit permission is illegal** and considered **unauthorized access** under computer crime laws in most countries.  

**You MUST:**
- Only run this tool on sites you **own, have permission to test, or public pentesting labs**.
- Use this tool **responsibly and ethically**.

**Consequences of misuse** may include:
- Criminal charges or fines.
- Civil lawsuits.
- GitHub account suspension if shared maliciously.

---

## 🎯 Real Intent
This tool is created to:  
1. **Demonstrate XSS cookie theft in a safe environment.**  
2. **Raise awareness** about cookie security, HTTPOnly, and Secure flags.  
3. **Teach defensive coding practices** for web developers.  
4. Provide a **hands-on learning experience** for ethical hackers and students.  

> > This is a **real hacking tool**, designed to **demonstrate XSS impacts and cookie theft in a legal, ethical pentesting context**.  
> It is **not intended for malicious use** on unauthorized websites or real users.


---

## 🛠 Setup & Usage
1. Clone this repository:
```
git clone https://github.com/giriaryan694-a11y/CookieStealer.git
cd CookieSteale
pip install -r requirements.txt
python main.py
```
2. Use a **controlled lab environment**, e.g.,  
   [http://testphp.vulnweb.com/](http://testphp.vulnweb.com/).  
3. Follow the instructions in `/docs/` to simulate XSS cookie access.  
4. Observe **how cookies can be exposed**, without stealing real data.

---

## 🧪 Recommended Safe Labs
- [VulnWeb Test PHP](http://testphp.vulnweb.com/)  
- [Test HTML5](http://testhtml5.vulnweb.com/)  
- [Test ASP](http://testasp.vulnweb.com/)  
- [Test REST API](http://rest.vulnweb.com/)  

> Only test in environments designed for security experimentation.

---

## 🔒 Security & Ethics
- **Never use this on real websites**.  
- **Do not share real user data.**  
- Encourage **responsible pentesting practices**.  
- Educate others about **XSS prevention and cookie security**.

---

## 📚 Learning Resources
- [OWASP XSS](https://owasp.org/www-community/attacks/xss/)  
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)  
- [VulnWeb Labs](http://www.vulnweb.com/)

---

## 💡 Contribution
- Contributions are welcome **only if they keep this tool educational and safe**.  
- Submit **pull requests** with demos, lab exercises, or safe payloads.  

---

## 📝 Disclaimer
This tool is for **educational purposes only**. The author **assumes no liability** for any misuse or damage caused by this tool. **Use at your own risk.**

