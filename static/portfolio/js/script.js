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
});
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