import React, { useState, useEffect, useRef } from 'react';

/**
 * GradientVideoBackground
 * Ambient atmospheric looping gradient video with a 4-blob CSS-only radial fallback.
 * Designed to provide a soft atmospheric glow behind content using mix-blend-mode: screen.
 */
const PORTFOLIO_GLOW_VIDEO_SRC = './portfolio-showcase-glow.mp4';

export default function GradientVideoBackground({ videoSrc = PORTFOLIO_GLOW_VIDEO_SRC }) {
  const videoRef = useRef(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    // Check prefers-reduced-motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      setHasError(true);
      return;
    }

    const video = videoRef.current;
    if (!video) return;

    const handleReady = () => {
      setIsLoaded(true);
      try {
        const playPromise = video.play();
        if (playPromise !== undefined) {
          playPromise.catch(() => {
            // Autoplay blocked by browser policy; fallback stays active
          });
        }
      } catch (err) {
        // Fallback remains visible
      }
    };

    const handleError = () => {
      setHasError(true);
      setIsLoaded(false);
    };

    video.addEventListener('loadeddata', handleReady);
    video.addEventListener('canplay', handleReady);
    video.addEventListener('error', handleError);

    if (video.readyState >= 2) {
      handleReady();
    }

    return () => {
      video.removeEventListener('loadeddata', handleReady);
      video.removeEventListener('canplay', handleReady);
      video.removeEventListener('error', handleError);
    };
  }, []);

  return (
    <div
      className="portfolio-glow-bg"
      aria-hidden="true"
      style={{
        position: 'absolute',
        inset: 0,
        zIndex: 0,
        pointerEvents: 'none',
        overflow: 'hidden',
        maskImage: 'linear-gradient(to bottom, transparent 0%, black 18%, black 82%, transparent 100%)',
        WebkitMaskImage: 'linear-gradient(to bottom, transparent 0%, black 18%, black 82%, transparent 100%)',
      }}
    >
      {/* CSS Fallback 4-blob radial gradient */}
      <div
        className="portfolio-glow-fallback"
        style={{
          position: 'absolute',
          width: '140%',
          height: '150%',
          left: '50%',
          top: '-20%',
          transform: 'translateX(-50%)',
          opacity: 0.8,
          mixBlendMode: 'screen',
          filter: 'blur(64px)',
          WebkitFilter: 'blur(64px)',
          willChange: 'transform',
          pointerEvents: 'none',
          background: `
            radial-gradient(circle at 30% 35%, var(--glow-purple) 0%, transparent 55%),
            radial-gradient(circle at 70% 30%, var(--glow-blue) 0%, transparent 50%),
            radial-gradient(circle at 40% 70%, var(--glow-magenta) 0%, transparent 55%),
            radial-gradient(circle at 65% 65%, var(--glow-teal) 0%, transparent 50%)
          `,
        }}
      />

      {/* Decorative Oversized Ambient Glow Video */}
      {!hasError && (
        <video
          ref={videoRef}
          src={videoSrc}
          autoPlay
          loop
          muted
          playsInline
          preload="auto"
          tabIndex={-1}
          aria-hidden="true"
          style={{
            position: 'absolute',
            width: '140%',
            height: '150%',
            left: '50%',
            top: '-20%',
            transform: 'translateX(-50%)',
            objectFit: 'cover',
            opacity: isLoaded ? 0.8 : 0,
            transition: 'opacity 600ms ease',
            mixBlendMode: 'screen',
            filter: 'blur(64px)',
            WebkitFilter: 'blur(64px)',
            willChange: 'transform, opacity',
            pointerEvents: 'none',
          }}
        />
      )}
    </div>
  );
}
