// frontend/docusaurus/.eslint.config.js
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import pluginReact from 'eslint-plugin-react';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ['**/*.{js,jsx,ts,tsx}'],
    
    languageOptions: {
      parser: tseslint.parser,
      parserOptions: {
        ecmaFeatures: {
          jsx: true,
        },
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
      globals: {
        browser: true,
        node: true,
        es2021: true,
      },
    },
    plugins: {
      react: pluginReact,
    },
    rules: {
      // Add your custom ESLint rules here
    },
  },
);