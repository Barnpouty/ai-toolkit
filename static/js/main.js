/* AI Toolkit 2026 — small, dependency-free enhancements.
   The page works fully without this file; each block below only adds polish. */
(() => {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* Header: compact once the page scrolls ---------------------------------- */
  const header = document.querySelector("[data-header]");
  if (header) {
    const update = () => header.classList.toggle("is-scrolled", window.scrollY > 12);
    update();
    window.addEventListener("scroll", update, { passive: true });
  }

  /* Mobile menu ------------------------------------------------------------ */
  const toggle = document.querySelector("[data-menu-toggle]");
  const nav = document.getElementById("site-nav");
  if (toggle && nav) {
    const setOpen = (open) => {
      toggle.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
      document.body.classList.toggle("menu-open", open);
      if (open) nav.querySelector("a")?.focus();
    };
    toggle.addEventListener("click", () => setOpen(toggle.getAttribute("aria-expanded") !== "true"));
    nav.addEventListener("click", (e) => { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { setOpen(false); toggle.focus(); }
    });
    window.matchMedia("(min-width: 901px)").addEventListener("change", (e) => { if (e.matches) setOpen(false); });
  }

  /* Category explorer: accessible tabs (WAI-ARIA pattern) ------------------- */
  document.querySelectorAll("[data-tabs]").forEach((root) => {
    const tabs = Array.from(root.querySelectorAll('[role="tab"]'));
    const select = (tab, focus) => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        const panel = document.getElementById(t.getAttribute("aria-controls"));
        if (!panel) return;
        if (on) {
          panel.removeAttribute("data-hidden");
          if (!reduceMotion) {
            panel.classList.remove("is-entering");
            void panel.offsetWidth; // restart animation
            panel.classList.add("is-entering");
          }
        } else {
          panel.setAttribute("data-hidden", "");
        }
      });
      if (focus) tab.focus();
      tab.scrollIntoView({ block: "nearest", inline: "nearest", behavior: reduceMotion ? "auto" : "smooth" });
    };
    tabs.forEach((tab, i) => {
      tab.addEventListener("click", () => select(tab, false));
      tab.addEventListener("keydown", (e) => {
        const keys = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 };
        let next = null;
        if (e.key in keys) next = tabs[(i + keys[e.key] + tabs.length) % tabs.length];
        else if (e.key === "Home") next = tabs[0];
        else if (e.key === "End") next = tabs[tabs.length - 1];
        if (next) { e.preventDefault(); select(next, true); }
      });
    });
  });

  /* Scroll reveals (only elements marked data-reveal) ---------------------- */
  const revealables = document.querySelectorAll("[data-reveal]");
  if (!reduceMotion && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    revealables.forEach((el) => io.observe(el));
  } else {
    revealables.forEach((el) => el.classList.add("is-visible"));
  }

  if (reduceMotion || !finePointer) return;

  /* Primary CTAs lean slightly toward the pointer -------------------------- */
  document.querySelectorAll("[data-magnetic]").forEach((btn) => {
    const strength = 0.18, max = 6;
    btn.addEventListener("pointermove", (e) => {
      const r = btn.getBoundingClientRect();
      const x = Math.max(-max, Math.min(max, (e.clientX - r.left - r.width / 2) * strength));
      const y = Math.max(-max, Math.min(max, (e.clientY - r.top - r.height / 2) * strength));
      btn.style.transform = `translate(${x}px, ${y}px)`;
    });
    btn.addEventListener("pointerleave", () => { btn.style.transform = ""; });
  });

  /* Hero books follow the pointer by a few degrees ------------------------- */
  const tilt = document.querySelector("[data-tilt]");
  const books = tilt?.querySelector(".books");
  if (tilt && books) {
    const hero = tilt.closest("section") || tilt;
    let frame = 0;
    hero.addEventListener("pointermove", (e) => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const r = hero.getBoundingClientRect();
        const dx = (e.clientX - r.left) / r.width - 0.5;
        const dy = (e.clientY - r.top) / r.height - 0.5;
        books.style.transform = `rotateY(${dx * 6}deg) rotateX(${-dy * 4}deg)`;
      });
    });
    hero.addEventListener("pointerleave", () => { books.style.transform = ""; });
    books.style.transition = "transform .9s cubic-bezier(0.2, 0.7, 0.1, 1)";
    books.style.transformStyle = "preserve-3d";
  }
})();
