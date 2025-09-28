# 🕸️ Webify v2

A fast **AI-powered website generator** for smaller, clean websites, built with Flask + OpenAI's Responses API.  
Webify v2 is the successor to **Webify.ai v1** — rebuilt from the ground up to be faster, cleaner, and far more polished.  
Think of it as a **v0 / Lovable-inspired site builder** that turns your ideas into a quick prototype

---

### ✨ Features

- ⚡ **AI Website Generation** – Just describe the site you want, and Webify builds it for you.  
- 🎨 **Tailwind CSS Styling** – Modern, responsive designs out of the box.  
- 🧠 **Improved Model Integration** – Uses `gpt-4o` (or `o3` for deep reasoning) with `max_output_tokens` for long, coherent outputs.  
- 🖼 **Live Preview Page** – See the generated site on its own page, not just in a box.  
- 🔄 **Regeneration Support** – Easily tweak prompts and generate again.  
- 🧰 **Modular Code** – Clean separation of backend logic (`model.py`) and templates.

---

### 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/your-username/webify-v2.git
cd webify-v2

2. **Set up a virtual environment**
```bash
python -m venv venv

3. **Install dependencies**
```bash
pip install -r requirements.txt

4. **Set up your OpenAI API key in .env**
```bash
OPENAI_API_KEY=your_api_key_here



