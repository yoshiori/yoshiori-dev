import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

interface Talk {
  title: string;
  url: string;
  thumbnail?: string;
  date: string;
}

function formatDate(date: string) {
  const d = new Date(date);
  if (isNaN(d.valueOf())) return date;
  return d.toLocaleDateString("en-US", { year: "numeric", month: "short" });
}

function TalkItem({ talk }: { talk: Talk }) {
  const [hovered, setHovered] = useState(false);

  return (
    <motion.a
      href={talk.url}
      target="_blank"
      rel="noopener noreferrer"
      className="relative shrink-0 block w-[280px] overflow-hidden border border-border bg-surface no-underline"
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      whileHover={{ scale: 1.08, zIndex: 10 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
    >
      <div className="relative">
        {talk.thumbnail ? (
          <img
            className="block w-full aspect-video object-cover bg-thumb-bg"
            src={talk.thumbnail}
            alt={talk.title}
            loading="lazy"
          />
        ) : (
          <div className="w-full aspect-video bg-thumb-bg flex items-center justify-center">
            <span className="font-mono text-[10px] tracking-widest text-border">
              SPEAKERDECK
            </span>
          </div>
        )}
        <AnimatePresence>
          {hovered && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.2 }}
              className="absolute inset-0 flex flex-col justify-end p-3.5 bg-gradient-to-t from-black/90 via-black/50 to-transparent"
            >
              <motion.div
                initial={{ y: 10, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                exit={{ y: 10, opacity: 0 }}
                transition={{ duration: 0.2, delay: 0.05 }}
              >
                <div className="text-xs text-white leading-relaxed mb-1">
                  {talk.title}
                </div>
                <div className="font-mono text-[10px] tracking-wider text-white/60">
                  {formatDate(talk.date)}
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </motion.a>
  );
}

function MarqueeRow({
  talks,
  direction,
  duration,
}: {
  talks: Talk[];
  direction: "left" | "right";
  duration: number;
}) {
  const [paused, setPaused] = useState(false);
  // Triplicate for seamless looping
  const items = [...talks, ...talks, ...talks];

  return (
    <div
      className="overflow-hidden"
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
    >
      <div
        className="flex gap-3 w-max"
        style={{
          animation: `marquee-${direction} ${duration}s linear infinite`,
          animationPlayState: paused ? "paused" : "running",
        }}
      >
        {items.map((talk, i) => (
          <TalkItem key={`${talk.url}-${i}`} talk={talk} />
        ))}
      </div>
    </div>
  );
}

export default function TalkMarquee({ talks }: { talks: Talk[] }) {
  const mid = Math.ceil(talks.length / 2);
  const row1 = talks.slice(0, mid);
  const row2 = talks.slice(mid);

  return (
    <div className="flex flex-col gap-3 -mx-6">
      <style>{`
        @keyframes marquee-left {
          0% { transform: translateX(0); }
          100% { transform: translateX(calc(-100% / 3)); }
        }
        @keyframes marquee-right {
          0% { transform: translateX(calc(-100% / 3)); }
          100% { transform: translateX(0); }
        }
      `}</style>
      <MarqueeRow talks={row1} direction="left" duration={50} />
      <MarqueeRow talks={row2} direction="right" duration={55} />
    </div>
  );
}
