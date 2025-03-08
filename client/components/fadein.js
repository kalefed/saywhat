"use client";

import { motion } from "motion/react";

export default function Fadein({ children }) {
  return (
    <motion.div
      initial={{ opacity: 0 }} // Start invisible
      animate={{ opacity: 1 }} // Fade in to full opacity
      exit={{ opacity: 0 }} // Fade out when the component exits (if using transitions)
      transition={{ duration: 3 }} // Duration of the fade-in
    >
      {children}
    </motion.div>
  );
}
