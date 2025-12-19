import React, { useState, useEffect, useRef } from 'react';
import { Send, X, Bot, Sparkles, MessageSquare, ChevronDown } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

// Purana: 'the-sdd-ri-blueprint-building-an-ai-native-app-f-production.up.railway.app'
// Naya (Correct): 👇
const BOOK_BACKEND_URL = 'https://the-sdd-ri-blueprint-building-an-ai-native-app-f-production.up.railway.app';

export default function CustomChat() {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Dynamic Configuration State
  const [botConfig, setBotConfig] = useState({
    url: '',
    key: '',
    name: 'Loading...',
    tagline: 'Please wait',
  });
  const [messages, setMessages] = useState([
    { role: 'bot', content: 'Initializing AI Architect...' },
  ]);

  const scrollRef = useRef<HTMLDivElement>(null);

  // 1. FETCH CONFIG ON MOUNT (Remote configuration logic) 🚀
  useEffect(() => {
    async function fetchConfig() {
      try {
        const response = await fetch(`${BOOK_BACKEND_URL}/admin/chatbot-config`);
        const data = await response.json();
        setBotConfig({
          url: data.apiUrl,
          key: data.apiKey,
          name: data.botName, // Dynamic Name 🚀
          tagline: data.botTagline, // Dynamic Tagline 🚀
        });

        // Config milne ke baad asli welcome message
        setMessages([
          {
            role: 'bot',
            content:
              'Hello! I am your SDD Architect. Connection established. Ready to dive into technical details?',
          },
        ]);
      } catch (error) {
        setMessages([
          { role: 'bot', content: '❌ System Error: Could not load remote AI configuration.' },
        ]);
      }
    }
    fetchConfig();
  }, []);

  // Auto Scroll Logic
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isLoading]);

  const handleSendMessage = async () => {
    if (!input.trim() || isLoading || !botConfig.url) return;

    const userMsg = input;
    setInput('');
    setMessages((prev) => [...prev, { role: 'user', content: userMsg }]);
    setIsLoading(true);

    try {
      // API call using dynamic URL and Key
      const response = await fetch(`${botConfig.url}/api/v1/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMsg,
          api_key: botConfig.key,
          session_id: 'premium_session',
        }),
      });

      const data = await response.json();

      if (response.status === 200) {
        setMessages((prev) => [...prev, { role: 'bot', content: data.response || 'No response' }]);
      } else {
        setMessages((prev) => [
          ...prev,
          { role: 'bot', content: '🚫 Security Alert: Domain or Key rejected by AI server.' },
        ]);
      }
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: 'bot', content: '📡 Server busy. Please try again later.' },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed bottom-4 right-4 sm:bottom-6 sm:right-6 z-[10000] flex flex-col items-end selection:bg-green-200 font-sans">
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.8, y: 20, rotate: -5, transformOrigin: 'bottom right' }}
            animate={{ opacity: 1, scale: 1, y: 0, rotate: 0 }}
            exit={{ opacity: 0, scale: 0.8, y: 20, rotate: 5 }}
            transition={{ type: 'spring', damping: 20, stiffness: 200 }}
            className="mb-4 w-[calc(100vw-2rem)] sm:w-[360px] h-[500px] max-h-[70vh] bg-white dark:bg-slate-950 rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.5)] border border-white/20 dark:border-slate-600 flex flex-col overflow-hidden origin-bottom-right"
          >
            {/* --- HEADER --- */}
            <div className="p-5 bg-gradient-to-br from-slate-900 via-[#1a4a35] to-[#2e8555] text-white flex justify-between items-center relative overflow-hidden shrink-0">
              <motion.div
                animate={{ opacity: [0.3, 0.6, 0.3] }}
                transition={{ repeat: Infinity, duration: 3 }}
                className="absolute top-0 left-0 w-full h-full bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20"
              />
              <div className="flex items-center gap-4 relative z-10">
                <div className="relative">
                  <div className="w-12 h-12 bg-[#2e8555] rounded-2xl flex items-center justify-center shadow-lg shadow-green-500/40 border border-green-400/30">
                    <Bot size={28} className="text-white" />
                  </div>
                  <span className="absolute -bottom-1 -right-1 w-4 h-4 bg-[#3b82f6] border-2 border-slate-900 rounded-full animate-pulse"></span>
                </div>
                <div>
                  <h3 className="text-lg font-bold tracking-tight leading-none">
                    {botConfig.name}
                  </h3>
                  <p className="text-[10px] uppercase tracking-widest mt-1 text-green-200 font-bold">
                    {botConfig.tagline}
                  </p>
                </div>
              </div>
              <button
                onClick={() => setIsOpen(false)}
                className="w-10 h-10 rounded-xl bg-white/10 hover:bg-[#2e8555] flex items-center justify-center transition-all duration-300 group relative z-10"
              >
                <ChevronDown
                  size={24}
                  className="group-hover:translate-y-0.5 transition-transform"
                />
              </button>
            </div>

            {/* --- CHAT AREA --- */}
            <div
              ref={scrollRef}
              className="flex-1 p-6 overflow-y-auto space-y-6 custom-scrollbar bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] dark:opacity-100"
            >
              {messages.map((msg, idx) => (
                <motion.div
                  initial={{ opacity: 0, y: 20, scale: 0.9 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  key={idx}
                  className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} items-end gap-2`}
                >
                  {msg.role === 'bot' && (
                    <div className="w-8 h-8 rounded-lg bg-slate-200 dark:bg-slate-700 flex items-center justify-center shrink-0 mb-1">
                      <Sparkles size={16} className="text-[#2e8555]" />
                    </div>
                  )}
                  <div
                    className={`px-5 py-3 rounded-2xl text-sm leading-relaxed shadow-sm max-w-[85%] ${
                      msg.role === 'user'
                        ? 'bg-[#2e8555] text-white rounded-br-none font-medium'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-100 border border-slate-200 dark:border-slate-700 rounded-bl-none'
                    }`}
                  >
                    {msg.content}
                  </div>
                </motion.div>
              ))}

              {isLoading && (
                <div className="flex justify-start items-end gap-2">
                  <div className="w-8 h-8 rounded-lg bg-slate-200 dark:bg-slate-700 flex items-center justify-center shrink-0">
                    <LoaderIcon />
                  </div>
                  <div className="bg-slate-100 dark:bg-slate-800 px-5 py-4 rounded-2xl rounded-bl-none border border-slate-200 dark:border-slate-700 shadow-sm">
                    <div className="flex gap-1.5">
                      {[0, 0.2, 0.4].map((d) => (
                        <motion.div
                          key={d}
                          animate={{ y: [0, -6, 0] }}
                          transition={{ repeat: Infinity, duration: 0.6, delay: d }}
                          className="w-2 h-2 bg-[#2e8555] rounded-full"
                        />
                      ))}
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* --- INPUT AREA --- */}
            <div className="p-4 bg-white dark:bg-slate-950 border-t border-slate-100 dark:border-slate-800 shrink-0">
              <div className="flex items-center gap-2 bg-slate-50 dark:bg-slate-800/80 border-2 border-slate-100 dark:border-slate-700 rounded-2xl p-1.5 focus-within:border-[#2e8555] transition-all">
                <input
                  type="text"
                  value={input}
                  disabled={!botConfig.url || isLoading}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                  placeholder={botConfig.url ? 'Ask a question...' : 'Loading system...'}
                  className="flex-1 bg-transparent px-4 py-3 text-sm text-slate-800 dark:text-white placeholder:text-slate-400 outline-none w-full"
                />

                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={handleSendMessage}
                  disabled={isLoading || !botConfig.url}
                  className="w-10 h-10 bg-[#2e8555] text-white rounded-xl flex items-center justify-center shadow-md shadow-green-500/20 disabled:opacity-50 shrink-0"
                >
                  <Send size={18} />
                </motion.button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* --- TOGGLE BUTTON --- */}
      <motion.button
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        animate={isOpen ? { borderRadius: '20px' } : { borderRadius: '50%' }}
        onClick={() => setIsOpen(!isOpen)}
        className="h-14 w-14 sm:h-16 sm:w-16 bg-gradient-to-tr from-[#2e8555] to-[#3b82f6] text-white shadow-[0_10px_30px_rgba(46,133,85,0.4)] flex items-center justify-center group border-2 border-white/20 relative shrink-0 z-50"
      >
        <AnimatePresence mode="wait">
          {isOpen ? (
            <motion.div
              key="close"
              initial={{ rotate: -90, opacity: 0 }}
              animate={{ rotate: 0, opacity: 1 }}
              exit={{ rotate: 90, opacity: 0 }}
            >
              <X size={28} />
            </motion.div>
          ) : (
            <motion.div
              key="msg"
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              exit={{ scale: 0 }}
              className="relative"
            >
              <MessageSquare size={28} fill="white" />
              <motion.div
                animate={{ scale: [1, 1.5, 1], opacity: [0.5, 0, 0.5] }}
                transition={{ repeat: Infinity, duration: 2 }}
                className="absolute -top-1 -right-1 w-4 h-4 bg-[#3b82f6] rounded-full"
              />
            </motion.div>
          )}
        </AnimatePresence>
      </motion.button>
    </div>
  );
}

function LoaderIcon() {
  return (
    <motion.div
      animate={{ rotate: 360 }}
      transition={{ repeat: Infinity, duration: 2, ease: 'linear' }}
    >
      <Sparkles size={16} className="text-[#2e8555]" />
    </motion.div>
  );
}
