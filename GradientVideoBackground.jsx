import React, { useState, useEffect, useRef } from 'react';

/**
 * GradientVideoBackground
 * Ambient atmospheric looping gradient video with a 4-blob CSS-only radial fallback.
 * Designed to provide a soft atmospheric glow behind content using mix-blend-mode: screen.
 */
const PORTFOLIO_GLOW_VIDEO_SRC = './portfolio-showcase-glow.mp4';
const RESPECT_REDUCED_MOTION = true;

export default function GradientVideoBackground({ videoSrc = PORTFOLIO_GLOW_VIDEO_SRC }) {
  const containerRef = useRef(null);
  const videoRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;

    // Single console message stating whether reduced motion is currently detected
    const reducedMotionDetected = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    console.log('Reduced motion detected:', reducedMotionDetected);

    if (RESPECT_REDUCED_MOTION && reducedMotionDetected) {
      try { video.pause(); } catch (e) {}
      return;
    }

    // Set muted in code before play() for browser autoplay policy
    video.muted = true;
    video.defaultMuted = true;

    let playingFired = false;
    let retryAttached = false;
    let isVisible = true;
    let fallbackTimeout = null;

    const startFallbackTimeout = () => {
      if (fallbackTimeout || playingFired) return;
      fallbackTimeout = setTimeout(() => {
        if (!playingFired) {
          console.warn('Portfolio showcase background video failed to play within 3s; fallback gradient remains active.');
        }
      }, 3000);
    };

    const playVideo = () => {
      if (!isVisible) return;
      startFallbackTimeout();
      try {
        video.muted = true;
        const playPromise = video.play();
        if (playPromise !== undefined) {
          playPromise.catch(() => {
            attachRetry();
          });
        }
      } catch (err) {
        attachRetry();
      }
    };

    const handlePlaying = () => {
      playingFired = true;
      setIsPlaying(true);
      if (fallbackTimeout) {
        clearTimeout(fallbackTimeout);
        fallbackTimeout = null;
      }
      detachRetry();
    };

    const handleError = (e) => {
      console.warn('Portfolio showcase background video encountered an error; fallback gradient remains active.', e);
      if (fallbackTimeout) {
        clearTimeout(fallbackTimeout);
        fallbackTimeout = null;
      }
      setHasError(true);
      setIsPlaying(false);
    };

    const onUserInteraction = () => {
      detachRetry();
      playVideo();
    };

    const attachRetry = () => {
      if (retryAttached || playingFired) return;
      retryAttached = true;
      window.addEventListener('pointerdown', onUserInteraction, { once: true, passive: true });
      window.addEventListener('touchstart', onUserInteraction, { once: true, passive: true });
      window.addEventListener('scroll', onUserInteraction, { once: true, passive: true });
    };

    const detachRetry = () => {
      if (!retryAttached) return;
      retryAttached = false;
      window.removeEventListener('pointerdown', onUserInteraction);
      window.removeEventListener('touchstart', onUserInteraction);
      window.removeEventListener('scroll', onUserInteraction);
    };

    video.addEventListener('playing', handlePlaying);
    const handleCanPlay = () => {
      if (isVisible) playVideo();
    };
    video.addEventListener('canplay', handleCanPlay);
    video.addEventListener('error', handleError);

    // Initial play on mount
    playVideo();

    // IntersectionObserver to pause when offscreen, resume when entering
    let observer;
    if ('IntersectionObserver' in window && containerRef.current) {
      observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            isVisible = entry.isIntersecting;
            if (isVisible) {
              playVideo();
            } else {
              try { video.pause(); } catch (e) {}
            }
          });
        },
        { rootMargin: '100px 0px', threshold: 0 }
      );
      observer.observe(containerRef.current.parentElement || containerRef.current);
    }

    return () => {
      if (fallbackTimeout) clearTimeout(fallbackTimeout);
      detachRetry();
      video.removeEventListener('playing', handlePlaying);
      video.removeEventListener('canplay', handleCanPlay);
      video.removeEventListener('error', handleError);
      if (observer) observer.disconnect();
    };
  }, [videoSrc]);

  return (
    <div
      ref={containerRef}
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
        className={`portfolio-glow-fallback ${isPlaying ? 'is-hidden' : ''}`}
        style={{
          position: 'absolute',
          width: '140%',
          height: '150%',
          left: '50%',
          top: '-20%',
          transform: 'translateX(-50%)',
          opacity: isPlaying ? 0 : 0.8,
          transition: 'opacity 600ms ease',
          mixBlendMode: 'screen',
          filter: 'blur(64px)',
          WebkitFilter: 'blur(64px)',
          willChange: 'transform, opacity',
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
            opacity: isPlaying ? 0.8 : 0,
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
