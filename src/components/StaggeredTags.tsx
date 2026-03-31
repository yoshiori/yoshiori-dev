import { motion, useReducedMotion } from "framer-motion";

interface Props {
  tags: string[];
  variant?: "default" | "accent";
}

export default function StaggeredTags({ tags, variant = "default" }: Props) {
  const shouldReduceMotion = useReducedMotion();

  const container = {
    hidden: {},
    visible: { transition: { staggerChildren: shouldReduceMotion ? 0 : 0.04 } },
  };

  const item = {
    hidden: { opacity: 0, scale: shouldReduceMotion ? 1 : 0.85 },
    visible: { opacity: 1, scale: 1 },
  };
  const base =
    "font-mono text-xs border px-3 py-1 tracking-wider transition-all duration-200";
  const styles =
    variant === "accent"
      ? `${base} text-accent/70 border-accent/30 hover:text-accent hover:border-accent glow-border-hover`
      : `${base} text-muted border-border hover:text-text hover:border-border-hover`;

  return (
    <motion.div
      className="flex flex-wrap gap-2"
      variants={container}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: "-60px" }}
    >
      {tags.map((name) => (
        <motion.span key={name} className={styles} variants={item}>
          {name}
        </motion.span>
      ))}
    </motion.div>
  );
}
