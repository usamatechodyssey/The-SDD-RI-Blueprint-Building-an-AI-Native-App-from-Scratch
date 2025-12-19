import React from 'react';
import Link from '@docusaurus/Link';
import { motion } from 'framer-motion';
import { ArrowRight, Terminal } from 'lucide-react';

export default function Hero() {
  return (
    <section className="relative pt-24 pb-32 overflow-hidden">
      {/* Background Texture */}
      <div className="absolute inset-0 bg-grid-pattern pointer-events-none" />
      <div className="hero-glow" />

      <div className="container relative z-10 px-4 mx-auto text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="inline-flex items-center gap-2 px-3 py-1 mb-8 text-sm font-medium text-blue-700 bg-blue-100 rounded-full dark:bg-blue-900/30 dark:text-blue-300 ring-1 ring-blue-700/10"
        >
          <span className="relative flex w-2 h-2 mr-1">
            <span className="absolute inline-flex w-full h-full bg-blue-400 rounded-full opacity-75 animate-ping"></span>
            <span className="relative inline-flex w-2 h-2 bg-blue-500 rounded-full"></span>
          </span>
          v1.0 Public Beta Now Live
        </motion.div>

        <h1 className="mb-6 text-6xl font-black tracking-tight text-slate-900 dark:text-white md:text-8xl">
          Build <span className="text-gradient">Intelligent</span> <br />
          Software Systems
        </h1>

        <p className="max-w-2xl mx-auto mb-10 text-xl text-slate-600 dark:text-slate-400">
          The definitive guide to moving from <b>AI-Assisted</b> coding to building <b>AI-Native</b>{' '}
          architectures. Master Python, TypeScript, and Agentic workflows.
        </p>


        <div className="flex flex-col justify-center gap-4 sm:flex-row">
          <Link
            to="/docs/category/introduction"
            className="flex items-center justify-center px-8 py-4 text-lg font-bold text-white transition-all transform rounded-xl bg-slate-900 hover:bg-slate-800 hover:-translate-y-1 shadow-2xl shadow-slate-900/20 dark:bg-white dark:text-slate-900"
          >
            Start Reading
            <ArrowRight className="w-5 h-5 ml-2" />
          </Link>
          <Link
            to="https://github.com/usamatechodyssey"
            className="flex items-center justify-center px-8 py-4 text-lg font-bold transition-all transform bg-white border border-slate-200 rounded-xl text-slate-700 hover:bg-slate-50 hover:-translate-y-1 dark:bg-slate-800 dark:border-slate-700 dark:text-white dark:hover:bg-slate-700"
          >
            <Terminal className="w-5 h-5 mr-2" />
            View Source
          </Link>
        </div>
      </div>
    </section>
  );
}