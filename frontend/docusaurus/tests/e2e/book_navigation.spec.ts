// frontend/docusaurus/tests/e2e/book_navigation.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Book Navigation', () => {
  test('should navigate to the homepage', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Docusaurus/);
  });

  test('should navigate to a documentation page', async ({ page }) => {
    await page.goto('/docs/intro'); // Assuming 'intro' is a default Docusaurus doc page
    await expect(page.locator('h1')).toHaveText('Welcome'); // Assuming the title of intro.md is Welcome
  });

  test('should navigate using the table of contents', async ({ page }) => {
    await page.goto('/docs/intro');
    // Assuming Docusaurus generates a table of contents with links
    await page.click('nav.toc li a:has-text("Welcome")'); // Click on a link in the TOC
    await expect(page.locator('h1')).toHaveText('Welcome'); // Verify navigation
  });
});
