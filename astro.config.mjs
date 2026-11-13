import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://darkokostic95.github.io',
  base: '/biljina-kuhinja',
  trailingSlash: 'always',
  integrations: [sitemap()],
  build: { format: 'directory' },
  devToolbar: { enabled: false },
});
