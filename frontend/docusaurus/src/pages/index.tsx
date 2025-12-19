import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

// Components
import Hero from '../components/Homepage/Hero';
import Features from '../components/Homepage/Features';
import Curriculum from '../components/Homepage/Curriculum';
import CustomChat from '../components/Chatbot/index'; // <--- Naya Import

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="AI Native Software Development Book"
    >
      <main className="min-h-screen bg-white dark:bg-[#0f172a]">
        <Hero />
        <Features />
        <Curriculum />

        {/* 🤖 Custom Chatbot UI yahan add karein */}
        <CustomChat />
      </main>
    </Layout>
  );
}
