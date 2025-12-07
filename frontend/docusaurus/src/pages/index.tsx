import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { motion } from 'framer-motion';
import { ArrowRight, Terminal, Cpu, BookOpen, Layers, Zap, Shield, Code2 } from 'lucide-react';

function HeroSection() {
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
            to="/docs/introduction"
            className="flex items-center justify-center px-8 py-4 text-lg font-bold text-white transition-all transform rounded-xl bg-slate-900 hover:bg-slate-800 hover:-translate-y-1 shadow-2xl shadow-slate-900/20 dark:bg-white dark:text-slate-900"
          >
            Start Reading
            <ArrowRight className="w-5 h-5 ml-2" />
          </Link>
          <Link
            to="https://github.com/panaversity"
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

function BentoGrid() {
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

function CurriculumSection() {
  const chapters = [
    {
      title: 'Foundation',
      desc: 'Setting up Python 3.12, Poetry, and Node.js envs.',
      icon: Layers,
    },
    { title: 'AI-Assisted', desc: 'Using Copilot and Cursor to write 2x faster.', icon: Zap },
    { title: 'RAG Systems', desc: 'Building your first Chatbot with Qdrant.', icon: BookOpen },
    { title: 'Agentic AI', desc: 'Autonomous agents that can use tools.', icon: Shield },
  ];

  return (
    <section className="py-24 border-t border-slate-200 dark:border-slate-800">
      <div className="container px-4 mx-auto">
        <div className="flex flex-col md:flex-row gap-12 items-center">
          <div className="flex-1">
            <h2 className="text-4xl font-bold mb-6 dark:text-white">What you will learn</h2>
            <p className="text-lg text-slate-600 dark:text-slate-400 mb-8">
              A step-by-step journey from writing your first prompt to deploying scalable AI agents
              in production.
            </p>
            <div className="space-y-6">
              {chapters.map((c, i) => (
                <div key={i} className="flex gap-4">
                  <div className="mt-1 flex-shrink-0 w-8 h-8 rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center font-bold text-slate-500">
                    {i + 1}
                  </div>
                  <div>
                    <h4 className="text-xl font-bold dark:text-white">{c.title}</h4>
                    <p className="text-slate-500 dark:text-slate-500">{c.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
          <div className="flex-1 bg-slate-900 rounded-2xl p-8 shadow-2xl rotate-2 hover:rotate-0 transition-transform duration-500">
            <pre className="text-blue-400 font-mono text-sm overflow-hidden">
              {`# AI-Native Manifest
class Agent(Reusability):
    def __init__(self):
        self.brain = LLM()
        self.memory = VectorDB()

    def act(self, goal):
        plan = self.brain.think(goal)
        return self.execute(plan)

# Deploying...
>>> Agent is now live.
`}
            </pre>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="AI Native Software Development Book"
    >
      <main className="min-h-screen bg-white dark:bg-[#0f172a]">
        <HeroSection />
        <BentoGrid />
        <CurriculumSection />
      </main>
    </Layout>
  );
}
