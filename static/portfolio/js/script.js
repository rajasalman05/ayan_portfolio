// Terminal role-typing effect
document.addEventListener("DOMContentLoaded", function () {
  var roleEl = document.getElementById("role-typer");
  if (roleEl) {
    var roles = JSON.parse(roleEl.dataset.roles || "[]");
    var i = 0, char = 0, deleting = false;
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function tick() {
      if (!roles.length) return;
      var word = roles[i % roles.length];
      if (reduceMotion) {
        roleEl.textContent = roles[0];
        return;
      }
      if (!deleting) {
        char++;
        roleEl.textContent = word.slice(0, char);
        if (char === word.length) {
          deleting = true;
          setTimeout(tick, 1400);
          return;
        }
      } else {
        char--;
        roleEl.textContent = word.slice(0, char);
        if (char === 0) {
          deleting = false;
          i++;
        }
      }
      setTimeout(tick, deleting ? 35 : 65);
    }
    tick();
  }

  // Scroll reveal
  var revealEls = document.querySelectorAll(".reveal, .skill-card");
  if ("IntersectionObserver" in window) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { obs.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in-view"); });
  }

  // Mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
    });
  }

  // ---------- Theme Switcher Logic ----------
  var themeToggleBtn = document.getElementById("themeToggle");
  var themeIcon = document.getElementById("themeIcon");

  // Sun and Moon SVG paths
  var sunIconPath = '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>';
  var moonIconPath = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>';

  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    if (themeIcon) {
      themeIcon.innerHTML = theme === "light" ? sunIconPath : moonIconPath;
    }
  }

  // Detect saved theme or system preference
  var savedTheme = localStorage.getItem("theme");
  var systemPrefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;

  if (savedTheme) {
    setTheme(savedTheme);
  } else if (systemPrefersLight) {
    setTheme("light");
  } else {
    setTheme("dark");
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener("click", function () {
      var currentTheme = document.documentElement.getAttribute("data-theme");
      var newTheme = currentTheme === "light" ? "dark" : "light";
      setTheme(newTheme);
    });
  }
});

// Parallax/3D Mouse Move Effect
document.addEventListener('mousemove', (e) => {
  const cards = document.querySelectorAll('.gloody-card');
  const orbs = document.querySelectorAll('.floating-orb');
  
  const mouseX = e.clientX / window.innerWidth - 0.5;
  const mouseY = e.clientY / window.innerHeight - 0.5;

  cards.forEach(card => {
    card.style.transform = `perspective(1000px) rotateY(${mouseX * 10}deg) rotateX(${-mouseY * 10}deg) translateY(-4px)`;
  });

  orbs.forEach((orb, index) => {
    const speed = (index + 1) * 20;
    orb.style.transform = `translate(${mouseX * speed}px, ${mouseY * speed}px)`;
  });
});