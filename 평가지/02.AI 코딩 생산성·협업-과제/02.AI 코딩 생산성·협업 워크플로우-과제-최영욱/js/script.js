const menuButton = document.querySelector(".menu-button");
const navMenu = document.querySelector(".nav-menu");
const navLinks = document.querySelectorAll(".nav-menu a");
const header = document.querySelector(".header");
const progressBar = document.querySelector(".top-progress span");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

menuButton.addEventListener("click", () => {
  const isOpen = navMenu.classList.toggle("active");
  menuButton.classList.toggle("active", isOpen);
  document.body.classList.toggle("menu-open", isOpen);
  menuButton.setAttribute("aria-expanded", String(isOpen));
});

navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    navMenu.classList.remove("active");
    menuButton.classList.remove("active");
    document.body.classList.remove("menu-open");
    menuButton.setAttribute("aria-expanded", "false");
  });
});

const updateScrollUI = () => {
  const scrollTop = window.scrollY;
  const scrollable = document.documentElement.scrollHeight - window.innerHeight;
  const progress = scrollable > 0 ? (scrollTop / scrollable) * 100 : 0;
  progressBar.style.width = `${progress}%`;
  header.classList.toggle("scrolled", scrollTop > 24);
};
window.addEventListener("scroll", updateScrollUI, { passive: true });
updateScrollUI();

document.querySelector(".contact-form").addEventListener("submit", (event) => {
  event.preventDefault();
  alert("상담 신청이 완료되었습니다.");
  event.currentTarget.reset();
});

document.querySelector("#current-year").textContent = new Date().getFullYear();

const revealElements = document.querySelectorAll(
  ".section-heading, .course-card, .advantage-item, .review-card, .contact-content, .contact-form"
);
revealElements.forEach((element) => element.classList.add("reveal-target"));

if (!reduceMotion && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealElements.forEach((element, index) => {
    element.style.transitionDelay = `${Math.min(index % 4, 3) * 80}ms`;
    observer.observe(element);
  });
} else {
  revealElements.forEach((element) => element.classList.add("is-visible"));
}

const interfacePanel = document.querySelector(".hero-interface");
const codeWindow = document.querySelector(".code-window");
if (!reduceMotion && interfacePanel && codeWindow && window.matchMedia("(pointer: fine)").matches) {
  interfacePanel.addEventListener("pointermove", (event) => {
    const rect = interfacePanel.getBoundingClientRect();
    const x = (event.clientX - rect.left) / rect.width - 0.5;
    const y = (event.clientY - rect.top) / rect.height - 0.5;
    codeWindow.style.transform = `perspective(1000px) rotateY(${x * 8 - 4}deg) rotateX(${-y * 6 + 2}deg) translateY(-2px)`;
  });
  interfacePanel.addEventListener("pointerleave", () => {
    codeWindow.style.transform = "perspective(1000px) rotateY(-4deg) rotateX(2deg)";
  });
}

const canvas = document.querySelector("#network-canvas");
const context = canvas.getContext("2d");
let nodes = [];
let animationFrame = null;
let pointer = { x: -1000, y: -1000 };

const resizeCanvas = () => {
  const ratio = Math.min(window.devicePixelRatio || 1, 2);
  canvas.width = Math.floor(window.innerWidth * ratio);
  canvas.height = Math.floor(window.innerHeight * ratio);
  canvas.style.width = `${window.innerWidth}px`;
  canvas.style.height = `${window.innerHeight}px`;
  context.setTransform(ratio, 0, 0, ratio, 0, 0);
  const count = Math.max(22, Math.min(54, Math.floor(window.innerWidth / 28)));
  nodes = Array.from({ length: count }, () => ({
    x: Math.random() * window.innerWidth,
    y: Math.random() * window.innerHeight,
    vx: (Math.random() - 0.5) * 0.16,
    vy: (Math.random() - 0.5) * 0.16,
    r: Math.random() * 1.4 + 0.6
  }));
};

const drawNetwork = () => {
  context.clearRect(0, 0, window.innerWidth, window.innerHeight);
  nodes.forEach((node) => {
    node.x += node.vx;
    node.y += node.vy;
    if (node.x < -20) node.x = window.innerWidth + 20;
    if (node.x > window.innerWidth + 20) node.x = -20;
    if (node.y < -20) node.y = window.innerHeight + 20;
    if (node.y > window.innerHeight + 20) node.y = -20;

    const pointerDistance = Math.hypot(node.x - pointer.x, node.y - pointer.y);
    if (pointerDistance < 140) {
      node.x += (node.x - pointer.x) * 0.002;
      node.y += (node.y - pointer.y) * 0.002;
    }

    context.beginPath();
    context.arc(node.x, node.y, node.r, 0, Math.PI * 2);
    context.fillStyle = "rgba(107, 232, 255, 0.52)";
    context.fill();
  });

  for (let i = 0; i < nodes.length; i += 1) {
    for (let j = i + 1; j < nodes.length; j += 1) {
      const distance = Math.hypot(nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y);
      if (distance < 118) {
        context.beginPath();
        context.moveTo(nodes[i].x, nodes[i].y);
        context.lineTo(nodes[j].x, nodes[j].y);
        context.strokeStyle = `rgba(92, 145, 255, ${(1 - distance / 118) * 0.14})`;
        context.lineWidth = 0.7;
        context.stroke();
      }
    }
  }
  animationFrame = requestAnimationFrame(drawNetwork);
};

window.addEventListener("resize", resizeCanvas);
window.addEventListener("pointermove", (event) => { pointer = { x: event.clientX, y: event.clientY }; }, { passive: true });
resizeCanvas();
if (!reduceMotion) drawNetwork();
else {
  drawNetwork();
  cancelAnimationFrame(animationFrame);
  document.querySelectorAll(".course-media video").forEach((video) => video.pause());
}

// 교육 과정 영상은 화면에 보일 때만 재생합니다.
// 모바일에서 여러 영상이 동시에 재생되며 버벅이는 현상을 줄여줍니다.
const courseVideos = document.querySelectorAll(".course-media video");

if ("IntersectionObserver" in window) {
  const courseVideoObserver = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        const video = entry.target;

        if (entry.isIntersecting) {
          const playPromise = video.play();

          if (playPromise !== undefined) {
            playPromise.catch(function () {
              // 일부 모바일 브라우저가 자동 재생을 막는 경우에는
              // poster 이미지가 그대로 표시됩니다.
            });
          }
        } else {
          video.pause();
        }
      });
    },
    {
      threshold: 0.35
    }
  );

  courseVideos.forEach(function (video) {
    courseVideoObserver.observe(video);
  });
}
