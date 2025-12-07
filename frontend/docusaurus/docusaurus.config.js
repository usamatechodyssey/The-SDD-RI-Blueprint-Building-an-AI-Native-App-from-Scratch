// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const prismThemes = require('prism-react-renderer').themes;

/** @type {import('@docusaurus/types').Config} */
const config = {
  // --- 1. Site Metadata (Branding) ---
  title: 'AI Native Dev',
  tagline: 'Spec-Driven Reusable Intelligence',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'http://localhost:3000',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/',

  // GitHub pages deployment config.
  organizationName: 'panaversity', // Your GitHub Org
  projectName: 'ai-native-book', // Your Repo Name

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Internationalization
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Edit URL remove kar diya hai taake "Edit this page" ka link na dikhe (Optional)
          editUrl: undefined, 
        },
        blog: {
          showReadingTime: true,
          editUrl: undefined,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Social Card Image
      image: 'img/docusaurus-social-card.jpg',
      
      // --- 2. Navbar Configuration ---
      navbar: {
        title: 'AI Native Dev', // Website ke top-left mein ye dikhega
        
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Read Book',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/panaversity',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },

      // --- 3. Mega Footer Configuration ---
      footer: {
        style: 'light',
        links: [
          {
            title: 'Learn',
            items: [
              { label: 'Introduction', to: '/docs/introduction' },
              { label: 'AI Assisted', to: '/docs/introduction' },
              { label: 'AI Native', to: '/docs/introduction' },
            ],
          },
          {
            title: 'Community',
            items: [
              { label: 'Discord', href: 'https://discord.com' },
              { label: 'Twitter', href: 'https://twitter.com' },
              { label: 'GitHub', href: 'https://github.com' },
            ],
          },
          {
            title: 'More',
            items: [
              { label: 'Blog', to: '/blog' },
              { label: 'Panaversity', href: 'https://www.panaversity.org/' },
              { label: 'Privacy Policy', to: '/' },
            ],
          },
          {
            title: 'Legal',
            items: [
              { label: 'Terms', to: '/' },
              { label: 'License', to: '/' },
            ]
          }
        ],
        copyright: `Copyright © ${new Date().getFullYear()} AI Native Software Development. Built with Spec-Kit.`,
      },

      // Code Highlight Theme
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

module.exports = config;