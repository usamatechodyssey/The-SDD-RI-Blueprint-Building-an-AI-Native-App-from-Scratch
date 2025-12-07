// frontend/docusaurus/tests/e2e/chatbot_interacion.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Chatbot Interaction', () => {
  test('should display chatbot UI', async ({ page }) => {
    await page.goto('/');
    // Assuming a chatbot icon or button exists
    await expect(page.locator('.chatbot-button')).toBeVisible();
  });

  test('should send a message to the chatbot', async ({ page }) => {
    await page.goto('/');
    await page.click('.chatbot-button'); // Open chatbot
    await page.fill('.chatbot-input', 'Hello, bot!'); // Type message
    await page.press('.chatbot-input', 'Enter'); // Send message
    await expect(page.locator('.chatbot-messages')).toContainText('Hello, bot!'); // Verify message sent
  });

  test('should receive a response from the chatbot', async ({ page }) => {
    await page.goto('/');
    await page.click('.chatbot-button'); // Open chatbot
    await page.fill('.chatbot-input', 'What is Docusaurus?'); // Type message
    await page.press('.chatbot-input', 'Enter'); // Send message
    // Assuming the bot responds with some text containing "Docusaurus"
    await expect(page.locator('.chatbot-messages')).toContainText('Docusaurus'); // Verify bot response
  });
});
