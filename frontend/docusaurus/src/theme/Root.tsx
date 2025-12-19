import React from 'react';
import CustomChat from '@site/src/components/Chatbot/index'; // @site ka matlab project root hai

// Yeh component poori website ke har page ko wrap karta hai
export default function Root({children}) {
  return (
    <>
      {children}
      {/* 🤖 Ab chatbot har page par persistent rahega! */}
      <CustomChat />
    </>
  );
}