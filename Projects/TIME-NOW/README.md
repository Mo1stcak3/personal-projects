# ⏰🐱 TIME-NOW: Meme Edition 
> A real-time, vibe-infused clock website. Deployed via Cloudflare for maximum performance and minimum boredom.

[![Site Status](https://img.shields.io/website?url=https%3A%2F%2Fnutterbutters.uk&label=nutterbutters.uk&style=flat-square&color=blueviolet)](https://nutterbutters.uk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## 🚀 Live Demo
**Experience the vibe:** [nutterbutters.uk](https://nutterbutters.uk)

---

## 🔥 Features

* **Live Time Sync:** Real-time clock and date widget (Default: `Asia/Manila`).
* **Meme-Powered UI:** Features **Maxwell the Spinning Cat** for a high-quality aesthetic.
* **Kirby Soundscape:** Integrated HTML5 audio with an autoplay workaround for a cozy atmosphere.
* **Modern Deployment:** Custom domain hosting via **Cloudflare Pages** with automated SSL and edge caching.
* **Responsive Design:** Fully optimized for both desktop browsers and mobile devices.
* **Minimalist Codebase:** Lightweight structure for lightning-fast load times.

---

## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **Deployment** | Cloudflare Pages |
| **Domain & Security** | Cloudflare DNS + Universal SSL |
| **Assets** | Custom MP3 + Maxwell GIF |

---

## 📸 Preview

![TIME-NOW Demo](TIME-NOW/preview.gif)

---

## 🧪 Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/time-now-meme.git](https://github.com/your-username/time-now-meme.git)
    ```
2.  **Add Assets:** Ensure `AUDIO.mp3` is in the root folder.
3.  **Launch:** Open `index.html` in your browser. No server required.

---

## 🌍 Customizing Timezone

This project uses an external widget API. To localize it:
1.  Visit the [Time.now Widget Generator](https://time.now).
2.  Configure your preferred location.
3.  Replace the existing widget `<iframe>` or `<script>` in `index.html`.

---

## 🤓 What I Learned

Building this project allowed me to solve several technical hurdles common in modern web development:

* **Autoplay Workarounds:** Implemented JS event listeners to bypass strict browser policies regarding unmuted autoplaying audio.
* **DNS & Deployment:** Managed custom domain mapping and SSL handshake configurations within the Cloudflare ecosystem.
* **Asset Optimization:** Balanced high-quality GIF backgrounds and audio files with performance to ensure a low "Time to First Byte" (TTFB).
* **Documentation:** Focused on creating a professional, scannable README that effectively communicates technical value.

---

## 💬 Reflection

This project started as a simple experiment with a time widget. I decided to push it further by adding Maxwell the cat and Kirby music to show that technical projects can have personality. It’s a functional proof-of-concept for my ability to build, brand, and deploy web applications from scratch.

> **"Functional, deployed, and fun — this is how I learn and build in public."**

---

### 🤝 Contributing
Feel free to fork this repo and add your own memes! Pull requests are always welcome.
