import React from 'react';
import { Layers, Zap, BookOpen, Shield } from 'lucide-react';

export default function Curriculum() {
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
          
          {/* Code Snippet Visual */}
          <div className="flex-1 bg-slate-900 rounded-2xl p-8 shadow-2xl rotate-2 hover:rotate-0 transition-transform duration-500">
            <div className="flex gap-2 mb-4">
              <div className="w-3 h-3 rounded-full bg-red-500"/>
              <div className="w-3 h-3 rounded-full bg-yellow-500"/>
              <div className="w-3 h-3 rounded-full bg-green-500"/>
            </div>
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