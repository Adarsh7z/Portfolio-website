import React, { useState, useEffect } from 'react';

const NAV_LINKS = [
  { name: 'About', href: '#about' },
  { name: 'Showcase', href: '#portfolio-showcase' },
  { name: 'Skills', href: '#skills' },
  { name: 'Highlights', href: '#projects' },
  { name: 'Certificates', href: '#certificates' },
  { name: 'Contact', href: '#contact' },
];

const STARS = [
  { top: '10%', left: '12%', size: 2.5, duration: '3.8s', delay: '0.2s' },
  { top: '24%', left: '26%', size: 2, duration: '4.5s', delay: '1.2s' },
  { top: '8%', left: '48%', size: 3, duration: '5.2s', delay: '0.6s' },
  { top: '19%', left: '64%', size: 2, duration: '4.0s', delay: '1.9s' },
  { top: '32%', left: '79%', size: 2.5, duration: '4.6s', delay: '0.9s' },
  { top: '14%', left: '91%', size: 3, duration: '5.5s', delay: '1.4s' },
  { top: '39%', left: '8%', size: 2, duration: '4.2s', delay: '2.3s' },
  { top: '44%', left: '54%', size: 2.5, duration: '4.9s', delay: '0.4s' },
];

export default function Hero() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    if (mobileMenuOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [mobileMenuOpen]);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') setMobileMenuOpen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <section
      id="hero"
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        padding: '80px 2.5rem 2.5rem 2.5rem',
        position: 'relative',
        backgroundColor: '#0a0f14',
        overflow: 'hidden',
      }}
    >
      {/* Background Video & Blend Effects */}
      <div
        className="hero-bg-wrap"
        aria-hidden="true"
        style={{
          position: 'absolute',
          inset: 0,
          width: '100%',
          height: '100%',
          pointerEvents: 'none',
          zIndex: 1,
          overflow: 'hidden',
        }}
      >
        <video
          autoPlay
          loop
          muted
          playsInline
          style={{
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            mixBlendMode: 'screen',
          }}
          src="https://cdn.sceneai.art/Hero%20Section%20Video/736fd4a0-70ac-4f44-9633-55769ead6aca.mp4"
        />

        {/* Subtle dark gradient overlay behind left-aligned text */}
        <div
          className="hero-left-vignette-overlay"
          style={{
            position: 'absolute',
            inset: 0,
            background: 'linear-gradient(90deg, rgba(10, 15, 20, 0.65) 0%, rgba(10, 15, 20, 0.45) 32%, rgba(10, 15, 20, 0.15) 55%, transparent 75%)',
            pointerEvents: 'none',
            zIndex: 2,
          }}
        />

        {/* Bottom-right vignette shapes stacked for smooth fade */}
        <div style={{ position: 'absolute', bottom: '-9rem', right: '-9rem', width: '560px', height: '560px', borderRadius: '9999px', backgroundColor: '#000', filter: 'blur(120px)' }} />
        <div style={{ position: 'absolute', bottom: '-6rem', right: '-6rem', width: '450px', height: '450px', borderRadius: '9999px', backgroundColor: '#000', filter: 'blur(80px)' }} />
        <div style={{ position: 'absolute', bottom: '-3.5rem', right: '-3.5rem', width: '340px', height: '340px', borderRadius: '9999px', backgroundColor: '#000', filter: 'blur(60px)' }} />
        <div style={{ position: 'absolute', bottom: '-1.5rem', right: '-1.5rem', width: '240px', height: '240px', borderRadius: '9999px', backgroundColor: '#000', filter: 'blur(40px)' }} />

        {/* Ambient glows (indigo & fuchsia) */}
        <div style={{ position: 'absolute', top: '16%', left: '10%', width: '480px', height: '480px', transform: 'translate(-50%, -50%)', borderRadius: '9999px', backgroundColor: 'rgba(99, 102, 241, 0.1)', filter: 'blur(130px)' }} />
        <div style={{ position: 'absolute', top: '28%', right: '16%', width: '420px', height: '420px', transform: 'translateY(-50%)', borderRadius: '9999px', backgroundColor: 'rgba(217, 70, 239, 0.1)', filter: 'blur(120px)' }} />

        {/* 8 glowing white stars in top half */}
        {STARS.map((star, idx) => (
          <div
            key={idx}
            className="hero-star"
            style={{
              position: 'absolute',
              top: star.top,
              left: star.left,
              width: `${star.size}px`,
              height: `${star.size}px`,
              borderRadius: '9999px',
              backgroundColor: '#fff',
              boxShadow: '0 0 6px 1px rgba(255, 255, 255, 0.85)',
              animationDuration: star.duration,
              animationDelay: star.delay,
            }}
          />
        ))}
      </div>

      {/* Mobile Menu Overlay */}
      <div
        className="mobile-menu-overlay"
        id="mobile-menu"
        style={{ display: mobileMenuOpen ? 'flex' : 'none' }}
      >
        <button
          className="mobile-menu-close"
          id="mobile-menu-close"
          aria-label="Close menu"
          onClick={() => setMobileMenuOpen(false)}
        >
          <i className="fa-solid fa-arrow-left"></i> <span style={{ fontSize: '0.75rem', letterSpacing: '2px' }}>BACK</span>
        </button>
        <nav className="mobile-nav-links">
          {NAV_LINKS.map((link) => (
            <a
              key={link.name}
              href={link.href}
              className="mobile-nav-link"
              onClick={() => setMobileMenuOpen(false)}
            >
              {link.name}
            </a>
          ))}
          <a
            href="./Resume Final.pdf"
            download
            className="button mobile-resume-btn"
            onClick={() => setMobileMenuOpen(false)}
          >
            <div className="wrap">
              <p>
                <span><i className="fa-solid fa-download"></i></span>
                <span><i className="fa-solid fa-download"></i></span>
                <span>RESUME</span>
              </p>
            </div>
          </a>
        </nav>
      </div>

      {/* Desktop Navigation */}
      <nav className="fade-el fade-from-top visible" id="main-nav">
        <ul className="nav-links">
          {NAV_LINKS.map((link) => (
            <li key={link.name}>
              <a href={link.href}>{link.name}</a>
            </li>
          ))}
        </ul>
        <a href="./Resume Final.pdf" download className="button nav-btn nav-resume-btn">
          <div className="wrap">
            <p>
              <span><i className="fa-solid fa-download"></i></span>
              <span><i className="fa-solid fa-download"></i></span>
              <span>RESUME</span>
            </p>
          </div>
        </a>
        <button
          className="hamburger-btn"
          id="hamburger-btn"
          aria-label="Toggle mobile menu"
          onClick={() => setMobileMenuOpen(true)}
        >
          <i className="fa-solid fa-bars"></i>
        </button>
      </nav>

      {/* Hero Content Wrap: Left-aligned, vertically centered slightly above true center */}
      <div className="hero-content-wrap">
        <div className="hero-text-block">
          <h1 className="hero-name-heading">
            <span className="hero-name-word hero-anim-line d1">Adarsh</span>
            <span className="hero-name-word hero-anim-line d2">Reddy</span>
          </h1>
          <p className="hero-subtitle hero-anim-line d3">Growth Marketer, Content Strategist &amp; Web Dev</p>
          <p className="hero-description hero-anim-line d4">
            Combining business analytics, organic search, and intuitive web design to push what marketing can do
          </p>

          {/* Centered Action Buttons */}
          <div className="hero-buttons hero-anim-line d5">
            <a href="#projects" className="button hero-work-btn">
              <div className="wrap">
                <p>
                  <span></span>
                  <span></span>
                  <span>VIEW MY WORK</span>
                </p>
              </div>
            </a>
            <button
              className="btn-contact hero-contact-btn"
              onClick={() => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })}
            >
              Get In Touch
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}
