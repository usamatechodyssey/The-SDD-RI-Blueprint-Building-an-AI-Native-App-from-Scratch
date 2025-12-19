import React from 'react';
import { Cpu, Code2, Zap } from 'lucide-react';

export default function Features() {
  return (
    <section className="py-24 bg-slate-50 dark:bg-[#0b1120]">
      <div className="container px-4 mx-auto">
        <div className="mb-16 text-center">
          <h2 className="text-3xl font-bold md:text-5xl dark:text-white">
            Everything you need to <span className="text-gradient">Master AI</span>
          </h2>
          <p className="mt-4 text-lg text-slate-600 dark:text-slate-400">
            A complete ecosystem for the modern developer.
          </p>
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3 md:grid-rows-2 h-auto md:h-[600px]">
          {/* Large Card Left */}
          <div className="col-span-1 md:col-span-2 row-span-2 relative overflow-hidden rounded-3xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xl p-8 flex flex-col justify-between group hover:border-blue-500/50 transition-colors">
            <div className="z-10">
              <div className="w-12 h-12 mb-4 rounded-xl bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center text-blue-600">
                <Cpu size={28} />
              </div>
              <h3 className="text-3xl font-bold mb-2 dark:text-white">AI-Native Architecture</h3>
              <p className="text-slate-600 dark:text-slate-400 text-lg max-w-md">
                Learn how to design systems where the LLM is the engine, not just a plugin. Covers
                RAG, Vector DBs, and Agent Orchestration.
              </p>
            </div>
            {/* Decorative Element */}
            <div className="absolute right-0 bottom-0 w-64 h-64 bg-gradient-to-tl from-blue-100 to-transparent dark:from-blue-900/20 rounded-tl-full translate-x-10 translate-y-10 group-hover:scale-110 transition-transform duration-500"></div>
          </div>

          {/* Small Card Top Right */}
          <div className="p-8 bg-white dark:bg-slate-800 rounded-3xl border border-slate-200 dark:border-slate-700 shadow-lg hover:-translate-y-1 transition-transform">
            <div className="flex items-center gap-4 mb-4">
              <div className="p-2 bg-purple-100 dark:bg-purple-900/30 rounded-lg text-purple-600">
                <Code2 size={24} />
              </div>
              <h4 className="text-xl font-bold dark:text-white">Dual Stack</h4>
            </div>
            <p className="text-slate-600 dark:text-slate-400">
              Master both Python (Backend/AI) and TypeScript (Frontend/UI) seamlessly.
            </p>
          </div>

          {/* Small Card Bottom Right */}
          <div className="p-8 bg-white dark:bg-slate-800 rounded-3xl border border-slate-200 dark:border-slate-700 shadow-lg hover:-translate-y-1 transition-transform">
            <div className="flex items-center gap-4 mb-4">
              <div className="p-2 bg-green-100 dark:bg-green-900/30 rounded-lg text-green-600">
                <Zap size={24} />
              </div>
              <h4 className="text-xl font-bold dark:text-white">Spec-Driven</h4>
            </div>
            <p className="text-slate-600 dark:text-slate-400">
              Write specs, generate code. The future of high-speed development.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}