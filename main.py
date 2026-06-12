<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday Saumya | My Precious Sister</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #0f051d 0%, #290742 40%, #4a0e4e 70%, #1a052e 100%);
            overflow-x: hidden;
        }
        .font-luxury {
            font-family: 'Cinzel', serif;
        }
        .text-gold-gradient {
            background: linear-gradient(90deg, #ffe082 0%, #ffb300 50%, #ffe082 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .bg-luxury-gradient {
            background: linear-gradient(135deg, rgba(255, 105, 180, 0.15) 0%, rgba(147, 51, 234, 0.15) 50%, rgba(212, 175, 55, 0.1) 100%);
        }
        .glassmorphism {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        .glassmorphism-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .glassmorphism-card:hover {
            transform: translateY(-10px);
            border-color: rgba(212, 175, 55, 0.4);
            box-shadow: 0 12px 40px 0 rgba(236, 72, 153, 0.2);
        }
        @keyframes float-slow {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.6; }
            50% { transform: translateY(-25px) rotate(5deg); opacity: 0.9; }
        }
        @keyframes pulse-gold {
            0%, 100% { box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
            50% { box-shadow: 0 0 30px rgba(212, 175, 55, 0.6); }
        }
        .animate-float {
            animation: float-slow 6s ease-in-out infinite;
        }
        .pulse-gold-trigger {
            animation: pulse-gold 3s infinite;
        }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0f051d; }
        ::-webkit-scrollbar-thumb { background: linear-gradient(#ec4899, #8b5cf6); border-radius: 4px; }
    </style>
</head>
<body class="text-gray-100 antialiased">

    <div id="particles-container" class="fixed inset-0 pointer-events-none z-0 overflow-hidden"></div>

    <div class="fixed top-6 right-6 z-50">
        <button id="musicBtn" class="glassmorphism p-4 rounded-full text-gold-gradient hover:scale-110 transition duration-300 flex items-center justify-center cursor-pointer shadow-lg">
            <i id="musicIcon" class="fas fa-music text-xl"></i>
        </button>
        <audio id="bgMusic" loop>
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
        </audio>
    </div>

    <section class="relative min-h-screen flex flex-col justify-center items-center px-4 overflow-hidden z-10">
        <div class="absolute inset-0 bg-luxury-gradient opacity-40"></div>
        <div class="text-center z-10 max-w-4xl mx-auto space-y-6">
            <p class="font-luxury tracking-[0.3em] text-pink-400 text-sm md:text-lg uppercase">A Premium Celebration Portfolio</p>
            <h1 class="font-luxury text-5xl md:text-8xl font-bold tracking-tight drop-shadow-2xl">
                Happy Birthday <br>
                <span class="text-gold-gradient drop-shadow-[0_5px_15px_rgba(255,215,0,0.4)]">Saumya ❤️</span>
            </h1>
            <p class="text-lg md:text-2xl text-purple-200 font-light max-w-2xl mx-auto italic tracking-wide">
                "To the most wonderful, elegant, and loving sister in the universe."
            </p>
            <div class="pt-8 flex justify-center gap-4 animate-bounce">
                <a href="#countdown" class="text-sm uppercase tracking-[0.2em] text-amber-200 border-b border-amber-200/40 pb-2 hover:text-pink-400 hover:border-pink-400 transition-all duration-300">
                    Scroll to Explore the Magic <i class="fas fa-chevron-down ml-2"></i>
                </a>
            </div>
        </div>
    </section>

    <section id="countdown" class="py-24 relative z-10 px-4">
        <div class="max-w-4xl mx-auto glassmorphism rounded-3xl p-8 md:p-12 text-center relative overflow-hidden">
            <h2 class="font-luxury text-3xl md:text-4xl text-gold-gradient mb-8 tracking-wider">Counting Down To August 4th</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
                <div class="glassmorphism-card p-6 rounded-2xl"><span id="days" class="font-luxury text-4xl md:text-6xl font-bold text-pink-400">00</span><p class="text-xs uppercase tracking-widest mt-2 text-gray-400">Days</p></div>
                <div class="glassmorphism-card p-6 rounded-2xl"><span id="hours" class="font-luxury text-4xl md:text-6xl font-bold text-purple-400">00</span><p class="text-xs uppercase tracking-widest mt-2 text-gray-400">Hours</p></div>
                <div class="glassmorphism-card p-6 rounded-2xl"><span id="minutes" class="font-luxury text-4xl md:text-6xl font-bold text-amber-300">00</span><p class="text-xs uppercase tracking-widest mt-2 text-gray-400">Minutes</p></div>
                <div class="glassmorphism-card p-6 rounded-2xl"><span id="seconds" class="font-luxury text-4xl md:text-6xl font-bold text-red-400">00</span><p class="text-xs uppercase tracking-widest mt-2 text-gray-400">Seconds</p></div>
            </div>
        </div>
    </section>

    <section class="py-20 relative z-10 px-4 bg-black/20">
        <div class="max-w-4xl mx-auto grid md:grid-cols-2 gap-12 items-center">
            <div class="glassmorphism p-8 md:p-10 rounded-3xl min-h-[350px] flex flex-col justify-between border-l-4 border-pink-500 shadow-2xl">
                <div>
                    <i class="fas fa-quote-left text-4xl text-pink-500/30 mb-4"></i>
                    <div id="typewriter-text" class="text-gray-200 leading-relaxed tracking-wide text-md md:text-lg min-h-[200px]"></div>
                </div>
                <div class="mt-6 text-right"><span class="font-luxury text-gold-gradient font-semibold tracking-wider">— Forever Yours</span></div>
            </div>

            <div class="flex flex-col items-center justify-center space-y-6">
                <h3 class="font-luxury text-2xl text-purple-200 tracking-wide text-center">Tap to Unlock a Surprise</h3>
                <div id="giftBoxContainer" class="relative cursor-pointer group transform hover:scale-105 transition-transform duration-300">
                    <svg id="giftBoxSvg" class="w-64 h-64 pulse-gold-trigger rounded-2xl p-4 transition-all duration-500" viewBox="0 0 100 100">
                        <rect x="20" y="40" width="60" height="50" rx="4" fill="#4c1d95" stroke="#ffe082" stroke-width="1"/>
                        <rect id="giftLid" x="16" y="28" width="68" height="14" rx="3" fill="#6d28d9" stroke="#ffe082" stroke-width="1" class="transition-transform duration-700 origin-bottom"/>
                        <rect x="46" y="28" width="8" height="62" fill="#d4af37"/>
                        <rect x="16" y="32" width="68" height="6" fill="#d4af37"/>
                        <path d="M50,28 C40,15 45,10 50,25 C55,10 60,15 50,28 Z" fill="#ffe082"/>
                    </svg>
                </div>
                <p id="giftStatusText" class="text-sm tracking-widest text-pink-400 uppercase font-medium">Click The Luxury Box</p>
            </div>
        </div>
    </section>

    <section class="py-24 relative z-10 px-4">
        <div class="max-w-5xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="font-luxury text-4xl md:text-5xl text-gold-gradient tracking-widest">The Sisterhood Gallery</h2>
                <div class="h-[2px] w-24 bg-gradient-to-r from-pink-500 to-amber-500 mx-auto mt-4"></div>
            </div>
            <div class="relative overflow-hidden rounded-3xl glassmorphism p-4 md:p-8">
                <div id="gallerySlider" class="flex transition-transform duration-700 ease-out">
                    <div class="min-w-full px-4 flex flex-col md:flex-row gap-8 items-center">
                        <div class="w-full md:w-1/2 aspect-video bg-gradient-to-tr from-purple-800 to-pink-600 rounded-2xl flex items-center justify-center relative overflow-hidden">
                            <i class="fas fa-images text-6xl text-white/40"></i>
                        </div>
                        <div class="w-full md:w-1/2 space-y-4">
                            <span class="text-xs uppercase tracking-widest font-mono text-amber-300 bg-amber-400/10 px-3 py-1 rounded-full">The Infinite Bond</span>
                            <h3 class="font-luxury text-2xl text-white">Chasing Golden Sunsets</h3>
                            <p class="text-gray-300 font-light text-sm">Every laugh shared, every secret kept, and every beautiful dream pursued together makes life an extraordinary adventure with you.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="py-24 relative z-10 px-4 text-center">
        <div class="max-w-3xl mx-auto glassmorphism p-12 rounded-3xl border border-amber-500/20 relative overflow-hidden">
            <h2 class="font-luxury text-3xl md:text-5xl text-white mb-6 tracking-wide font-bold">The Grand Finale Surprise</h2>
            <button id="finaleBtn" class="pulse-gold-trigger px-8 py-4 rounded-full bg-gradient-to-r from-amber-400 via-pink-500 to-purple-600 font-luxury text-white tracking-[0.2em] uppercase font-bold text-sm shadow-xl hover:scale-105 transition-all duration-300 cursor-pointer">
                Open Your Birthday Surprise 🎁
            </button>
        </div>
    </section>

    <div id="finaleModal" class="fixed inset-0 z-50 bg-black/95 opacity-0 pointer-events-none transition-opacity duration-700 flex items-center justify-center p-4">
        <div class="max-w-2xl w-full glassmorphism p-8 md:p-12 rounded-3xl text-center transform scale-90 transition-transform duration-700 relative border border-pink-500/30">
            <button id="closeModalBtn" class="absolute top-4 right-4 text-gray-400 hover:text-white cursor-pointer p-2"><i class="fas fa-times text-xl"></i></button>
            <div class="w-20 h-20 bg-gradient-to-tr from-pink-500 to-amber-400 rounded-full flex items-center justify-center text-white text-3xl mx-auto mb-6"><i class="fas fa-heart"></i></div>
            <h3 class="font-luxury text-2xl md:text-4xl text-gold-gradient tracking-wide mb-6">To My Favorite Person</h3>
            <p class="text-xl md:text-2xl text-purple-100 font-light italic leading-relaxed">
                "Saumya, you will always be my favorite sister and one of the most important people in my life. Happy Birthday ❤️"
            </p>
        </div>
    </div>

    <script>
        const bgMusic = document.getElementById('bgMusic');
        const musicBtn = document.getElementById('musicBtn');
        const musicIcon = document.getElementById('musicIcon');

        musicBtn.addEventListener('click', () => {
            if (bgMusic.paused) {
                bgMusic.play().catch(e => console.log("Audio block check"));
                musicIcon.className = 'fas fa-pause text-xl';
            } else {
                bgMusic.pause();
                musicIcon.className = 'fas fa-music text-xl';
            }
        });

        const particlesContainer = document.getElementById('particles-container');
        const configs = { count: 30, symbols: ['❤️', '✨', '🎈'] };
        for (let i = 0; i < configs.count; i++) {
            const p = document.createElement('div');
            p.className = 'absolute pointer-events-none animate-float select-none';
            p.innerText = configs.symbols[Math.floor(Math.random() * configs.symbols.length)];
            p.style.left = Math.random() * 100 + 'vw';
            p.style.top = Math.random() * 100 + 'vh';
            p.style.animationDelay = Math.random() * 5 + 's';
            p.style.fontSize = (Math.random() * 20 + 12) + 'px';
            particlesContainer.appendChild(p);
        }

        function updateCountdown() {
            const currentYear = new Date().getFullYear();
            let target = new Date(`August 4, ${currentYear} 00:00:00`).getTime();
            let diff = target - new Date().getTime();
            if (diff < 0) { target = new Date(`August 4, ${currentYear + 1} 00:00:00`).getTime(); diff = target - new Date().getTime(); }
            document.getElementById('days').innerText = String(Math.floor(diff / (1000*60*60*24))).padStart(2, '0');
            document.getElementById('hours').innerText = String(Math.floor((diff % (1000*60*60*24)) / (1000*60*60))).padStart(2, '0');
            document.getElementById('minutes').innerText = String(Math.floor((diff % (1000*60*60)) / (1000*60))).padStart(2, '0');
            document.getElementById('seconds').innerText = String(Math.floor((diff % (1000*60)) / 1000)).padStart(2, '0');
        }
        setInterval(updateCountdown, 1000); updateCountdown();

        // Pass message via dynamic injector smoothly
        window.injectMessage = function(msg) {
            let idx = 0; const out = document.getElementById('typewriter-text');
            function type() { if(idx < msg.length) { const c = msg.charAt(idx); out.innerHTML += c === '\n' ? '<br>' : c; idx++; setTimeout(type, 45); } }
            setTimeout(type, 1000);
        };

        function triggerPremiumFireworks() {
            const end = Date.now() + 4000;
            const interval = setInterval(() => {
                if (Date.now() > end) return clearInterval(interval);
                confetti({ startVelocity: 30, spread: 360, ticks: 60, origin: { x: Math.random(), y: Math.random() - 0.2 } });
            }, 300);
        }
        window.addEventListener('DOMContentLoaded', () => { triggerPremiumFireworks(); });

        const giftBoxContainer = document.getElementById('giftBoxContainer');
        const giftLid = document.getElementById('giftLid');
        let opened = false;
        giftBoxContainer.addEventListener('click', () => {
            if(!opened) { giftLid.style.transform = 'translateY(-18px) rotate(-10deg)'; triggerPremiumFireworks(); opened = true; }
            else { giftLid.style.transform = 'none'; opened = false; }
        });

        const finaleBtn = document.getElementById('finaleBtn');
        const finaleModal = document.getElementById('finaleModal');
        const closeModalBtn = document.getElementById('closeModalBtn');
        finaleBtn.addEventListener('click', () => {
            finaleModal.classList.remove('pointer-events-none', 'opacity-0');
            finaleModal.children[0].classList.replace('scale-90', 'scale-100');
            triggerPremiumFireworks();
        });
        closeModalBtn.addEventListener('click', () => {
            finaleModal.classList.add('pointer-events-none', 'opacity-0');
            finaleModal.children[0].classList.replace('scale-100', 'scale-90');
        });
    </script>
</body>
</html>
import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Part 1 ke saare design content ko yahan hold kiya jayega
HTML_CONTENT = """
"""

# Dynamic emotional letter setup
EMOTIONAL_MESSAGE = (
    "Dear Saumya,\\n\\nYou are not just my sister, you are one of the most "
    "precious blessings in my life. Thank you for always supporting me, "
    "caring for me, and filling my life with happiness. I pray that your life "
    "is filled with endless joy, success, love, and beautiful memories. May all "
    "your dreams come true. Happy Birthday, Saumya. ❤️"
)

@app.route('/')
def home():
    # Typewriter effect ko trigger karne ke liye message dynamic append kiya jata hai
    dynamic_trigger = f"<script>window.addEventListener('DOMContentLoaded', () => {{ window.injectMessage(`{EMOTIONAL_MESSAGE}`); }});</script>"
    full_template = HTML_CONTENT.replace("</body>", f"{dynamic_trigger}</body>")
    return render_template_string(full_template)

if __name__ == '__main__':
    # Cloud scaling ready setups (Render production friendly)
    app_port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=app_port, debug=False)
